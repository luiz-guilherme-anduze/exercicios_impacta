n = 0
i = 1
m = 0

while(n >= 0):
    n = int(input())
    if n >= 0:
        m = (n + m)
        i = i + 1


tamanhoLista = len(range(1 , i))

media = m/tamanhoLista

print(f'{media:.2f}')