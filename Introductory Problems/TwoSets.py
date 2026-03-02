n = int(input())

suma = (n**2 + n) // 2
if suma % 2 == 0:
    print("YES")
    lista1 = []
    lista2 = []
    objetivo = suma // 2
    for i in range(n, 0, -1):
        if i <= objetivo:
            lista1.append(i)
            objetivo -= i
            continue
        lista2.append(i)
    
    print(len(lista1))
    print(" ".join(map(str, lista1)))
    print(len(lista2))
    print(" ".join(map(str, lista2)))
else:
    print("NO")


            

