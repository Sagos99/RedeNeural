import numpy as np


def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1 - sig)

entradas = np.array([[0,0],
                     [0,1],
                     [1,0],
                     [1,1]])

saidas = np.array([[0], [1], [1], [0]])

pesos0 = 2 * np.random.random((2,3))-1
pesos1 = 2 * np.random.random((3,1))-1

epocas = 15000
taxaAprendizagem = 0.3
momento = 1
tentativas = 0

for j in range(epocas):

# mediaAbsoluta = 0.80
# while mediaAbsoluta > 0.02:

    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    camadaOculta = sigmoid(somaSinapse0)

    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1)

    erroCamadaSaida = saidas - camadaSaida # calcula o erro
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
    print('Erro: '+str(mediaAbsoluta))

    derivadaSaida = sigmoidDerivada(camadaSaida)
    deltaSaida = erroCamadaSaida * derivadaSaida

    pesos1Transposta = pesos1.T
    deltaSaidaXPeso = deltaSaida.dot(pesos1Transposta)
    deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)

    camadaOcultaTransposta = camadaOculta.T
    pesosNovos1 = camadaOcultaTransposta.dot(deltaSaida)
    pesos1 = (pesos1 * momento) + (pesosNovos1 * taxaAprendizagem)

    camadaEntradaTransposta = camadaEntrada.T
    pesosNovos0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    pesos0 = (pesos0 * momento) + (pesosNovos0 * taxaAprendizagem)
    tentativas += 1


resultado = np.around(camadaSaida).astype(int)

print('\nPesos0: \n'+str(pesos0))
print('Pesos1: \n'+str(pesos1))

print('\nTentativas: '+str(tentativas))
print('Resultado: '+str(resultado))
