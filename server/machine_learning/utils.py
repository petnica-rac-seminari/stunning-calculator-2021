import numpy as np
import dataset as data


#region relu +
def ReLU(data):

    if (data > 0):
        return data
    else:
        return 0

def dReLU(data):
    if (data > 0):
        return 1
    else:
        return 0

#endregion



def Softmax(data):
    mxs = np.max(data, axis = 1).reshape(-1, 1)
    exps = np.exp(data - mxs)

    sums = np.sum(exps, axis = 1).reshape(-1, 1)

    return exps / sums
#endregion



def CELoss(y, yH): 
    return -np.sum(y * np.log(yH) ) / y.shape[0]





