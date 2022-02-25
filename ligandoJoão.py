mae = input('Como a mãe de João se sente? ')
joao = input('João está ocupado ou livre? ')
joaoLugar = input('Onde João está?')


while mae == 'preocupada':
    print('ligar para João')
    if joao == 'ocupado':
        print('João não atende')
        print('Ligar para João depois')
    elif joao == 'livre' and joaoLugar =='chegando em casa':
        print('João desabafa até chegar em casa')
        break
    elif joao == 'livre' and joaoLugar == 'em casa':
        print('João desabafa por 5 min e desliga')
        break   