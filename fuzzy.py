"INSTALAR O PACOTE SCIKIT-FUZZY"
# pip install scikit-fuzzy

from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score
import skfuzzy



iris = datasets.load_iris()
iris


# TRANSPOR A MATRIZ -> T, TRANSFORMAR LINHA EM COLUNA
# AGRUPAMENTO PARCIAL DIFUSÃO
# UM ELEMENTO PODE PARTICIPAR A MAIS DE UM GRUPO
# DATA             -> CONJUNTO DE DADOS QUE SERÁ ANALISADO
# ERROR            -> 0.005, VALOR MINIMO DA ERROR
# MAXITTER         -> NUMERO MAXIMO DE ITERAÇÕES
r = skfuzzy.cmeans(data = iris.data.T, c = 3, m = 2,
                   error = 0.005, maxiter= 1000,
                   init= None)

# r -> RETORNA UMA TUPLA COM 7 POSIÇÕES
previsoes_porcentagem = r[1]


# PROBABILIDADE DA PRIMEIRO REGISTRO ESTA
# EM UMA DOS 3 CLASSES
print(previsoes_porcentagem[0][1])
print(previsoes_porcentagem[1][1])
print(previsoes_porcentagem[2][1])



previsoes = previsoes_porcentagem.argmax(axis = 0)
confusao = confusion_matrix(previsoes, iris.target)
confusao
























