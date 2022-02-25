

while True:
    try:
        n = int(input())
        epr = 0
        ehd = 0
        intrusos = 0
        
        for i in range(1,n+1):
            aluno = input().split()
            a, b= int(aluno[0]), aluno[1]
            if b == 'EPR':
                epr += 1
            elif b == 'EHD':
                ehd += 1
            elif b != 'EPR' or b != 'EHD':
                intrusos += 1
        
        print(f'EPR: {epr}')
        print(f'EHD: {ehd}')
        print(f'INTRUSOS: {intrusos}')
    except EOFError:
        break