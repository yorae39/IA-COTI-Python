import numpy as np
import math


# FUNÇÃO LOAD NOS DADOS
amostras = []

with open('dataset.data', 'r') as f:
    for linha in f.readlines():
        atrib = linha.replace('\n', '').split(',')
        amostras.append([ int(atrib[0]), 
                          int(atrib[1]),
                          int(atrib[2]), 
                          int(atrib[3]) ])
    
print(amostras[:5])    
print(len(amostras))


# INFO DATASET - INFORMAÇOES DOBRE O DATASET
def info_dataset(amostras, verbose = True):
    if verbose:
        print('Total de amostras : %d ' % len(amostras))
    rotulo1, rotulo2 = 0, 0
    for amostra in amostras:
        if amostra[-1] == 1:
            rotulo1 += 1
        else:
             rotulo2 += 1
    if verbose:
        print('Exemplos de rotulo1 : %d' % rotulo1)
        print('Exemplos de rotulo2 : %d' % rotulo2)
    return [len(amostras), rotulo1, rotulo2]

info_dataset(amostras)


# PORCENTAGEM -> CONJUTNO DE TREINAMENTO
p = 0.7 # -> treinamento

_, rotulo1, rotulo2 = info_dataset(amostras, False)

print(rotulo1)
print(rotulo2)


# MAXIMO DE INSTANCIAS DOS ROTULOS

max_rotulo1, max_rotulo2 = int(p * rotulo1), int(p * rotulo2)

print(max_rotulo1)
print(max_rotulo2)


# CRIAÇÃO DA FUNÇÃO SAMPLE
# SEPARAÇÃO DE TREINAMENTO E TESTE 

treinamento, teste = [], []

def sample(max_r1, max_r2, treinamneto, teste, amostras):
    # NUMERO MAXIMO DE AMOSTRAS 
    t_r1, t_r2 = 0, 0
    for amostra in amostras:
        if(t_r1 + t_r2) < (max_r1 + max_r2):
            treinamento.append(amostra)
            if amostra[-1] == 1 and t_r1 < max_r1:
                t_r1 += 1
            else:
                t_r2 += 1
        else:
            teste.append(amostra)

sample(max_rotulo1, max_rotulo2, treinamento, teste, amostras)


info_dataset(treinamento)
info_dataset(teste)



import knn

from knn import dist_euclidiana_np

def knn2(treinamento, nova_amostra, k):
    # calcular a distanacia
    dists, tam_treino = {}, len(treinamento)
    for i in range(tam_treino):
        d = dist_euclidiana_np(treinamento[i], nova_amostra)
        dists[i] = d
        return dists
        pass


distancias = knn2(treinamento, teste[0], 0)


sorted(distancias, key=distancias.get)[:5]


def knn2(treinamento, nova_amostra, k):
    # calcular a distancia
    dists, tam_treino = {}, len(treinamento)
    for i in range(tam_treino):
        d = dist_euclidiana_np(treinamento[i], nova_amostra)
        dists[i] = d
        k_vizinhos = sorted(dists, key = dists.get)[:k]
        qtd_rotulo1, qtd_rotulo2 = 0, 0
        
        for indice in k_vizinhos:
            if treinamento[indice][-1] == 1:
                qtd_rotulo1  += 1
            else:
                qtd_rotulo2 += 1
        if qtd_rotulo1 > qtd_rotulo2:
            return 1
        else:
            return 2
        pass



# FUNÇÃO PARA ENCONTRAR O NUMERO DE VIZINHOS
def k_n_vizinhos(treinamento):
    n = len(treinamento)
    k = int(math.sqrt(n))
    if k % 2 == 0:
        return k + 1
    else:
        return k


k = k_n_vizinhos(treinamento)



# TREINAMENTO
def train(treinamento, teste, k):
    acertos = 0
    for amostra in teste:
        classe = knn(treinamento, amostra, k)
        if amostra[-1] == classe:
            acertos += 1
    return acertos           
    pass


acertos = train(treinamento, teste, k)
print('Total de treinamento : %d' % len(treinamento))
print('Total de teste : %d' % len(teste ))
print ('Total de acertos : %d ' % acertos)
print('Porcentagem de acertos : %0.2f %%' % (100 * acertos / len(teste)))















