N, M = map(int, input().split())

data = [list(map(int, input().split())) for row in range(N)]
#print(data)

K = int(input())
#print(K)

[print(*row) for row in sorted(data, key=lambda x: x[K])]

None
