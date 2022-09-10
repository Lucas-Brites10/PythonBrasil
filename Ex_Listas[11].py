'''Não será feito pois é muito simples'''


saque = int(input("Valor do saque: "))

valor = saque

ced_atual = 100 # levando em consideração 100 reais como a nota mais alta
qtd_ceds = 0

while True:
    #Enquanto tiver dinheiro vai fazer o seguinte:

    if valor >= ced_atual:

        valor -= ced_atual
        qtd_ceds += 1

    else:
        #Se não:
        #Caso não de mais para tirar do valor total o valor que a ced_atual esta atribuida a ced_atual deve receber um
        #valor menor:

        if qtd_ceds > 0:
            print(f"{qtd_ceds} de R$: {ced_atual}")


        if ced_atual == 100:

            ced_atual = 50
            #A ced_atual vai passar a valer 50 reais quando não for possivel retirar 100 reais do valor total

        elif ced_atual == 50:

            ced_atual = 20

        elif ced_atual == 20:

            ced_atual = 10

        elif ced_atual == 10:

            ced_atual = 5

        elif ced_atual == 5:

            ced_atual = 1

        qtd_ceds = 0

        if valor == 0:
            break