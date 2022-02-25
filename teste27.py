controle = 0
n = 1

while(controle == 0):
    if(n > 0) & (n<13):
        n = int(input())
        controle = 1

lista = list(range(1 , n+1))

multiplicacao = 1

for item in lista:
    multiplicacao = item * multiplicacao

print(multiplicacao)