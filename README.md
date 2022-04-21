# An Unofficial Pytorch Implementation of MVSNet

[MVSNet: Depth Inference for Unstructured Multi-view Stereo](https://arxiv.org/abs/1804.02505). Yao Yao, Zixin Luo, Shiwei Li, Tian Fang, Long Quan. ECCV 2018. MVSNet is a deep learning architecture for depth map inference from unstructured multi-view images.

This is an unofficial Pytorch implementation of MVSNet done as part of a Thesis project.

## How to Use

### Environment
* python >= 3.6 (Anaconda)
* pytorch >= 1.0.1

### Download

The complete training and testing data can be downloaded from [Gaurav-Gosain/dissertation_data (github.com)](https://github.com/Gaurav-Gosain/dissertation_data).


### Training

* Download the preprocessed [DTU training data](https://drive.google.com/file/d/1eDjh-_bxKKnEuz5h-HXS7EDJn59clx6V/view) (Fixed training cameras, from [Original MVSNet](https://github.com/YoYo000/MVSNet)), and upzip it as the ``MVS_TRANING`` folder
* in ``train.sh``, set ``MVS_TRAINING`` as your training data path
* create a logdir called ``checkpoints``
* Train MVSNet: ``./train.sh``

### Testing

* Download the preprocessed test data [DTU testing data](https://drive.google.com/open?id=135oKPefcPTsdtLRzoDAQtPpHuoIrpRI_) (from [Original MVSNet](https://github.com/YoYo000/MVSNet)) and unzip it as the ``DTU_TESTING`` folder, which should contain one ``cams`` folder, one ``images`` folder and one ``pair.txt`` file.
* in ``test.sh``, set ``DTU_TESTING`` as your testing data path and ``CKPT_FILE`` as your checkpoint file. You can also download my [pretrained model](https://drive.google.com/file/d/1j2I_LNKb9JeCl6wdA7hh8z1WgVQZfLU9/view?usp=sharing).
* Test MVSNet: ``./test.sh``

### Fusion

in ``eval.py``, I implemented a simple version of depth map fusion.

### Evaluation

The matlab based evaluation code provided by the DTU Dataset is used to evaluate the results. The bare minimum code required for evaluation is present in the `/Evaluation` folder.

The Dissertation.ipynb is a Jupyter Notebook that contains the final code for the entire implementation.

The Dissertation_tpu.ipynb is a Jupyter Notebook that contains the code adapted to work with the pytorch lightning framework.