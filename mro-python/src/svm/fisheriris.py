import random
from numpy.ma import floor, mean
from sklearn.neighbors import KNeighborsClassifier, NearestCentroid
from sklearn.datasets import load_iris
from sklearn.svm import SVC, LinearSVC

__author__ = 'Magda'

def split_dataset(vectors, groups, percentage_in_test_set):
    permutation = range(len(vectors))
    random.shuffle(permutation)
    vectors = [ vectors[i].tolist() for i in permutation ]
    groups = [ groups[i].tolist() for i in permutation ]
    boundary = int(floor(percentage_in_test_set * 1.0 * len(vectors)))
    return vectors[0:boundary], groups[0:boundary], vectors[boundary:], groups[boundary:]

success_rate = lambda x, y : sum(x == y) * 1.0 / len(x)

if __name__ == "__main__":
    kernels = [ 'rbf', 'poly', 'linear', 'sigmoid' ]
    iterations = 500

    iris = load_iris()
    X, y = iris.data, iris.target

    success_rate = lambda x, y : sum(x == y) * 1.0 / len(x)

    svc_kernels = { kernel : [] for kernel in kernels }
    svc_linear = []
    nn_all = []
    cn_all = []

    for i in range(iterations):
        X_train, y_train, X_test, y_test = split_dataset(X, y, 0.25)
        print len(X_train)

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
