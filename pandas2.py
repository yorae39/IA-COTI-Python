# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:39:01 2019

@author: Aluno 09
"""

import pandas as pd
import numpy as np

df = pd.DataFrame([
                   ["PE", "Pernambuco", "Recife"],
                   ["RJ", "Rio de Janeiro", "Rio de Janeiro"],
                   ["PB", "Paraiba", "João Pessoa"],
                   ["SP", "São Paulo", "São Paulo"],
                   ["MG", "Minas Gerais", "Belo Horizonte"],
                   ["CE", "Ceará", "Fortaleza"],
                   ], columns = ["Sigla", "Nome", "Capital"])

df

df.iloc[2]
df["Sigla"]


# DADOS DO DATA FRAME
df.index

df.ix[0]

# INCLUI O FINAL DO PARTICIONAMENTO
df.loc[:2]



# SUBSTITUIR O INDICE DO DF
df.index = df["Sigla"]
df


#REMOVER
del df["Sigla"]
df








