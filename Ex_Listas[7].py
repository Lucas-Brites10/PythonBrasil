"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números."""
from random import randrange
#Criando um vetor com 5 numeros
vetor = []

while len(vetor) != 5:

    numero = randrange(0, 10)
    aux = numero
    vetor.append(numero)

    if len(vetor) > 0:
        if numero not in vetor:
            vetor.appen



    #verificando repetições


print(vetor)
