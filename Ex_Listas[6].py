A1 = []
A2 = []
A3 = []
A4 = []
A5 = []

for I in range(1):
    R = False
    for UM in range(4):
        if len(A1) == 0:
            print("\033[35m" + "Aluno 1")
        else:
            pass
        cor = "\033[33m"
        nota = float(input(f"{cor}" + f"Digite a {UM + 1} nota » "))
        A1.append(nota)

    for DOIS in range(4):
        if len(A2) == 0:
            print("\033[35m" + "Aluno 2")
        else:
            pass
        cor = "\033[33m"
        nota = float(input(f"{cor}" + f"Digite a {DOIS + 1} nota » "))
        A2.append(nota)

    for TRES in range(4):
        if len(A3) == 0:
            print("\033[35m" + "Aluno 3")
        else:
            pass
        cor = "\033[33m"
        nota = float(input(f"{cor}" + f"Digite a {TRES + 1} nota » "))

        A3.append(nota)

    for QUATRO in range(4):
        if len(A4) == 0:
            print("\033[35m" + "Aluno 4")
        else:
            pass
        cor = "\033[33m"
        nota = float(input(f"{cor}" + f"Digite a {QUATRO + 1} nota » "))

        A4.append(nota)

    for CINCO in range(4):
        if len(A5) == 0:
            print("\033[35m" + "Aluno 5")
        else:
            pass
        cor = "\033[33m"
        nota = float(input(f"{cor}" + f"Digite a {CINCO + 1} nota » "))

        A5.append(nota)

    if len(A5) == 4:
        R = True

    break


def media(aluno):

    media = 0
    for cal in aluno:
        media+= cal

    return media/len(aluno)

print("\n\n")


#MOSTRANDO AS MÉDIAS:

M_A1 = media(A1)
M_A2 = media(A2)
M_A3 = media(A3)
M_A4 = media(A4)
M_A5 = media(A5)

REPROVADOS = 0
APROVADOS = 0

REP = False
APR = False

if REP == True:
    cor = "\033[31m"

if APR == True:
    cor = "\033[33m"

if M_A1 < 5:
    REP = True
    APR = False
    REPROVADOS+=1

    print(f"A média do ALUNO 1 foi de {cor}{M_A1}")
else:
    APR = True
    REP = False
    APROVADOS+=1

    print(f"A média do ALUNO 1 foi de {cor}{M_A1} ")

