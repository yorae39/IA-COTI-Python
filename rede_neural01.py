"AULA FINAL - 1"
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer
from pybrain.structure import BiasUnit
from pybrain.structure import SigmoidLayer
from pybrain.structure import FullConnection

# Retira o (2) do expm2 que retia o erro
# Criação da rede neural
rede = FeedForwardNetwork()


# Camada da entrada LinearLine
camadaEntrada = LinearLayer(2)


# Criação da camada oculta com 3 neuronios
camadaOculta = SigmoidLayer(3)


# Criação de saida com apenas um neuronio
camadaSaida = SigmoidLayer(1)


# Criação das unidades de Bias
bias1 = BiasUnit()
bias2 = BiasUnit()


# Construindo a rede neural
rede.addModule(camadaEntrada)
rede.addModule(camadaOculta)
rede.addModule(camadaSaida)
rede.addModule(bias1)
rede.addModule(bias2)



# Ligação entre entrada e camada oculta
# Fullconnection -> Ligação de um neuronio
# com todos as outras da outra camada
entradaOculta = FullConnection(camadaEntrada, camadaOculta)
ocultaSaida = FullConnection(camadaOculta, camadaSaida)
biasOculta = FullConnection(bias1, camadaOculta)
biasSaida = FullConnection(bias2, camadaSaida)


# Construir  rede neural
rede.sortModules()
print(rede)


# Pesos aleatorios gerados na camada de entrada
print(entradaOculta.params)


# Camada oculta para a camada de saida
print(ocultaSaida.params)


# bias camada oculta
print(biasOculta.params)
print(biasSaida.params)














