p, l = input().strip(), input().split()
print(all(map(lambda x: int(x) > 0, l)) and any(map(lambda x: str(x) == str(x)[::-1], l)))
