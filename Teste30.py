#número de dados entrados
i=0
while(i == 0):
    n = int(input())
    if(n>=1) and (n<=10):
        i = 1

#entrada de dados
j=0
dados = []
curso = []
while (j != n):
    registro = int(dados[2*j])
    curso = str(dados[2*j+1])
    j += 1
intrusos = 0
epr = 0
ehd = 0

#processamento
k = 0
while(k != n):
    if (curso[k] != 'EPR') and (curso[k] != 'EHD'):
        intrusos += 1
    elif (curso[k] == 'EPR'):
        epr += 1
    elif (curso[k] == 'EHD'):
        ehd += 1
    k += 1

#impressão
print('EPR:', str(epr))
print('EHD:', str(ehd))
print('INTRUSOS:',str(intrusos))