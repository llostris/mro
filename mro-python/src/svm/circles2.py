from numpy.ma import floor
from sklearn.datasets import make_circles
from matplotlib import pyplot as plt
from sklearn.svm import SVC
import numpy as np

__author__ = 'Magda'


def plot_initial_data(X, y):
    greens = y == 1
    reds = y == 0
    plt.plot(X[reds, 0], X[reds, 1], "ro")
    plt.plot(X[greens, 0], X[greens, 1], "go")
    plt.show()

def split_dataset(vectors, groups, percentage_in_test_set):
    boundary = floor(percentage_in_test_set * 1.0 * len(vectors))
    return vectors[0:boundary], groups[0:boundary], vectors[boundary:], groups[boundary:]

def classification(X, y):
    train_set, y_train, test_set, y_test = split_dataset(X, y, 0.75)
    print len(train_set), len(y_train), len(test_set), len(y_test)

    svc = SVC(kernel='poly').fit(train_set, y_train)
    result = svc.predict(test_set)
    print 'result: %i' % (sum(result == y_test) * 1.0 / len(result))
    return train_set, y_train, test_set, y_test

kernels = [ 'rbf', 'poly', 'linear' ]

X, y = make_circles(n_samples=400, factor=.3, noise=.1)
plot_initial_data(X, y)
X_train, y_train, X_test, y_test = classification(X, y)

svc = SVC(kernel='linear', degree=2)
svc.fit(X, y)

xx, yy = np.meshgrid(np.linspace(-3, 3, 200), np.linspace(-3, 3, 200))
Z = svc.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.imshow(Z, interpolation='bicubic',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()), aspect='auto',
           origin='lower', cmap=plt.cm.RdBu_r)
contours = plt.contour(xx, yy, Z, levels=[0], linewidths=2,
                       linetypes='--')
plt.scatter(X[:, 0], X[:, 1], s=30, c=y, cmap=plt.cm.Paired)
plt.xticks(())
plt.yticks(())
plt.axis([-3, 3, -3, 3])
plt.show()
