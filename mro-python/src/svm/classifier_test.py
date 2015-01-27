import random
from numpy.ma import mean, floor
from sklearn.datasets import load_iris
from sklearn.neighbors import NearestCentroid, KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC

__author__ = 'Magda'

class ClassifierTest:

    def __init__(self):
        self.kernels = [ 'rbf', 'poly', 'linear', 'sigmoid' ]
        self.classifiers = self.initialize_classifiers()
        self.results = [ [] for x in self.classifiers ]


    def initialize_classifiers(self):
        classifiers = []
        for kernel in self.kernels:
            print kernel
            fun = lambda X_train, y_train, X_test: SVC(kernel=kernel).fit(X_train, y_train).predict(X_test)
            classifiers.append(fun)

        fun = lambda X_train, y_train, X_test: LinearSVC(multi_class='crammer_singer').fit(X_train,
                                                                                             y_train).predict(X_test)
        classifiers.append(fun)

        fun = lambda X_train, y_train, X_test: KNeighborsClassifier(n_neighbors=1).fit(X_train, y_train).predict(
            X_test)
        classifiers.append(fun)

        fun = lambda X_train, y_train, X_test: NearestCentroid().fit(X_train, y_train).predict(X_test)
        classifiers.append(fun)

        return classifiers


    def success_rate(self, x, y):
        return sum(x == y) * 1.0 / len(x)


    def split_dataset(self, vectors, groups, percentage_in_test_set):
        permutation = range(len(vectors))
        random.shuffle(permutation)
        vectors = [ vectors[i].tolist() for i in permutation ]
        groups = [ groups[i].tolist() for i in permutation ]
        boundary = int(floor(percentage_in_test_set * 1.0 * len(vectors)))
        return vectors[0:boundary], groups[0:boundary], vectors[boundary:], groups[boundary:]


    def run_test(self, dataset, groups, iterations = 100, percentage_in_test_set = 0.75):
        for i in range(iterations):
            X_train, y_train, X_test, y_test = self.split_dataset(dataset, groups, percentage_in_test_set)

            for cls in self.classifiers:
                result = cls(X_train, y_train, X_test)
                self.results[self.classifiers.index(cls)].append(self.success_rate(result, y_test))

        print len(self.results)
        for i in self.results:
            print len(i)
        average = []

        for result in self.results:
            average.append(mean(result))

        for i in average:
            print i


if __name__ == "__main__":
    kernels = [ 'rbf', 'poly', 'linear', 'sigmoid' ]
    iterations = 100

    iris = load_iris()
    X, y = iris.data, iris.target

    ct = ClassifierTest()
    ct.run_test(X, y)