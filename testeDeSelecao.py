entrada = input().split()

A = int(entrada[0])
B = int(entrada[1])
C = int(entrada[2])
D = int(entrada[3])

X = B > C
Y = D > A
Z = C + D > A + B
W = C > 0
XX = D > 0
YY = A % 2 == 0


if X and Y and Z and W and XX and YY:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')