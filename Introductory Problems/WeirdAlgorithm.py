n = int(input())
lista = []
while n != 1:
    lista.append(n)
    if n % 2 == 0:
        n //= 2
        continue
    n = (n * 3) + 1

lista.append(1)
print(f' '.join(map(str, lista)))
