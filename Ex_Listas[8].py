"""Faça um Programa que peça a idade e a altura de 5 pessoas,
armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida."""

# Contador de pessoas para serem cadastradas:
c = 0

# Vetores:
nomes = []
alturas = []
idades = []


while True:

    nome = str(input("\nInforme seu nome » "))
    nomes.append(nome)  # Adicionando o nome na lista nomes.
    nome = nome.capitalize()

    altura = float(input(f"{nome} digite sua altura (em cm) » "))
    alturas.append(altura)  # Adicionando a altura na lista de alturas.

    idade = int(input(f"{nome} informe sua idade » "))
    idades.append(idade)

    c += 1
    print("\n←→←→←→←→←→→←→←→←→←→←←→←→←→←→←→←→←→←→→←→←→←→←→←←→←→←→")
    if c == 2:
        break
    else:
        continue

cc = 0
while cc != len(nomes):
    print(f"\n{nomes[cc].capitalize()} tem {idades[cc]} anos e mede {alturas[cc]} cm")
    cc += 1