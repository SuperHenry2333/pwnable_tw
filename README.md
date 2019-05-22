# pwnable_tw
Lean pwn!


<img src="http://latex.codecogs.com/gif.latex?\frac{\partial J}{\partial \theta_k^{(j)}}=\sum_{i:r(i,j)=1}{\big((\theta^{(j)})^Tx^{(i)}-y^{(i,j)}\big)x_k^{(i)}}+\lambda \theta_k^{(j)}" />



# Baseline

These are  our implementations of the baselines. 


## Modifications

Our implementations are based on [LibRec](https://github.com/guoguibing/librec), [Neural Collaborative Filtering](https://github.com/tensorflow/models/tree/master/official/recommendation) and [Variational autoencoders for collaborative filtering](https://github.com/dawenl/vae_cf.git). To fairly evaluate all baseline models, we reimplement the evaluation part of the programs we used. The measures for evaluation are defined as follows:


## Dependencies

- Librec need JDK 1.8
- NCF and VAE_MF runs well on python 3.6.6 with tensorflow-gpu 1.12.0

## Data

There is a script named data_convert.py in each directory to generate the data format from raw data. 
```
python ./data/convert_data.py --raw_train ../data/ml10m/train_feats.csv --raw_test ../data/ml10m/test_feats.csv --output ./data/ml10m
``` 

## Usage

Run
```
cd src
./run.sh
```
To run LibRec, you have to compile the java code into runable baseline.jar first.
