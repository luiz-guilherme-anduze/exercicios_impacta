divida = int(input())
parcela = int(input())
pagamento = 1

while(divida != 0):
    if(divida >= parcela):
        print(f'pagamento: {pagamento}')
        print(f'antes = {divida}')
        divida = divida - parcela
        print(f'depois = {divida}')
        print('-----')
    else:
        print(f'pagamento: {pagamento}')
        print(f'antes = {divida}')
        divida = 0
        print(f'depois = {divida}')
        print('-----')
    pagamento += 1
