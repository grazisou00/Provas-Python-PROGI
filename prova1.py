def alternada(N, seq):
    N > 1 
    impar = True
    M = 1 
    for i in range (1, N):
        if impar:
            if seq[i]% 2 == 0:
                impar = False
                M += 1
        else:
            if seq[i]% 2 != 0:
                impar = True 
                M += 1
    return M if impar else "NAO"

N = int(input('informe N: '))
seq = [int(x) for x in input('informe a sequencia: ').strip().split()]
print(alternada(N, seq))
print("%")


