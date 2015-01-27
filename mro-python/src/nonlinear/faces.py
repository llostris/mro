from os import listdir
from numpy.ma import mod, ceil
import scipy.misc
import numpy as np
from sklearn.decomposition import KernelPCA, PCA
from sklearn.manifold import LocallyLinearEmbedding
from sklearn.neighbors import NearestCentroid, KNeighborsClassifier

__author__ = 'Magda'

path = '../../yaleBfaces/zad1/'
dimensions = [ 10, 20, 50, 100]
neighbors = [ 10, 15, 50, 100]
kernels = [ 'poly', 'rbf', 'linear', 'sigmoid' ]

def load_data():
    files = listdir(path)

    faces = np.zeros(shape=(len(files), 2500))   # create matrix for all faces
    faces_index = 0
    for filename in files:
        # load image to numpy array
        face = scipy.misc.imread(path + filename)

        faces[faces_index] = face.ravel()
        faces_index += 1
    return faces, files

def split_datsets(dataset, training_number, per_class):
    # this scenario : dataset, 10, 9, 19
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

    # initial data
    no_dimensions = 1000
    neighbors = 50
    kernel = 'poly' # "linear" | "poly" | "rbf" | "sigmoid" | "cosine" | "precomputed"

    faces, filenames = load_data()
    print len(faces), len(faces[0])

    X_pca = PCA(n_components=no_dimensions).fit_transform(faces)
    results = X_pca

    # X_kpca = KernelPCA(kernel=kernel, n_components=no_dimensions, fit_inverse_transform=True).fit_transform(faces)
    # results = X_kpca
    #
    # X_lle = LocallyLinearEmbedding(n_neighbors=neighbors, n_components=no_dimensions).fit_transform(faces)
    # results = X_lle

    train_set, test_set, y_train, y_test = split_datsets(results, 7, 19)
    # print len(results), len(results[0])
    # print len(train_set), len(test_set), len(y_train)
    # print len(train_set[0]), len(test_set[0])
    # print y_train

    # NN
    result = KNeighborsClassifier(n_neighbors=1).fit(train_set, y_train).predict(test_set)
    percentage_nn = sum(result == y_test) * 1.0 / len(result)

    # closest centroid
    result = NearestCentroid().fit(train_set, y_train).predict(test_set)
    percentage_nc = sum(result == y_test) * 1.0 / len(result)

    print "%f\t%f" % (percentage_nn, percentage_nc)