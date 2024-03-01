Ubuntu22.04配置OpenGL环境

```bash
sudo apt install build-essential g++
sudo apt install libgl-dev libglfw3-dev
```

https://glad.dav1d.de/
选择最新版本gl, 勾选"Local Files", 然后生成并下载


修改`.vscode/tasks.json`文件, 添加头文件和链接操作
```json
    "args": [
        "-fdiagnostics-color=always",
        "-g",
        "${file}",
        "${workspaceFolder}/glad/glad.c",
        "-o",
        "${fileDirname}/${fileBasenameNoExtension}",
        "-lGL",
        "-lglfw",
    ],
```

<br>


OpenGL教程: [LearnOpenGL](https://learnopengl.com/Getting-started/OpenGL)


[图解弄懂gl，glu，glut，glew，glfw之间关系-CSDN](https://blog.csdn.net/wangleizhenshuai/article/details/122960349)
[上帝视角看GPU：图形流水线基础_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1P44y1V7bu/?spm_id_from=333.1007.top_right_bar_window_history.content.click)
[最好的OpenGL教程之一_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1MJ411u7Bc/?spm_id_from=333.337.search-card.all.click&vd_source=c03ebf3c70dde0f2b5c39bf1f5ee258e)
[Cherno OpenGL教程 | Fl0w3r (yousazoe.top)](https://www.yousazoe.top/archives/cbd8aac2.html)
[LearnOpenGL CN (learnopengl-cn.github.io)](https://learnopengl-cn.github.io/intro/)


[Lecture 01 Overview of Computer Graphics_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1X7411F744?p=1&vd_source=c03ebf3c70dde0f2b5c39bf1f5ee258e)
[GAMES101: 现代计算机图形学入门 (ucsb.edu)](https://sites.cs.ucsb.edu/~lingqi/teaching/games101.html)

[OpenGL ES 2.0 知识串讲（1）――OpenGL ES 2.0 概括 (geekfaner.com)](http://geekfaner.com/shineengine/blog2_OpenGLESv2_1.html)
[OpenGL矩阵变换的数学推导-腾讯云开发者社区-腾讯云 (tencent.com)](https://cloud.tencent.com/developer/article/1389550)


  surface, context and thread    画布，画家与画室
  VBO   方案碎片    VAO    绘画方案

  3D渲染、动画制作、玩家交互、游戏逻辑

\#define GLEW_STATIC

