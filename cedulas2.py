dinheiro = float(input())

notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0

print(f'{dinheiro:.0f}')
if dinheiro >= 100.0:
    notas100 = dinheiro // 100
    dinheiro = dinheiro % 100
print(f'{notas100:.0f} nota(s) de R$ 100,00')
if dinheiro >= 50.0:
    notas50 = dinheiro // 50
    dinheiro = dinheiro % 50
print(f'{notas50:.0f} nota(s) de R$ 50,00')
if dinheiro >= 20.0:
    notas20 = dinheiro // 20
    dinheiro = dinheiro % 20
print(f'{notas20:.0f} nota(s) de R$ 20,00')
if dinheiro >= 10.0:
    notas10 = dinheiro //10
    dinheiro = dinheiro % 10
print(f'{notas10:.0f} nota(s) de R$ 10,00')
if dinheiro >= 5.0:
    notas5 = dinheiro // 5
    dinheiro = dinheiro % 5
print(f'{notas5:.0f} nota(s) de R$ 5,00')
if dinheiro >= 2.0:
    notas2 = dinheiro // 2
    dinheiro = dinheiro % 2
print(f'{notas2:.0f} nota(s) de R$ 2,00')
if dinheiro >= 1.0:
    notas1 = dinheiro // 1
print(f'{notas1:.0f} nota(s) de R$ 1,00')
