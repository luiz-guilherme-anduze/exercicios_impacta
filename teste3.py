from decimal import Decimal

Ai = Decimal(input())
Bi = Decimal(input())
A = round(Ai, 1)
B = round(Bi,1)
MEDIAi = (Decimal(3.5)*A+Decimal(7.5)*B)/2
MEDIA =round(MEDIAi,5)
print("MEDIA = "+str(MEDIA))