#entrada
tempoViagem = int(input())
velocidadeMedia = int(input())

#processamento
gastoCombustivel = (tempoViagem * velocidadeMedia)/12

#saida
print(f'{gastoCombustivel:.3f}')