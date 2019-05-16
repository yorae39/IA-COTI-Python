# -*- coding: utf-8 -*-
"""
Created on Thu May  9 19:03:40 2019

@author: Aluno 09
"""

# pip install pydataset - ANACONDA PROMPT

import pydataset 
import pandas as pd 


pydataset.data()["title"]

type(pydataset.data())


titanic = pydataset.data("titanic")
titanic

titanic.head()

titanic.tail(10)

titanic.describe()


titanic['class'].value_counts()


len(pydataset.data())


























