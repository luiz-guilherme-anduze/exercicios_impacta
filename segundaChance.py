n = int(input())
provaAlunos = []
trabalhoAlunos = []

for i in range(n):
    prova = float(input())
    provaAlunos.append(prova)

for j in range(n):
    trabalho = float(input())
    trabalhoAlunos.append(trabalho)

mediaFinal = []
alteradas = 0
medias = 0.0

for k in range(n):
    if trabalhoAlunos[k] == 10.0:
        medias = provaAlunos[k] + (0.2 * trabalhoAlunos[k])
        if medias > 10.0:
            medias = 10.0
        mediaFinal.append(medias)
        alteradas += 1
        if provaAlunos[k] == 10.0:
            alteradas -= 1
    elif trabalhoAlunos[k] < 10.0:
        mediaFinal.append(provaAlunos[k])

print(f'NOTAS ALTERADAS: {alteradas}')

for z in range(0,n):
    if provaAlunos[z] != mediaFinal[z]:
        print(f'*({z+1:03}) original: {provaAlunos[z]:0>5.2f} | final: {mediaFinal[z]:0>5.2f}')
    elif provaAlunos[z] == mediaFinal[z]:
        print(f'-({z+1:03}) original: {provaAlunos[z]:0>5.2f} | final: {mediaFinal[z]:0>5.2f}')