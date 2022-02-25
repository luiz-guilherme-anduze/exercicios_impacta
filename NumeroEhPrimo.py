numero = int(input())

numeros = list(range(1,numero+1))
multiplos = 0
n =[]

for k in numeros:
    n.append(int(input()))

for i in numeros:
    for j in range(2,n[i-1]):
        if n[i-1] % j == 0:
            multiplos += 1
    if multiplos == 0:
        print(f'{n[i-1]} eh primo')
    else:
        print(f'{n[i-1]} nao eh primo')
    multiplos = 0
