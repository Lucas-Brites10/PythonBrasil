notas = []
for I in range(0, 4):

    n = float(input(f"Digite a {I+1} nota » "))
    notas.append(n)

def media_notas(notas):

    t = 0
    for I in range(len(notas)):
        t += notas[I]

    media = t/len(notas)

    return media

print(media_notas(notas))