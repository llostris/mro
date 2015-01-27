from numpy.numarray import arange

__author__ = 'Magda'

from math import cos, exp, sin, pi

from sklearn.decomposition import PCA
from sklearn.manifold import LocallyLinearEmbedding
import numpy as np
import matplotlib.pyplot as plt

#As a path collection

from matplotlib.collections import LineCollection



def spiral():


    # t = [0:0.01:(20*pi)];
    # x = ((exp(0.1*t)).*(cos(t)));
    # y = ((exp(0.1*t)).*(sin(t)));

    a = 1
    b = .1
    X = []
    Y = []

    for theta in arange(0, 20 * pi, 0.1):
        X.append(a*cos(theta)*exp(b * theta))
        Y.append(a*sin(theta)*exp(b * theta))

    # fig = plt.figure()
    # ax = fig.add_subplot(211)

    plt.plot(X, Y, color = 'g')
    plt.show()
    return X, Y

def run_pca(n, data):
    result = PCA(n_components=1).fit(data).transform(data)
    fig = plt.figure()
    plt.plot(result[:, 0], result[:, 1])
    plt.show()

def run_lle(n, data):
    result = LocallyLinearEmbedding(n, n_components=2, method='hessian').fit(data).transform(data)
    fig = plt.figure()
    plt.plot(result[:, 0], result[:, 1])
    plt.show()

if __name__ == "__main__":
    neighbors = 2
    X, Y = spiral()
    # data = [X, Y]
    data = np.array([ X, Y ])
    data = np.transpose(data)
    print data.shape
    # print data
    run_pca(1, data)
    run_lle(50, data)
