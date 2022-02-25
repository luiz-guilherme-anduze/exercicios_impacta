testeN = int(input())

membros = ['Rolien', 'Naej', 'Elehcim', 'Odranoel']
nMembro = 0
testeK = 0
resultado = []

for i in range(testeN):
    testeK = int(input())
    for j in range (testeK):
        nMembro = int(input())
        if nMembro == 1:
            resultado.append('Rolien')
        elif nMembro == 2:
            resultado.append('Naej')
        elif nMembro == 3:
            resultado.append('Elehcim')
        elif nMembro == 4:
            resultado.append('Odranoel')
    print(resultado)

