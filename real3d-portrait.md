## Real3D-Portrait功能与架构简介

Real3D-Portrait架构用于实现从未见过的人像照片和参考视频或音频中生成会说话的人像视频。这一任务可以被分解成为两个子任务：
（1）从输入人像图片中重建精确的三维人脸表示；
（2）对三维表示进行变形，并渲染出与驱动条件（运动或音频）相对应的会说话的人脸。

Real3D-Potrait的推理过程Pipeline示意图如下：

![Refer to caption](https://arxiv.org/html/2401.08503v2/x1.png)



### Image-to-Plane

首先，Real3D-Portrait使用一个Image-to-Plane模型将输入的人脸图像进行3D重建，转化为标准的tri-plane表示。这个模型由两大部分构成：

- ViT分支：这一分支使用了数个堆叠的SegFormer模块（见下图c），用于完成pixel-to-world标准化操作。
- VGG分支：由于ViT分支难以捕捉到图像中的高频分量，模块中引入了数个堆叠的卷积层，用以保留图像的高频特征。

这两部分的输出连接在一起，最后形成人脸模型的标准tri-plane表示。

![Refer to caption](https://arxiv.org/html/2401.08503v2/x2.png)



这一部分主要完成了任务（1），即从图像重建3D人脸。



### Motion Adapter & Volume Renderer

Motion Adapter模块的主要功能是根据重建的人脸模型和动作信息，合成3D人脸的动作。这一模块接收以PNCC编码的Source和Target人脸与动作信息，通过数个SegFormer模块和插值、采样，生成人脸动作的差分tri-plane表示。将它与Image-to-Plane模块中生成的人脸tri-plane结果相加，即可得到人脸的动画。Volume Renderer则负责根据前两步生成的人脸动画tri-plane表示，渲染出（较低分辨率的）人脸图像。



<img src="https://arxiv.org/html/2401.08503v2/x6.png" alt="Refer to caption" style="zoom: 50%;" />



这一部分主要完成了任务（2），即根据驱动信息来生成会说话的人脸。



### Head-Torso-Background Super-Resulotion

由Volume Renderer生成的人脸图像将与原始图片的人脸、躯干、背景信息一起传入Head-Torso-Background Super-Resolution（HTB-SR）模块中，生成高分辨率的图像，并且完成人脸、躯干和背景的自然融合。HTB-SR模块由背景分支（BG Branch）、躯干分支（Torso Branch）和人脸超分辨率分支（SR Branch）组成，它们使用了从原始图片中提取的人脸、躯干、背景信息，结合人脸的动作来预测三者的动态关系，在生成的视频中尽可能真实地还原背景信息。

<img src="https://arxiv.org/html/2401.08503v2/x7.png" alt="Refer to caption" style="zoom:50%;" />

HTB-SR模块在前两个子任务的基础上进行修正，使得最后合成的视频看起来更加自然，这也是Real3D-Portrait架构的重要创新点之一。