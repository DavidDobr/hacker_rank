from collections import deque


def attachable(arr, len1, len2):
    if len(arr) == 0:
        return True
    else:
        return max(len1, len2) <= min(arr)


def unstackable(H):
    V = deque()
    while len(H) > 0:
        left = H[0]
        right = H[-1]
        if not attachable(V, left, right):
            return 'No'

        if right >= left:
            V.append(H.pop())
        else:
            V.append(H.popleft())
    # return min(V)
    return 'Yes'


H = deque(map(int, "9 8 5 2 1 7 10 15".split()))
print(unstackable(H))