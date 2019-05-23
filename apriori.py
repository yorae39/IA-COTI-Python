"APRIORI"
# pip install apyori

from apyori import apriori
import pandas as pd


dados = pd.read_csv('mercado2.csv', header = None)
print(dados)


transacoes = []

# CONVERTER
for i in range(len(dados)):
    transacoes.append([str(dados.values[i, j]) 
    for j in range(len(dados.columns))])
    
transacoes


len(transacoes)

transacoes[0]


regras = apriori(transacoes, min_support = 0.003, min_confidence = 0.2,
                 min_lift = 3, min_length = 2)

regras

resultado = list(regras)

print(len(resultado))



resultado2 = [list(x) for x in resultado]

resultadoFormatado = []

for j in range(0, 154):
    resultadoFormatado.append([list(x) for x in resultado2[j][2]])

resultadoFormatado

resultadoFormatado[0]


len(resultadoFormatado)

for r in resultadoFormatado:
    print(r)
    print("---------------------------")

















