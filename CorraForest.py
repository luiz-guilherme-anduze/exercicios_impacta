n = 1
media = 0
tempo = []
while(n>=0):
    n = int(input())
    if n>=0:
        media = media + n
        tempo.append(n)               
    else:
        break
media = media / len(tempo)
print(f'MEDIA: {media:.2f}')
for k in tempo:
    if k < media:
        print(k)    