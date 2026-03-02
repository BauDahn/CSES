n = int(input()) # No importo sys porque solo hay 1 entrada

if n == 1:
    print(1)
elif n < 4:
    print("NO SOLUTION")
else:
    lista = []
    
    for i in range(1, n, 2):
        lista.append(i + 1)

    for i in range(1, n + 1, 2):
        lista.append(i)

    print(' '.join(map(str, lista)))

