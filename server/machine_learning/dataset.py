from mlxtend.data import loadlocal_mnist
import numpy as np

def normalize(x: np.ndarray) -> np.ndarray:
    return (x - x.min()) / (x.max() - x.min())

def vectorize(y: np.ndarray) -> np.ndarray:
    vector_y = np.zeros((y.shape[0], 10))
    for i in range (0, y.shape[0]):
        vector_y[i, y[i]] = 1
    print(vector_y[0])
    print(y[0])
    return vector_y

def get_data():
    X, y = loadlocal_mnist(
        "train-images.idx3-ubyte",
        "train-labels.idx1-ubyte"
    )
    Xt, yt = loadlocal_mnist(
        "t10k-images.idx3-ubyte",
        "t10k-labels.idx1-ubyte"
    )
    X = normalize(X)

    y = vectorize(y)
    yt = vectorize(yt)
    return X, y, Xt, yt

get_data()