dia = str(input('Que dia é hoje? '))
prazo = int(input('Qual o prazo da entrega? '))

if(prazo==0):
    print('chega hoje!')
elif(prazo==1):
    if(dia=='domingo'):
        print('sera entregue segunda')
    elif(dia=='segunda'):
        print('sera entregue terca')
    elif(dia=='terca'):
        print('sera entregue quarta')
    elif(dia=='quarta'):
        print('sera entregue quinta')
    elif(dia=='quinta'):
        print('sera entregue sexta')
    elif(dia=='sexta'):
        print('sera entregue sabado')
    elif(dia=='sabado'):
        print('sera entregue domingo')
elif(prazo==2):
    if(dia=='domingo'):
        print('sera entregue terca')
    elif(dia=='segunda'):
        print('sera entregue quarta')
    elif(dia=='terca'):
        print('sera entregue quinta')
    elif(dia=='quarta'):
        print('sera entregue sexta')
    elif(dia=='quinta'):
        print('sera entregue sabado')
    elif(dia=='sexta'):
        print('sera entregue domingo')
    elif(dia=='sabado'):
        print('sera entregue segunda')
elif(prazo==3):
    if(dia=='domingo'):
        print('sera entregue quarta')
    elif(dia=='segunda'):
        print('sera entregue quinta')
    elif(dia=='terca'):
        print('sera entregue sexta')
    elif(dia=='quarta'):
        print('sera entregue sabado')
    elif(dia=='quinta'):
        print('sera entregue domingo')
    elif(dia=='sexta'):
        print('sera entregue segunda')
    elif(dia=='sabado'):
        print('sera entregue terca')
elif(prazo==4):
    if(dia=='domingo'):
        print('sera entregue quinta')
    elif(dia=='segunda'):
        print('sera entregue sexta')
    elif(dia=='terca'):
        print('sera entregue sabado')
    elif(dia=='quarta'):
        print('sera entregue domingo')
    elif(dia=='quinta'):
        print('sera entregue segunda')
    elif(dia=='sexta'):
        print('sera entregue terca')
    elif(dia=='sabado'):
        print('sera entregue quarta')
elif(prazo==5):
    if(dia=='domingo'):
        print('sera entregue sexta')
    elif(dia=='segunda'):
        print('sera entregue sabado')
    elif(dia=='terca'):
        print('sera entregue domingo')
    elif(dia=='quarta'):
        print('sera entregue segunda')
    elif(dia=='quinta'):
        print('sera entregue terca')
    elif(dia=='sexta'):
        print('sera entregue quarta')
    elif(dia=='sabado'):
        print('sera entregue quinta')
elif(prazo==6):
    if(dia=='domingo'):
        print('sera entregue sabado')
    elif(dia=='segunda'):
        print('sera entregue domingo')
    elif(dia=='terca'):
        print('sera entregue segunda')
    elif(dia=='quarta'):
        print('sera entregue terca')
    elif(dia=='quinta'):
        print('sera entregue quarta')
    elif(dia=='sexta'):
        print('sera entregue quinta')
    elif(dia=='sabado'):
        print('sera entregue sexta')