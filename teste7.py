n = int(input())

if(n>=2):
    if((n%2)==0):
        impar = n-1
        par = n+2
        print(impar,par)
    else:
        impar = n-2
        par = n+1
        print(impar,par)
