# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:13:06 2019

@author: Aluno 09
"""

import pandas as pd
import numpy as np


# SERIES -> DAODS EM UMA DIMENSÃO
s = pd.Series([1, 4, 5, 6, 7, 10, 6])
s

s[0]


s[2:4]


# DESCRIÇÃO DE SERIES
s.describe()
s.mean()
s.median()
s.duplicated()
s2 = pd.Series([11, 5, 8])

s.append(s2)

# CRIAR DATAFRAME
df = pd.DataFrame([        
        ["Python Web", 2000],
        ["Machine Learning", 3000],
        ["Lógica de programação", 4500]
        ], columns = ["curso",  "alunos"])

df
df["curso"]
df["alunos"]
df["alunos"].mean()

df["alunos"].median()


# ACESSAR O CONTEUDO
df.iloc[1]
df.iloc[1]["alunos"]




























