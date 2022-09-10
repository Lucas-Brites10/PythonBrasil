'''Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser
compostos pelos elementos intercalados dos dois outros vetores.'''
from random import randrange

A = []
B = []

while len(A) + len(B) != 20:

    A.append(randrange(0, 1000))
    B.append(randrange(0, 1000))

C = []

for I in range(len(A)):

    a = C.append(A[I])
    b = C.append(B[I])

cor_a = "\033[33m"
cor_b = "\033[31m"

print(f"{cor_a}Lista A: {A}\n")
print(f"{cor_b}Lista B: {B}\n")

for n in range(len(C)):

    if n == 0:
        print(f"{C[n]}{cor_b}")
    if n % 2 != 0:
        print(f"{C[n]} {cor_a}")


    else:
        print(f"{C[n]} {cor_b}")

print(f"Lista C: {C}")

