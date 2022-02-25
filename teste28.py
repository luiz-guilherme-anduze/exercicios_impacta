lista = list(range(1 , 101))
entrada = 0
maior = 0
posicao = 0

for item in lista:
    entrada = int(input())
    if(entrada >= maior):
        maior = entrada
        posicao = item

print(maior)
print(posicao)
