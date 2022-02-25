n = 0.0
vicSoma = 0.0

while(n != -1.0):
    vicCoin = float(input())
    if (vicCoin != -1.0):
        vicSoma += vicCoin
    else:
        n = -1.0

reais = vicSoma * 2.5

print(f'VC$ {vicSoma:.2f}')
print(f'R$ {reais:.2f}')
