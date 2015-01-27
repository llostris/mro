from sklearn.datasets import make_circles
from sklearn.decomposition import KernelPCA
from matplotlib import pyplot as plt

__author__ = 'Magda'

X, y = make_circles(n_samples=400, factor=.3, noise=.05)
greens = y == 1
reds = y == 0

# "linear" | "poly" | "rbf" | "sigmoid" | "cosine" | "precomputed"
kpca = KernelPCA(kernel="poly", fit_inverse_transform=True, gamma=10)
X_kpca = kpca.fit_transform(X)

plt.figure(0)
plt.subplot(1, 1, 1, aspect='equal')
plt.plot(X_kpca[greens, 0], X_kpca[greens, 1], "go")
plt.plot(X_kpca[reds, 0], X_kpca[reds, 1], "ro")
plt.show()