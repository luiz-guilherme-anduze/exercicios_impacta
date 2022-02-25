def verificaNegativoOuZero(vet):
    for i in range(10):
        if vet[i] <= 0:
            vet[i] = 1
    return vet

def pegaVetor():
    vet = []
    for i in range(10):
        vet.append(int(input()))

    return vet

def imprimeVetor(vet):
    for i in range(10):
        print(f'X[{i}] = {vet[i]}')

x = pegaVetor()
vetor = verificaNegativoOuZero(x)
imprimeVetor(vetor)    