

https://docs.nerf.studio/quickstart/installation.html
https://colmap.github.io/install.html


```bash
conda create --name nerfstudio -y python=3.8
conda activate nerfstudio
python -m pip install --upgrade pip
pip install torch==2.1.2+cu118 torchvision==0.16.2+cu118 --extra-index-url https://download.pytorch.org/whl/cu118
conda install -c "nvidia/label/cuda-11.8.0" cuda-toolkit -y
pip install ninja git+https://github.com/NVlabs/tiny-cuda-nn/#subdirectory=bindings/torch
pip install nerfstudio
conda install -c conda-forge colmap
sudo apt install ffmpeg -y

ns-download-data nerfstudio --capture-name=poster
ns-train nerfacto --data data/nerfstudio/poster
```

| cmd              | desc           |
| ---------------- | -------------- |
| ns-download-data | 下载样例数据集 |
| ns-process-data  | 处理定制数据集 |
| ns-train         | 训练模型       |
| ns-render        | 渲染视频       |
| ns-export        | 导出点云       |


```bash
conda activate ns
ns-process-data video --data data/custom/bicycle/video.mp4 --output-dir data/custom/bicycle/
ns-process-data video --data data/custom/wangdao/video.mp4 --output-dir data/custom/wangdao/

ns-train splatfacto --data data/custom/bicycle/
ns-viewer --load-config outputs/bicycle/splatfacto/2024-06-10_111235/config.yml

ns-train splatfacto-big --data data/custom/book/
ns-viewer --load-config outputs/book/splatfacto/2024-06-10_124254/config.yml



ns-train splatfacto-big --data data/custom/bicycle/
ns-viewer --load-config outputs/bicycle/splatfacto/2024-06-10_113701/config.yml   


ns-train nerfacto-big --data data/custom/wangdao/
ns-viewer --load-config outputs/wangdao/nerfacto/2024-06-10_192114/config.yml  
ns-eval --load-config outputs/wangdao/nerfacto/2024-06-10_192114/config.yml \
--output-path eval/wangdao/nerfacto/2024-06-10_192114/output.json \
--render-output-path eval/wangdao/nerfacto/2024-06-10_192114

ns-train splatfacto-big --data data/custom/wangdao/
ns-viewer --load-config outputs/wangdao/splatfacto/2024-06-10_222845/config.yml  
ns-eval --load-config outputs/wangdao/splatfacto/2024-06-10_222845/config.yml \
--output-path eval/wangdao/splatfacto/2024-06-10_222845/output.json \
--render-output-path eval/wangdao/splatfacto/2024-06-10_222845


ns-train splatfacto-big \
--pipeline.model.cull_alpha_thresh=0.005 \
--pipeline.model.continue_cull_post_densification=False \
--pipeline.model.use_scale_regularization=True \
--data data/custom/wangdao/
ns-viewer --load-config outputs/wangdao/splatfacto/2024-06-11_184110/config.yml 
ns-eval --load-config outputs/wangdao/splatfacto/2024-06-11_184110/config.yml \
--output-path eval/wangdao/splatfacto/2024-06-11_184110/output.json \
--render-output-path eval/wangdao/splatfacto/2024-06-11_184110

