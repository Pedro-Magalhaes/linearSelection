﻿#!/usr/bin/env python3.6
import random
from heap import Heap
from random import randrange, uniform
import time
import argparse

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
    # Para tratar o problema de elementos repetidos:
    # se encontrar elementos repetidos, remove o primeiro deles
    # em seguida passa a inserir os elementos repetidos cada hora em uma das listas
    removed = False 
    left = True
    for elemento in l:
        if elemento < mediana:
            L.append(elemento)
        elif elemento > mediana:
            R.append(elemento)
        else:
            if removed == True:
                if(left == True):
                    L.append(elemento)
                    left = False
                else:
                    R.append(elemento)
            else:
                removed = True
    return L,R


def __linearSelectionRecursion(l,k):
    # Função que vai separando em grupos de 5 até achar a mediana
    m = linearMedian(l)
    # Função que separa L e R
    L,R = getLR(l,m)
    if k == len(L) + 1: # elemento eh a mediana
        return m
    if k < len(L) + 1: # elemento esta a esquerda
        return __linearSelectionRecursion(L,k)
    else: # esta na lista de maiores que a mediana
        #como a lista L e a mediana foram descartadas temos que compensar no k
        return __linearSelectionRecursion(R , k - len(L) - 1)

def linearSelection(l,k):
    if (k <= 0):
        print('Error: k must be > 0')
        exit(-1)
    if (k > len(l)):
        print('Error: k must be < than len(list)')
        exit(-1)
    assert( type(l) == list)
    return __linearSelectionRecursion(l,k)


def Testes ():
    # Teste para instâncias com 10 tamanhos diferentes
    for i in range (0,10):
        # Calculando k, sendo metade da lista arredondado para baixo
        k = (i + 1) * 1000 // 2
        somaLinear = 0
        somaSort = 0
        #criando 10 instâncias de cada tamanho
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
            vet = Heap.heap_sort(vet)
            m2  = vet[k-1]
            fim = time.time()
            somaSort += fim - inicio

        print("Para ",(i+1)*1000, " elementos: ")
        print("LINEAR SELECTION -> " +"Tempo: {:.2e}".format(somaLinear/10) + " Mediana: "+str(m))
        print(" SORT  SELECTION -> " +"Tempo: {:.2e}".format(somaSort/10) + " Mediana: "+str(m2))


#Testes()


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list', nargs='+',type=int,help="Lista de elementos em que devemos rodar o linear selection")
    parser.add_argument('--k', type=int, default=0,help="o Késimo menor elemento sera retornado, se não for informado será retornada a mediana ( len(l)//2 )")
    group.add_argument('-t', '--test',action='store_true',help="Rodar a bateria de testes propostos")
    args = parser.parse_args()
    if (args.test == True):
        Testes()
    else:
        l = args.list
        k = args.k or len(l)//2
        element = linearSelection(l,k)
        print("the {}th element is {}".format(k,element))
        return  element




main()

