controle = 0

while (controle == 0):
    n = int(input())
    if (n > 5) & (n < 2000):
        controle = 1

lista  = list(range(2 , n+1))

for item in lista:
    if(item%2 == 0):
        itemQuadrado = item ** 2
        print(f'{item}^2 = {itemQuadrado}')

    