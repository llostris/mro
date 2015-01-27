__author__ = 'Magdalena Strzoda'

import networkx as nx
import scipy.cluster.hierarchy as hierarchy
import matplotlib.pyplot as pyplot
import sklearn.cluster.spectral as spectral
import numpy as np
import random

IMG_DIR = 'img/'

def random_walk(start, end, G):
    walked = 0
    current = start

    while current != end :
        walked += 1
        neighbors = G.neighbors(current)
        current = neighbors[random.randint(0, len(neighbors) - 1)]

    return walked


def commute_time(start, end, G):
    return random_walk(start, end, G) + random_walk(end, start, G)


def commute_time_matrix(G, adj_matrix):
    matrix = np.zeros(adj_matrix.shape)

    for node1 in range(adj_matrix.shape[0]):
        for node2 in range(adj_matrix.shape[1]):
            matrix[node1][node2] = commute_time(node1, node2, G)

    return matrix


def perform_clustering(filepath, method, metric, cutoff, dataset_name=None):
    path = IMG_DIR + dataset_name + '-' + metric + '-' + method
    ext = '.png'

    G = nx.read_gml(filepath)

    if dataset_name == 'karate':
        G = nx.convert_node_labels_to_integers(G, first_label=0)

    if metric == 'euclidean' or metric == 'correlation':
        adj_matrix = nx.adjacency_matrix(G)
        distance_matrix = adj_matrix.todense()
        linkage_matrix = hierarchy.linkage(distance_matrix, method=method, metric=metric)
    elif metric == 'shortest-paths':
        distance_matrix = nx.floyd_warshall_numpy(G)
        linkage_matrix = hierarchy.linkage(distance_matrix, method=method)
    elif metric == 'commute-time':
        adj_matrix = nx.adjacency_matrix(G)
        distance_matrix = commute_time_matrix(G, adj_matrix)
        linkage_matrix = hierarchy.linkage(distance_matrix, method=method)
    else:
        print "invalid metric"
        return

    pyplot.subplot(1, 1, 1)
    hierarchy.dendrogram(linkage_matrix)
    # pyplot.show()
    pyplot.savefig(path + ext)

    clustering = hierarchy.fcluster(linkage_matrix, cutoff)
    draw_graph(G, clustering, path + '-graph' + ext)


def spectral_partition(dataset, filename):
    G = nx.read_gml(dataset)
    adj_matrix = nx.adjacency_matrix(G)
    distance_matrix = adj_matrix.todense()
    res = spectral.spectral_clustering(distance_matrix)
    # print res, len(res)
    draw_graph(G, res, filename)


def draw_graph(G, membership, filename=None):
    partition = { i : [] for i in range(max(membership) + 1) }
    for n,p in zip(list(range(len(G))),membership):
        partition[p].append(n)
    clustering = list(partition.values())
    # print clustering

    BM = nx.blockmodel(G, clustering)
    # print BM.number_of_nodes(), G.number_of_nodes()

    pyplot.clf()
    posBM = nx.spring_layout(BM)
    nx.draw(BM, posBM, with_labels=True)
    # pyplot.show()
    if filename:
        pyplot.savefig(filename)


if __name__ == "__main__":
    # dataset_name = [ 'dolphins', 'karate', 'football' ]
    dataset_name = 'football'

    method = [ 'single', 'average', 'complete' ]
    metric = [ 'euclidean', 'correlation', 'shortest-paths', 'commute-time' ]
    dataset = '../../hierarchical/' + dataset_name +'.gml'

    perform_clustering(dataset, 'complete', 'commute-time', 1.0, dataset_name=dataset_name)
    spectral_partition(dataset, dataset_name +'-spectral.png')

