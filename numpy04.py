# -*- coding: utf-8 -*-
"""
Created on Tue May  7 19:28:30 2019

@author: Aluno 09
"""

import numpy as np


array = np.arange(100000)
array

# ARRAYS MULTIDIMENSIONAIS
mat = np.array([[1,2], [3,4]])
mat


# rand
data = np.random.rand(2, 3)
data 
data.shape
data.ndim



# INSERINDO DADOS NO ARRAY
arr = np.array([1,2,3])
arr
print(arr)

# INSERT
arr2 = np.insert(arr, 1, 10)
arr2


a = np.array([[1,2,3], [4,5,6]])

a.sum()

a.sum(axis = 0)

a.sum(axis = 1)


np.insert(a, 1, 5, axis = 1)


#JUNTANDO ARRAYS
a1 = np.array([1,2,3])
np.append(a1, [4,5,6])

a = np.array([[1,2], [3,4]])
np.append(a, [[5,6]], axis = 0)

#TRANSPOSE
a.T


np.append(a.T, [[5,6]], axis = 0)

















































