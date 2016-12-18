s = input()
def is_even(n):
    if n.isnumeric():
        return int(n) % 2 == 0
    else:
        return False

print(*sorted(s, key=lambda c: (c.isnumeric(), c.isupper(), is_even(c), c)), sep='')
