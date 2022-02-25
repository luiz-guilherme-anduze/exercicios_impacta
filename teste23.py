xi = 0

while(xi == 0):
    x = int(input())
    if (x >=1) & (x <= 1000):
        xi =1

lista = list(range(1, x+1))


for item in lista:
    if (item%2 == 1):
        print(item)

