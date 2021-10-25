import pandas as pd
import numpy as np
import random

import dataset
import utils

def PrepoznavanjeCifre(X):
    print('X JE OVO', X)
    X = dataset.normalize(X)
    print('X NORMALIZOVANO', X)

    w1 = pd.read_csv('parameters/parameters_w1.csv', sep=',',header=None)
    w1 = w1.to_numpy()
    w1 = w1[:, 1:]

    b1 = pd.read_csv('parameters/parameters_b1.csv', sep=',',header=None)
    b1 = b1.to_numpy()
    b1 = b1[:, 1:]

    w2 = pd.read_csv('parameters/parameters_w2.csv', sep=',',header=None)
    w2 = w2.to_numpy()
    w2 = w2[:, 1:]

    b2 = pd.read_csv('parameters/parameters_b2.csv', sep=',',header=None)
    b2 = b2.to_numpy()
    b2 = b2[:, 1:]

    w3 = pd.read_csv('parameters/parameters_w3.csv', sep=',',header=None)
    w3 = w3.to_numpy()
    w3 = w3[:, 1:]

    b3 = pd.read_csv('parameters/parameters_b3.csv', sep=',',header=None)
    b3 = b3.to_numpy()
    b3 = b3[:, 1:]
    
    z1 = X @ w1 + b1
    a1 = utils.ReLU(z1)

    z2 = a1 @ w2 + b2
    a2 = utils.ReLU(z2)

    z3 = a2 @ w3 + b3
    yh = utils.Softmax(z3)

    rez = 0
    
    print('OVO JE YH ', yh)

    for i in range (0, 10):
        if yh[0][i] > yh[0][rez]:
            rez = i
        pass
    return rez

_, _, primerX, primery = dataset.get_data()
index = int(random.random() * primerX.shape[0])
primerX = primerX[index]
primery = primery[index]
print(primery)
print("primerX type: ", type(primerX))
print("primerX[0] type: ", type(primerX[0]))
print("primerX: ", primerX)
print(PrepoznavanjeCifre(primerX))