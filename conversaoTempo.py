tempo = int(input())

segundos = 0
minutos = 0
horas = 0

if tempo >= 60:
    if tempo < 3600:
        minutos = tempo // 60
        segundos = tempo % 60
    elif tempo >= 3600:
        horas = (tempo / 60) // 60
        minutos = (tempo / 60) % 60
        segundos = (tempo % 60) % 60
    print(f'{horas}:{minutos}:{segundos}')
else:
    print(f'{horas}:{minutos}:{tempo}')


