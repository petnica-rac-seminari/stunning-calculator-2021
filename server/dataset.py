from mlxtend.data import loadlocal_mnist
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

def normalize(x: np.ndarray) -> np.ndarray:
    return (x - x.min()) / (x.max() - x.min())

def vectorize(y: np.ndarray) -> np.ndarray:
    vector_y = np.zeros((y.shape[0], 10))
    for i in range (0, y.shape[0]):
        vector_y[i, y[i]] = 1
    return vector_y

# staviti random redosled X-eva i y-ona
def get_data():
    X, y = loadlocal_mnist(
        "machine_learning/train-images.idx3-ubyte",
        "machine_learning/train-labels.idx1-ubyte"
    )
    Xt, yt = loadlocal_mnist(
        "machine_learning/t10k-images.idx3-ubyte",
        "machine_learning/t10k-labels.idx1-ubyte"
    )
    # i = 4
    # print(X[i])
    # print(y[i])

    # img = Image.new('L', (28, 28))
    # img.putdata(X[i])
    # img.show()

    # X = normalize(X)
    # Xt = normalize(Xt)

    y = vectorize(y)
    yt = vectorize(yt)

    return X, y, Xt, yt

get_data()