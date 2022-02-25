x = 2
n = 0
while x == 2:
    if(x >= 1) and (x <= 20):
        n = int(input())
        x = 1

nPerfeito = 0
lista = []
acumPerfeito = 0

for i in range(n):
    nPerfeito = int(input())
    lista = list(range(1,nPerfeito))
    for i in lista:
        if nPerfeito%lista[i-1] == 0:
            acumPerfeito += lista[i-1]
    if acumPerfeito == nPerfeito:
        print(str(nPerfeito) +' eh perfeito')
    else:
        print(str(nPerfeito) +' nao eh perfeito')
    acumPerfeito = 0


