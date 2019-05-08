# -*- coding: utf-8 -*-
"""
AULA 01 DE PYTHON - 07/05/2019
"""

# IMPORT numpy
# numeric array

import numpy

a = numpy.array([10, 20, 30, 50])
a

type(a)

print(a)



mat = numpy.array([[1,2], [3,4]])
mat
print(mat)


# ACESSANDO A POSIÇÃO
print(mat[1, 1])

print(mat[-1, -1])


print(mat.transpose())


m1 = numpy.array(numpy.array([[1,2], [3,4]]))
m2 = numpy.array(numpy.array([[5,6], [7,8]]))


m1
m2

#OPERAÇÕES
print(m1 + m2)
print(m1 - m2)


#FUNÇÕES
m3 = numpy.array([1,2,3,4])
m3


# argmax -> INDICE DO MAIOR ELEMENTO
p = m3.argmax()
m3[p]



p = m3.argmin()
print(p)
print(m3[p])
















































