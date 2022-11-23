from random import random
linhas = int(input('Quantas linhas a matriz tera?'))
colunas = int(input('Quantas colunas a matriz tera?'))


def separarParesEImpar(array):
    matrizPar = []
    matrizImpar = []
    novaMatrizFinal = []
    for i in array:
        if i % 2 == 0:
            matrizPar.append(i)
        else:
            matrizImpar.append(i)
        matrizPar.sort()
        matrizImpar.sort()
    novaMatrizFinal.extend(matrizPar)
    novaMatrizFinal.extend(matrizImpar)
    print(novaMatrizFinal)


def organizarMatriz(array):
    matrizFinal = []
    for item in array:
        matrizFinal.extend(item)
    separarParesEImpar(matrizFinal)


def checarValor(arrayDaMatriz, linha):
    array = arrayDaMatriz
    par = 0
    impar = 0
    valorPorcentagemPar = 0
    valorPorcentagemImpar = 0
    for i in array:
        if i % 2 == 0:
            par += 1
            valorPorcentagemPar = (round((par / len(array) * 100)))
        else:
            impar += 1
            valorPorcentagemImpar = (round((impar / len(array) * 100)))

    print('A linha %d tem %d%% de valores pares e %d%% de valores impares' %
          (linha, valorPorcentagemPar, valorPorcentagemImpar))


def gerarMatriz(linhas, colunas):
    matriz = []
    for a in range(linhas):
        matriz.append([])
    for y in range(colunas):
        for z in range(linhas):
            matriz[z].append(completarMatriz())
    for x in range(0, linhas):
        checarValor(matriz[x], x)
    for i in matriz:
        print(i)
    organizarMatriz(matriz)


def completarMatriz():
    valor1 = round(random() * 10)
    return valor1


gerarMatriz(linhas, colunas)
