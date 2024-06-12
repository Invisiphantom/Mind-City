## Miniconda安装

https://developer.nvidia.com/cuda-downloads

```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt update
sudo apt -y install cuda-toolkit-12-5

mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash

conda remove --name PyT --all
conda create --name PyT python=3.12
conda activate PyT

pip install torch torchvision torchaudio 
pip install torchmetrics numpy pandas matplotlib jupyter seaborn 
pip install scikit-learn transformers datasets tokenizers accelerate altair 
pip install torch_tb_profiler tensorboard nltk sentencepiece networkx
pip uninstall

import torch
print(torch.__version__)
torch.cuda.is_available()

import nltk
nltk.download()
```

```cmd
python -m site
setx PYTHONNOUSERSITE 1
set PYTHONNOUSERSITE=1
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```
