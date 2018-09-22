#!/usr/bin/env python3.6
import random

def groupIn5(l):
    group = []
    for i in range(len(l)):
        if (i % 5) == 0: #devemos criar um novo grupo
            group.append([])
        group[i//5].append(l[i]) # i//5 da o indice

    print(group)
    return group


def linearMedian(l):
    l = groupIn5(l)
    medians = []
    for element in l:
        print(element)
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
        else:
            i = random.randint(1,2)
            if(i == 1):
                L.append(elemento)
            else:
                R.append(elemento)
    return L,R


def __linearSelectionRecusion(l,k):    
    m = linearMedian(l)
    L,R = getLR(l,m)
    if k == len(L) + 1: # elemento eh a mediana
        return m
    if k < len(L) + 1: # elemento esta a esquerda
        if(len(R)==1):
            return L
        return __linearSelectionRecusion(L,k)
    else: # esta na lista de maiores que a mediana
        #como a lista L e a mediana foram descartadas temos que compensar no k
        if(len(R)==1):
            return R
        return __linearSelectionRecusion(R , k - len(L) - 1)

def linearSelection(l,k):
    assert(k > 0)
    assert( type(l) == list)
    return __linearSelectionRecusion(l,k)

a = [7,4,1,2,3,5,6,89,20,22,22,22,22,22,22,22,14,12,25,11,32,33,44]
k = 13
e = linearSelection(a,k)
a.sort()
print("vetor:",a)
print(e , k)
