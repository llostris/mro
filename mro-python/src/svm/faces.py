from os import listdir
import random
from numpy.ma import mod, ceil, mean
import scipy.misc
import numpy as np
from sklearn.neighbors import KNeighborsClassifier, NearestCentroid
from sklearn.svm import SVC, LinearSVC

__author__ = 'Magda'

train_set = 'training2/'
test_set = 'test2/'
path = '../../faces/'
kernels = [ 'poly', 'rbf', 'linear', 'sigmoid' ]

def load_data(path):
    files = listdir(path)

    faces = np.zeros(shape=(len(files), 2500))   # create matrix for all faces
    labels = []
    faces_index = 0
    for filename in files:
        # load image to numpy array
        face = scipy.misc.imread(path + filename)

        faces[faces_index] = face.ravel()
        labels.append(int(filename[6:8]))
        faces_index += 1
    return faces, labels


def split_dataset(dataset, labels, training_number, per_class):
    train_set = []
    test_set = []
    y_train = []
    y_test = []
    for i in range(len(dataset)):
        if mod(i, per_class) < training_number :
            train_set.append(dataset[i])
            y_train.append(ceil(i / per_class))
        else :
            test_set.append(dataset[i])
            y_test.append(ceil(i / per_class))

    return (train_set, test_set, y_train, y_test)


if __name__ == "__main__":
    iterations = 10

    X_train, y_train = load_data(path + train_set)
    X_test, y_test = load_data(path + test_set)

    success_rate = lambda x, y : sum(x == y) * 1.0 / len(x)

    svc_kernels = { kernel : [] for kernel in kernels }
    svc_linear = []
    nn_all = []
    cn_all = []

    for i in range(iterations):

        for kernel in kernels:
            svc = SVC(kernel=kernel).fit(X_train, y_train).predict(X_test)
            svc_kernels[kernel].append(success_rate(svc, y_test))

        svc = LinearSVC(multi_class='crammer_singer').fit(X_train, y_train).predict(X_test)
        svc_linear.append(success_rate(svc, y_test))

        nn = KNeighborsClassifier(n_neighbors=1).fit(X_train, y_train).predict(X_test)
        nn_all.append(success_rate(nn, y_test))

        cn = NearestCentroid().fit(X_train, y_train).predict(X_test)
        cn_all.append(success_rate(cn, y_test))

    for kernel in kernels:
        print mean(svc_kernels[kernel])

    print

    print mean(svc_linear)
    print mean(nn_all)
    print mean(cn_all)