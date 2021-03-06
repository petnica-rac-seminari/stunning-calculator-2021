import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import dataset as data
import utils

X, y, tX, ty = data.get_data()

X = data.normalize(X)
tX = data.normalize(tX)

X = X[:15000]
tX = tX[:1000]

y = y[:15000]
ty = ty[:1000]

#region init w and b
k = 1e-2
w1 = np.random.uniform(-10, 10, (X.shape[1], 400)) * k
b1 = np.random.uniform(-10, 10, (1, 400)) * k

w2 = np.random.uniform(-10, 10, (400, 100)) * k
b2 = np.random.uniform(-10, 10, (1, 100)) * k

w3 = np.random.uniform(-10, 10, (100, 10)) * k
b3 = np.random.uniform(-10, 10, (1, 10)) * k
#endregion

#region hyperparams
epoch = int(1e2)
lr = 8e-1

L = []
#endregion

#region learning
for i in range (1, epoch + 1):
    if i % (epoch / 10) == 0:
        print("iteracija ", i)
    
    X, y = utils.Randomize(X, y)

    #region feed forward
    z1 = X @ w1 + b1
    a1 = utils.ReLU(z1)

    z2 = a1 @ w2 + b2
    a2 = utils.ReLU(z2)

    z3 = a2 @ w3 + b3
    yh = utils.Softmax(z3)

    L.append(utils.CELoss(y, yh))
    #endregion
    
    #region back propagation
    dz3 = (yh - y) / y.shape[0]
    dw3 = a2.transpose() @ dz3
    db3 = dz3.sum(axis=0)

    da2 = dz3 @ w3.transpose()
    dz2 = utils.dReLU(z2) * da2
    dw2 = a1.transpose() @ dz2
    db2 = dz2.sum(axis=0)

    da1 = dz2 @ w2.transpose()
    dz1 = utils.dReLU(z1) * da1
    dw1 = X.transpose() @ dz1
    db1 = dz1.sum(axis=0)
    #endregion

    #region learnig
    w3 -= lr * dw3
    b3 -= lr * db3

    w2 -= lr * dw2
    b2 -= lr * db2

    w1 -= lr * dw1
    b1 -= lr * db1
    #endregion

#endregion

#region testing
tz1 = tX @ w1 + b1
ta1 = utils.ReLU(tz1)

tz2 = ta1 @ w2 + b2
ta2 = utils.ReLU(tz2)

tz3 = ta2 @ w3 + b3
tyh = utils.Softmax(tz3)
#endregion

#region plot
print( np.sum( np.argmax( ty, axis=1 )==np.argmax( tyh, axis=1 ) ) )

plt.plot(L)
_, ax = plt.subplots(1, 2)
ax[0].matshow(ty)
ax[1].matshow(tyh)
plt.show()
#endregion


parameters = [w1, b1, w2, b2, w3, b3]
file_names = []
for i in range (0, len(parameters) // 2):
    file_names.append("parameters/parameters_w" + str(i+1) + ".csv")
    pd.DataFrame(parameters[2*i]).to_csv(file_names[-1], header=None)
    file_names.append("parameters/parameters_b" + str(i+1) + ".csv")
    pd.DataFrame(parameters[2*i+1]).to_csv(file_names[-1], header=None)
