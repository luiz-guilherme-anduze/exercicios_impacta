notas = input().split()
p1, p2, p3, p4 = float(notas[0]), float(notas[1]), float(notas[2]), float(notas[3])

media =  (2 * p1 + 3 * p2 + 4 * p3 + p4)/10

if(media >= 7.0):
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
elif(media >= 5.0) & (media <= 6.9):
    exame = float(input())
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    print(f'Nota do exame: {exame:.1f}')
    notaFinal = (media + exame)/2
    if (notaFinal >= 5.0):
        print('Aluno aprovado.')
    elif(notaFinal < 5.0):
        print('Aluno reprovado.')
    print(f'Media final: {notaFinal:.1f}')
elif(media < 5.0):
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')

