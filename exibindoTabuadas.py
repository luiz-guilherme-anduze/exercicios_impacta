t1 = int(input())
t2 = int(input())

if(t1<=t2):
    for j in range(t1, t2+1):
        for i in range(10):
            tabuada = j * (i+1)
            print(j,'x',i+1,'=', tabuada)
        print('----------')
else:
    print('Nenhuma tabuada no intervalo!')