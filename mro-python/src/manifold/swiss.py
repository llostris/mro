from pylab import *
# from mpl_toolkits.mplot3d import Axes3D
from sklearn import manifold, datasets

# load Swiss roll dataset
X, color = datasets.samples_generator.make_swiss_roll(n_samples=1500)

# run Isomap on the points in X with 2 dim output
n_neighbors = 10
Y = manifold.Isomap(n_neighbors, 2).fit_transform(X)

# 3D plot
# fig = figure()
# ax = fig.gca(projection='3d')
# ax.scatter(X[:,0], X[:,1], X[:,2], c=color)

# 2D projection
figure()
scatter(Y[:,0], Y[:,1], c=color)

show()