import sys

# sys.stdin = open('input.txt', 'r')
data = sys.stdin.read().split()

n = int(data[0])
lista = set(map(int, data[1 : ]))

for i in range(1, n + 1):
    if i in lista:
        continue
    print(i)