# -*- coding: utf-8 -*-
"""
Created on Thu May  9 19:52:54 2019

@author: Aluno 09
"""

#  INSTALAR A BIBLIOTECA db.py
# pip install db.py

from db import DB


# CARREGANDO OS DADOS DO SQLITE PARA PYTHON
database = DB(filename = "logs.sqlite3", dbtype = "sqlite")

database.tables

# CARREGANDO TABELA
log_df = database.tables.log
log_df



log_df = database.tables.log.all()
log_df


log_df = database.query("select * from log where user_id = 3")
log_df


























