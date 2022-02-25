X = int(input())
Y = int(input())
x = 0
y = 0

if (X >= Y):
    lista = list(range(Y +1 , X))
    for item in lista:
        if (item%2 == 1):
            x = item + x
    print(x)
elif (X < Y):
    lista = list(range(X +1 , Y))
    for item in lista:
        if (item%2 == 1):
            y = item + y
    print(y)