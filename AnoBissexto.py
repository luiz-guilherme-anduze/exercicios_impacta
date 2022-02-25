inicio = int(input())
fim = int(input())
contador = 0
n = inicio
intervalo = (fim+1) - inicio

while(n != (fim+1)):
    divisivelPor4 = n%4 == 0
    naoDivisivelpor100 = n%100 != 0
    divisivelPor400 = n%400 == 0
    if((divisivelPor4) and (naoDivisivelpor100)) or (divisivelPor400):
        print(n)
        contador += 1
    n += 1

print(f'bissextos: {contador}')