# S, k = input().split(' ')
S, k = 'HACK 2'.split(' ')

S = sorted(S)
k = int(k)

from itertools import combinations_with_replacement

print(*list(map(''.join,combinations_with_replacement(S,k))), sep='\n')