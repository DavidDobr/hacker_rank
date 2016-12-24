from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x*y, fracs)
    return t.numerator, t.denominator

input_test = ['1 2', '3 4', '10 6']
fracs = []
for test in input_test:
    fracs.append(Fraction(*map(int, test.split())))
result = product(fracs)
print(*result)
