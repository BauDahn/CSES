import sys

sys.stdin = open('input.txt', 'r')

data = sys.stdin.read().split()
it = iter(data)
to_int = int

n = to_int(next(it))