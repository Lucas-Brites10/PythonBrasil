'''Faça um Programa que leia um vetor A com 10 números inteiros,
 calcule e mostre a soma dos quadrados dos elementos do vetor'''
from random import randrange

vetor = []

for i in range(10):

    vetor.append(randrange(0, 100))

#CALCULADO A SOMA DOS QUADRADOS DOS ELEMENTOS DO VETOR:

#CALCULANDO O QUADRADO DE CADA ELEMENTO DO VETOR:

for J in range(len(vetor)):

    aux = vetor[J]
    vetor[J] = aux*aux

#SOMANDO CADA ELEMENTO

sum = 0

for S in vetor:

    sum+=S
    
print(sum)