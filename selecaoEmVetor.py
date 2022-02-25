def pegaVetor():
    vetor = []
    for i in range(10):
        n = float(input())
        vetor.append(n)
    return vetor

def imprimeVetor(vetor):
    for i in range(10):
        if vetor[i] <= 10.0:
            print(f'A[{i}] = {vetor[i]:.1f}')

vetor = pegaVetor()
imprimeVetor(vetor)