entrada = input().split()
codPeca1, numPeca1, valorPeca1 = int(entrada[0]), int(entrada[1]), float(entrada[2])

entrada1 =input().split()
codPeca2, numPeca2, valorPeca2 = int(entrada1[0]), int(entrada1[1]), float(entrada1[2])

total = (numPeca1 * valorPeca1)  + (numPeca2 * valorPeca2)

print(f'VALOR A PAGAR: R$ {total:.2f}')