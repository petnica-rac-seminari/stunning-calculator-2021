from keras.datasets import mnist

(X, y), (Xt, yt) = mnist.load_data() #training and testing data

print('X_train: ' + str(X.shape))
print('Y_train: ' + str(y.shape))
print('X_test:  '  + str(Xt.shape))
print('Y_test:  '  + str(yt.shape))