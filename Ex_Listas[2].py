
lista = [1,2,3,4,5]

for I in range(len(lista)):

    for J in range(len(lista)-1):

        if lista[J] < lista[J+1]:

            lista[J], lista[J+1] = lista[J+1], lista[J]


print(lista)
