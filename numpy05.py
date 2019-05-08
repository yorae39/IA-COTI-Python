# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:01:23 2019

@author: Aluno 09
"""

import numpy as np

a = np.array([[1,2], [3,4]])
a

np.repeat(a, 3)

np.repeat(a, 2, axis = 0)
np.repeat(a, 2, axis = 1)


#TILE
a = np.array([1,2,3])
np.tile(a, 2)


#DIVIDINDO UM ARRAY -> SPLIT
a = np.array([[1,2,3], [4,5,6]])
a

np.array_split(a, 2, axis = 0)


b = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
b



arrays = np.array_split(b, 4, axis = 0)
arrays


for array in arrays:
    print(array)


# ARRAYS DE ZEROS
np.zeros(4)
np.zeros((2,2))


np.ones(4)
np.ones((2,2))


np.ones((5,4))


# ARRAYS IDENTIDADE
d = np.eye(3)
d


# INDEXAÇÃO BOLEANA
a = np.array([[1,2], [3,4], [5,6]])
a


idx = (a > 2)
idx


#JUNÇÃO DE ARRAYS
a = np.array([[1,2], [3,4]])
b = np.array([[5,6]])

np.concatenate((a,b), axis = 0)


#SHUFFLE
a = np.arange(10)
a

np.random.shuffle(a)
a

# NUMEROS COMPLEXOS
a = np.array([1,10+2j, 20 + 5j], dtype = complex)
a


a[1]
a[1] + a[2]
a[1] - a[2]





































