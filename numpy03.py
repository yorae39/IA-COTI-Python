# -*- coding: utf-8 -*-
"""
Created on Tue May  7 19:16:49 2019

@author: Aluno 09
"""

import numpy as np

l = [10, 20, 30, 40, 50]
a = np.array(l)
print(a)

#COPIAS
b = a[:]
b


b[0] = 20000
a 

#COPIA REAL
c = a.copy()
c[0] = 10
print(c)

a





















