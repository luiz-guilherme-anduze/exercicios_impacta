def lista_perfeitos(n):
    
    lista =[]
    
    for numero in range(2, n):
        soma = 0
        for divisor in range(1, numero):
            if numero % divisor == 0:
                soma += divisor
                
        if soma == numero:
            lista.append(n)
    return lista
    
n = int(input("Digite um numero natural maior ou igual a 2 ")
perfeitos = lista_perfeitos(n)
print(perfeitos)