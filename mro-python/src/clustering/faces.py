from milk import kmeans as milk_kmeans

__author__ = 'Magda'

from os import listdir
import scipy.misc
import numpy as np

from sklearn.cluster import KMeans, k_means

path = '../../yaleBfaces/zad1/'

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

def faces(n):
    faces, files = load_data()

    assignments = KMeans(n).fit_predict(faces)
    for x, filename in zip(assignments, files):
        print x
        # print filename, x

def faces_milk(n, metric):
    faces, files = load_data()

    assignments = milk_kmeans(faces, n, distance=metric, max_iter=300, return_assignments=True,
                             return_centroids=False)

    for x, filename in zip(assignments, files):
        print x
        # print filename, x

if __name__ == "__main__":
    n = 10

    #faces(n)
    faces_milk(n, 'euclidean')