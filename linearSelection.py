#!/usr/bin/env python3.6

from random import randrange, uniform
import time

def groupIn5(l):
    group = []
    for i in range(len(l)):
        if (i % 5) == 0: #devemos criar um novo grupo
            group.append([])
        group[i//5].append(l[i]) # i//5 da o indice
    return group


def linearMedian(l):
    l = groupIn5(l)
    medians = []
    for element in l:
        element.sort()
        medians.append(element[ len(element)//2 ]) #append no elemento do meio (o ultimo vetor pode ter menos de 5 elem)
    if len(medians) == 1: #achamos a mediana
        return medians[0]
    return linearMedian(medians)


def getLR(l,mediana):
    L=[]
    R=[]
    for elemento in l:
        if elemento < mediana:
            L.append(elemento)
        elif elemento > mediana:
            R.append(elemento)
    return L,R


def __linearSelectionRecusion(l,k):
    # Função que vai separando em grupos de 5 até achar a mediana
    m = linearMedian(l)
    # Função que separa L e R
    L,R = getLR(l,m)
    if k == len(L) + 1: # elemento eh a mediana
        return m
    if k < len(L) + 1: # elemento esta a esquerda
        return __linearSelectionRecusion(L,k)
    else: # esta na lista de maiores que a mediana
        #como a lista L e a mediana foram descartadas temos que compensar no k
        return __linearSelectionRecusion(R , k - len(L) - 1)

def linearSelection(l,k):
    assert(k > 0)
    assert( type(l) == list)
    return __linearSelectionRecusion(l,k)

def Testes ():
    # Teste para 10 instâncias diferentes
    for i in range (0,10):
        # Calculando k, sendo metade da lista arredondado para baixo
        k = (i + 1) * 1000 // 2
        somaLinear = 0
        somaSort = 0
        for u in range(0,10):
            vet = []
            # Cada instância vai ter quantidade de elementos diferentes (1000,2000.....10000)
            for j in range (0,(i+1)*1000):
                vet.append(uniform(1, 100000))  # faixa de ponto flutuante


            #Calculando tempo de execução do LinearSelection
            inicio = time.time()
            m = linearSelection(vet, k)
            fim = time.time()
            somaLinear += fim - inicio

            # Calculando tempo de execução do SortSelection
            inicio = time.time()
            vet.sort()
            m2  = vet[k-1]
            fim = time.time()
            somaSort += fim - inicio

        print("Tempo médio total do algoritmo Linear Selection para ",(i+1)*1000, " elementos: ")
        print("{:.2e}".format(somaLinear/10))
        print("Tempo médio total do algoritmo Sort Selection para ",(i+1)*1000, " elementos: ")
        print("{:.2e}".format(somaSort/10))


#a = [7,4,1,2,3,5,6,89,20,22,14,12,25,11,32,33,44]
#k = 4
#e = linearSelection(a,k)
#a.sort()
#print("vetor:",a)
#print(e , k)
Testes()
#Teste
