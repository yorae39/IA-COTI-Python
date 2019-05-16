# -*- coding: utf-8 -*-
"""
Created on Thu May  9 19:22:24 2019

@author: Aluno 09
"""

import pandas as pd

help(pd.read_csv)

# LENDO UM XLS
populacao = pd.read_excel("total-populacao-pernambuco.xls")
populacao


populacao.head()
populacao.shape


# pd.set_option("display.max_rows", 200)
# pd.set_option("display.max_columns", 10)
# pd.set_option("display.width", 500)
# pd.set_option("display.height", 500)


populacao["Total de mulheres"] / populacao["Total de homens"]


populacao["Total de mulheres"].sum() / populacao["Total de homens"].sum()






