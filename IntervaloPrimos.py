inicioInt = int(input())
fimInt = int(input())
num = inicioInt
multiplos = 0
p = 0

if(num == 1):
    num +=1

for numero in range(num, fimInt + 1):
    for n in range(2 , numero):
        if(numero%n == 0):
            multiplos += 1
    if(multiplos == 0):
        p += 1
        print(numero)
    multiplos = 0
print(f'primos: {p}')
