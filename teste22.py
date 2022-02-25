entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

if(a > b) & (a > c):
    print(f'{a} eh o maior')
elif(b > a) & (b > c):
    print(f'{b} eh o maior')
elif(c > a) & (c > b):
    print(f'{c} eh o maior')
