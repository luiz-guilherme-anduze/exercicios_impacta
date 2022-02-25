v = []
for i in range(20):
    entrada = input()
    v.append(entrada)

for i in range(0,10):
    troca = v[i]
    v[i]=v[19-i]
    v[19-i]= troca

for i in range(0,20):
    print(f'N[{i}] = {v[i]}')


