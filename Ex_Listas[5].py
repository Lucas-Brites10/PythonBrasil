from random import randrange
RED = "\033[1;31m"
BLUE = "\033[1;35m"

lista = []
for I in range(20):

    lista.append(randrange(0,100))

    if I in lista:
        lista.remove(I)
        lista.append(randrange(0,100))

def par(lista):
    par = []
    for P in range(len(lista)):

        if lista[P] % 2 == 0:

            par.append(lista[P])

    print(par, BLUE)
    return par

def impar(lista):

    impar = []

    for Im in range(len(lista)):
        if Im % 2 != 0:
            impar.append(Im)

        else:
            continue

    a = print(impar)
    a = BLUE
    return impar


par(lista)
impar(lista)
