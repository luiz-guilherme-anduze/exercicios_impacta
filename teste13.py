import math

entradaA = input().split()
x1 = float(entradaA[0])
y1 = float(entradaA[1])

entradaB = input().split()
x2 = float(entradaB[0])
y2 = float(entradaB[1])

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f'{distancia:.4f}')

