def preencheVetor(n):
    vetor = []
    for i in range(10):
        valorV = (2**i)*n
        vetor.append(valorV)
    
    return vetor

def imprimeVetor(vetor):
    for i in range(10):
        print(f'N[{i}] = {vetor[i]}')

n = int(input())
vetor = preencheVetor(n)
imprimeVetor(vetor)