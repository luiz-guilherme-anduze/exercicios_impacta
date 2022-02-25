notaTrabalho = float(input())
notaProva = float(input())

media = (notaTrabalho + notaProva)/2

if(media >= 6):
    print('aprovado')
elif((media < 6) & (notaTrabalho >=2) ):
    print('talvez com sub')
else:
    print('reprovado')
