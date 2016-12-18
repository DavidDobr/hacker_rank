# [0, 1, 1, 2, 3, 5, 8]

def fibonacci(n):
    final = [0]
    old = 0
    new = 1
    if n >= 2:
        final.append(1)
        for i in range(n-2):
            current = old + new
            final.append(current)
            old, new = new, current
    return final

n = 15

if __name__ == '__main__':
    print(fibonacci(n))
