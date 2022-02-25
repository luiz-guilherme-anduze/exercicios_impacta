entrada = input().split()
A, B, C = float(entrada[0]), float(entrada[1]), float(entrada[2])

areaTriangulo = (A * C)/2
areaCirculo = 3.14159 * C**2
areaTrapezio = (A+B)*0.5*C
areaQuadrado = B**2
areaRetangulo = A * B

print(f'TRIANGULO:{areaTriangulo:.3f}')
print(f'CIRCULO:{areaCirculo:.3f}')
print(f'TRAPEZIO:{areaTrapezio:.3f}')
print(f'QUADRADO:{areaQuadrado:.3f}')
print(f'RETANGULO:{areaRetangulo:.3f}')