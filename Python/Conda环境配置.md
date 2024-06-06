## Miniconda安装

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash

conda remove --name PyT --all
conda create --name PyT python=3.12
conda activate PyT

pip install torch torchvision torchaudio torchmetrics numpy pandas matplotlib jupyter seaborn scikit-learn transformers datasets tokenizers accelerate altair torch_tb_profiler tensorboard nltk sentencepiece

import torch
print(torch.__version__)
torch.cuda.is_available()

import nltk
nltk.download()

sudo apt install libglu1-mesa-dev
export LIBRARY_PATH=$LIBRARY_PATH:/usr/lib/wsl/lib
```
