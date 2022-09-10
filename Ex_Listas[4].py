from termcolor import colored

consoantes = ["a","e","i","o","u"]

word = input("Digite a palavra » ")
lst = []

RED = "\033[1;31m"
BLUE = "\033[1;34m"

for i in word:
    lst.append(i)
    if i not in consoantes:
        print(i, BLUE, end="")
    else:
        print(i, RED, end="")




