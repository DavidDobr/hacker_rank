import math

class point3d(object):
    """
    point object


    @parameters: one list of 3 coordinates
    @ToDo: add incorrect x,y,z input handling
    """
    def __init__(self, l):
        # set point's coordinates
        # l is an iterable (list or )
        self.x, self.y, self.z = map(float, l)
        self.coords = (self.x, self.y, self.z)

    def __add__(self, no):
        return None

    def __sub__(self, no):
        # substracting point substracts CORRESPONDING coordinates' values
        return [m_i - n_i for m_i, n_i in zip(self.coords, no.coords)]

class vector(object):
    """
    3d eucledian vector object specifying head & tail

    Accepts 2 Point_3d objects
    usage: Vector(tail, head)

    @ToDo: add length function
    """
    def __init__(self, tail, head):
        self.tail = tail
        self.head = head
        self.gradient = head - tail
        self.length = math.sqrt( sum([c**2 for c in self.gradient]) )

def dot_product(v1, v2):
    """
    calculate dot product of 2 vectors

    @parameters: two 3d vectors v1, v2
    @returns: dot product as float

    """
    # https://en.wikipedia.org/wiki/Dot_product
    # dot product simply sums cross-multiplications of corresponding coordinates
    multiples = [m_i * n_i for m_i, n_i in zip(v1.gradient, v2.gradient)]
    return float(sum(multiples))

def vectors_angle(v1, v2):
    """
    calculate angle b/w two 3d vectors

    @parameters: two 3d vectors v1, v2
    @returns: angle as RADIANS
    """

    # http://www.intmath.com/vectors/7-vectors-in-3d-space.php
    # returns angle b/w vectrs in RADIANS
    cos_theta = dot_product(v1, v2)/(v1.length*v2.length)
    theta = math.acos(cos_theta)
    return theta

def cross_product(v1, v2):
    """
    calculate cross product b/w two 3d vectors

    @parameters: two 3d vectors v1, v2
    @returns: cross product as vector object
    """
    # https://www.mathsisfun.com/algebra/vectors-cross-product.html
    ax, ay, az = v1.gradient
    bx, by, bz = v2.gradient

    # since we use vectorised v1, v2, we can assume they both start at the origin
    # then AxB = (Ay*Bz - Az*By, ..., ...) [reffer to link above for full formula]
    cx = ay*bz - az*by
    cy = az*bx - ax*bz
    cz = ax*by - ay*bx

    # cross is our resulting vector, i.e. cross-product b/w v1 and v2
    cross_tail = point3d( ( 0,  0,  0) )
    cross_head = point3d( (cx, cy, cz) )
    cross = vector(cross_tail, cross_head)
    return cross
