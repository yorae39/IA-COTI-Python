# -*- coding: utf-8 -*-
"""
Created on Tue May  7 19:00:32 2019

@author: Aluno 09
"""

import numpy as np

array = np.arange(100000)
array


lista = list(range(100000))

#CALCULA O TEMPO DE PROCESSAMENTO
%time for _ in range(10) : array = array * 2

%time for _ in range(10) : lista = [x * 2 for x in lista]


#ARRAY MULTI DIMENSIONAL
data = np.random.rand(2, 3)
print(data)

data * 10
data + data
data.shape
data.dtype
































