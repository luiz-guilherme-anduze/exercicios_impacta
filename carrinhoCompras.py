entrada = []
entrada = input().split()
menu =[]    

while True:
    menu = input().split()
    if menu[0] == 'exibir':
        for item in range(0,len(entrada)):
            entrada[item] = int(entrada[item])
        entrada.sort()
        print(*entrada)    
    elif menu[0] == 'adicionar':
        menu[1] = int(menu[1])
        entrada.append(menu[1])
    elif menu[0] == 'remover':
        if int(menu[1]) in entrada:
            menu[1] = int(menu[1])
            entrada.remove(menu[1])
        else:
            print('código',menu[1],'não encontrado')
    elif menu[0] == 'encerrar':
        if entrada:
            for item in range(0,len(entrada)):
                entrada[item] = int(entrada[item])
            entrada.sort()
            print(*entrada)   
        break

