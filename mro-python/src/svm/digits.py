import os
import random
import struct
from numpy import array, mean
from numpy.ma import floor
from numpy.matrixlib import matrix
from sklearn.datasets import fetch_mldata
from sklearn.neighbors import KNeighborsClassifier, NearestCentroid
from sklearn.svm import SVC, LinearSVC
import numpy as np
from matplotlib import pyplot as plt

__author__ = 'Magda'

path = '../../'
def split_datasets(mnist, train_set_len, test_set_len):
    permutation = range(train_set_len + test_set_len)
    random.shuffle(permutation)
    vectors = [ mnist.data[i].tolist() for i in permutation ]
    groups = [ mnist.target[i].tolist() for i in permutation ]
    boundary = train_set_len
    return vectors[0:boundary], groups[0:boundary], vectors[boundary:], groups[boundary:]

def visualise(X, y):
    print len(X), len(y), len(X[0])
    svc = SVC(kernel='linear', degree=2)
    svc.fit(X, y)

    h = .02
    x_min, x_max = min(X[:][0]) - 1, max(X[:][0]) + 1
    y_min, y_max = min(X[:][1]) - 1, max(X[:][1]) + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    color_map = {-1: (1, 1, 1), 0: (0, 0, .9), 1: (1, 0, 0), 2: (.8, .6, 0)}

    Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
    plt.axis('off')

    # Plot also the training points
    colors = [color_map[y] for y in y_train]
    plt.scatter(X[:, 0], X[:, 1], c=colors, cmap=plt.cm.Paired)
    plt.show()


if __name__ == "__main__":
    mnist = fetch_mldata('MNIST original', data_home=path)
    print mnist.data.shape
    X_train, y_train, X_test, y_test = split_datasets(mnist, 200, 5800)

    kernels = [ 'rbf', 'poly', 'linear', 'sigmoid' ]
    iterations = 3

    success_rate = lambda x, y : sum(x == y) * 1.0 / len(x)

    svc_kernels = { kernel : [] for kernel in kernels }
    svc_linear = []
    nn_all = []
    cn_all = []

    for i in range(iterations):

        for kernel in kernels:
            svc = SVC(kernel=kernel).fit(X_train, y_train).predict(X_test)
            svc_kernels[kernel].append(success_rate(svc, y_test))

        nn = KNeighborsClassifier(n_neighbors=1).fit(X_train, y_train).predict(X_test)
        nn_all.append(success_rate(nn, y_test))

        cn = NearestCentroid().fit(X_train, y_train).predict(X_test)
        cn_all.append(success_rate(cn, y_test))

    for kernel in kernels:
        print mean(svc_kernels[kernel])

    print

    print mean(nn_all)
    print mean(cn_all)

    # visualise(X_train + X_test, y_train + y_test)