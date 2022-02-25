vetor = input().split()
A = int(vetor[0])
B = int(vetor[1])

if (A%B == 0) or (B%A == 0):
    print('Sao  Multiplos')
else:
    print('Nao sao Multiplos')