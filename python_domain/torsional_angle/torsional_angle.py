import math
import vectors_eucledian as ve

if __name__ == "__main__":
    # execute only if run as a script

    # INSTANTIATE TEST POINTS
    origin = ve.point3d((0, 0, 0))
    a = ve.point3d("0 4 5".split())
    b = ve.point3d("1 7 6".split())
    c = ve.point3d("0 5 9".split())
    d = ve.point3d("1 7 2".split())

    [print(obj.coords) for obj in [origin, a, b, c, d]]
    # a, b, c, d = [ve.point3d(*input().split()) for _ in range(4)]

    # INSTANTIATE INSTANCES OF WORKING VECTORS
    AB = ve.vector(a, b)
    BC = ve.vector(b, c)
    CD = ve.vector(c, d)

    [print(obj.gradient, obj.length) for obj in (AB, BC, CD)]
