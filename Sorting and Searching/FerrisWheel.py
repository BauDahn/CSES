import sys

input = sys.stdin.readline

n, x = map(int, input().split())

pesos = list(map(int, input().split()))

pesos.sort()

contador = 0
i = 0

while i < n:
    

print(contador)
    