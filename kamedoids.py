"pip install  pyclustering"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster import cluster_visualizer
from sklearn import datasets


iris = datasets.load_iris()
iris


# NÃO PRECISA CONFIGURAR O NUMERO DE CLUSTER,
# ELE DESCOBRE SOZINHO INDICES ALEATÓRIOS A MEDOIDS
cluster = kmedoids(iris.data[:, 0:2], [3, 12, 20])
cluster

# medoids
cluster.get_medoids()


# efetuar o agrupamento
cluster.process()

# previsores
previsoes = cluster.get_clusters()

# 3 listas -> com elementos de cada grupo
len(previsoes)

# quantidade de elementos por grupo
for grupo in previsoes:
    print(len(grupo))
    
# Os elemsntos do gripo 0
print(previsoes[0])
    
    
# pegar medoids -> são usados como centro para classificação
# cluster

medoides = cluster.get_medoids()
medoides


v = cluster_visualizer()
v.append_clusters(previsoes, iris.data[:, 0:2])
v.append_cluster(medoides, iris.data[:, 0:2], marker= '*',
                 markersize=15)
v.show()








    
    
    
    