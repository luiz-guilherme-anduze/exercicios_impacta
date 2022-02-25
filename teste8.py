mercadoria = float(input())
n = int(input())
i =1
desconto = 0.90

totalSdesconto = mercadoria * n

if(n==1):
    print(f'{totalSdesconto:.2f}')
    totalCdesconto = totalSdesconto * 0.89
    print(f'{totalCdesconto:.2f}')
elif(n>1):    
    while((n+1)!=i):
        desconto = desconto - 0.01
        if(n==i):
            totalCdesconto = totalSdesconto * desconto
            print(f'{totalSdesconto:.2f}')
            print(f'{totalCdesconto:.2f}')
        i += 1
        

