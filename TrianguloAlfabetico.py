n = int(input())

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
k =2

for i in range(1, n+1):
    for j in range (1, k):
        print(f'{alfabeto[i-1]}',end="")
    k += 1
    i += 1
    print()

    
