"""
Input is stackable if it's shaped like a 'mountain' with smaller
numbers in the middle.
"""

from collections import deque

def attachable(arr, len1, len2):
    if len(arr) == 0:
        return True
    else:
        return max(len1, len2) <= min(arr)


def unstackable(H):
    if len(H) < 3: return 'Yes'
    inflections = 0
    while len(H) > 1:
        a, b = H.popleft(), H[0]
        if inflections == 0:
            if a < b: inflections += 1
        elif inflections == 1:
            if a > b: return 'No'
    return 'Yes'


H = deque(map(int, "1 0 5 1".split()))
print(unstackable(H))