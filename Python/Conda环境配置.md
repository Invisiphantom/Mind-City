## Miniconda安装

https://docs.anaconda.com/miniconda/
https://developer.nvidia.com/cuda-downloads

```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-6

mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash

conda remove --name PyT --all
conda create --name PyT python=3.12
conda activate PyT

pip install torch torchvision torchaudio
pip install torchmetrics numpy pandas matplotlib jupyter seaborn 
pip install scikit-learn transformers datasets tokenizers accelerate altair 
pip install torch_tb_profiler tensorboard nltk sentencepiece networkx kaggle
pip install opencv-python wandb ultralytics roboflow labelimg
pip uninstall

import torch
print(torch.__version__)
torch.cuda.is_available()

import nltk
nltk.download()

wandb login
https://wandb.ai/settings#api
```
