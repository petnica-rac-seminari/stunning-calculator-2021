import numpy as np

import dataset as data

X, y, Xt, yt = data.get_data()

#region init w and b
w1 = np.random.uniform(-10, 10, (X.shape[1], 400)) * 1e-1
b1 = np.random.uniform(-10, 10, (1, 400)) * 1e-1

w2 = np.random.uniform(-10, 10, (400 // 2, 100)) * 1e-1
b2 = np.random.uniform(-10, 10, (1, 100)) * 1e-1

w3 = np.random.uniform(-10, 10, (100, 10)) * 1e-1
b3 = np.random.uniform(-10, 10, (1, 10)) * 1e-1
#endregion

#region hyperparams
epoch = int(1e3)
lr = 1e-3

#endregion