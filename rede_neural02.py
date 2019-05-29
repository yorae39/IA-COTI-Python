"AULA FINAL - 2"

from sklearn.neural_network import MLPClassifier
from sklearn import datasets


iris = datasets.load_iris()


entrada = iris.data


saidas = iris.target



redeNeural = MLPClassifier(verbose= True, max_iter=1000, 
                           tol=0.00001,
                           learning_rate_init=0.01,
                           activation='logistic')


redeNeural.fit(entrada, saidas)


# Predição
redeNeural.predict([entrada[120]])

# Nomes das classes
iris.target_names

redeNeural.predict([[5,6.3,3,4]])


iris.target[120]
