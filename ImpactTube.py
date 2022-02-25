def canais(qtdCanais):
    
    tabela = []
    
    for i in range(qtdCanais):
        entrada = input().split(';')
        entrada[1] = int(entrada[1])
        entrada[2] = float(entrada[2])
        entrada[3] = entrada[3] == 'sim'
        tabela.append(entrada)
    
    return tabela

def bonus(tabela):
    
    bonusP = float(input())
    bonusN = float(input())
    print(f'-----\nBÔNUS\n-----')

    for linha in tabela:
        if linha[3] == True:
            bonus = ((linha[1]//1000) * bonusP) + linha[2]
            print(f'{linha[0]}:R$ {bonus:.2f}')
        else:
            bonus = ((linha[1]//1000) * bonusN) + linha[2]
            print(f'{linha[0]}: R$ {bonus:.2f}')

qtdCanais = int(input())
tabela = canais(qtdCanais)
bonus(tabela)