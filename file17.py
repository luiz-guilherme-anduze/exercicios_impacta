filo = str(input('digite o filo do animal: '))
classe = str(input('digite a classe do animal: '))
alimentacao = str(input('digite a alimentacao do animal: '))

if(filo == 'vertebrado'):
    if(classe == 'ave'):
        if(alimentacao == 'carnivoro'):
            print('aguia')
        elif(alimentacao == 'onivoro'):
            print('pomba')
    elif(classe == 'mamifero'):
        if(alimentacao == 'onivoro'):
            print('homem')
        elif(alimentacao == 'herbivoro'):
            print('vaca')
elif(filo == 'invertebrado'):
    if(classe == 'inseto'):
        if(alimentacao == 'hematofago'):
            print('pulga')
        elif(alimentacao == 'herbivoro'):
            print('lagarta')
    elif(classe == 'anelideo'):
        if(alimentacao == 'hematofago'):
            print('sanguessuga')
        elif(alimentacao == 'onivoro'):
            print('minhoca')
        

