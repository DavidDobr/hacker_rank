
# coding: utf-8

# In[1]:

from math import cos, acos, sin, asin, sqrt, degrees

import sys
print(sys.version)


# In[2]:

class Point_3d(object):
    """
    Accepts 3 numerical parameters representing 3d coordinates, converts them to float
    
    returns a tuple in form of (x, y, z) coordinates
    
    @ToDo: add incorrect x,y,z input handling
    """
    def __init__(self, x, y, z):
        # set point's coordinates
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.coords = [self.x, self.y, self.z]
        
    def __add__(self, no):
        return None
        
    def __sub__(self, no):
        # substracting point substracts CORRESPONDING coordinates' values
        return [m_i - n_i for m_i, n_i in zip(self.coords, no.coords)]
    
    



# INSTANTIATE TEST POINTS
origin = Point_3d(0, 0, 0)
a = Point_3d(*"0 4 5".split())
b = Point_3d(*"1 7 6".split())
c = Point_3d(*"0 5 9".split())
d = Point_3d(*"1 7 2".split())

[print(obj.coords) for obj in [origin, a, b, c, d]]
None

# a, b, c, d = [Point_3d(*input().split()) for _ in range(4)]


# In[3]:

class Vector(object):
    """
    Accepts 2 Point_3d objects
    usage: Vector(tail, head)
    
    @ToDo: add length function
    """
    def __init__(self, tail, head):
        self.tail = tail
        self.head = head
        self.vectorized = head - tail
        self.length = self.length()
    def length(self):
        return sqrt( sum([c**2 for c in self.vectorized]) )

# INSTANTIATE INSTANCES OF WORKING VECTORS
AB = Vector(a, b)
BC = Vector(b, c)
CD = Vector(c, d)

[print(obj.vectorized) for obj in (AB, BC, CD)]
None


# In[4]:

AB.length


# In[5]:

def dot_product(v1, v2):
    # https://en.wikipedia.org/wiki/Dot_product
    # dot product simply sums cross-multiplications of corresponding coordinates
    multiples = [m_i * n_i for m_i, n_i in zip(v1.vectorized, v2.vectorized)]
    return sum(multiples)
print(dot_product(AB, BC))


# In[6]:

def vectors_angle(v1, v2):
    # http://www.intmath.com/vectors/7-vectors-in-3d-space.php
    # returns angle b/w vectrs in RADIANS
    cos_theta = dot_product(v1, v2)/(v1.length*v2.length)
    theta = acos(cos_theta)
    return theta
vectors_angle(AB, BC)


# In[7]:

def cross_product(v1, v2):
    # https://www.mathsisfun.com/algebra/vectors-cross-product.html
    ax, ay, az = v1.vectorized
    bx, by, bz = v2.vectorized
    
    # since we use vectorised v1, v2, we can assume they both start at the origin
    # then AxB = (Ay*Bz - Az*By, ..., ...) [reffer to link above for full formula]
    cx = ay*bz - az*by
    cy = az*bx - ax*bz
    cz = ax*by - ay*bx
    
    # c is our resulting vector, i.e. cross-product b/w v1 and v2
    c_tail = Point_3d( 0,  0,  0)
    c_head = Point_3d(cx, cy, cz)
    c = Vector(c_tail, c_head)
    
    return c

cross_product(AB, BC).vectorized


# In[8]:

print(cross_product(AB, BC)) # it is a vector


# In[9]:

M = cross_product(AB, BC)
N = cross_product(BC, CD)

print(M.vectorized)
print(N.vectorized)


# In[10]:

# Calculating angles b/w planes

cos_phi = dot_product(M, N) / (M.length*N.length)
phi = acos(cos_phi)
print('{0:.2f}'.format(degrees(phi)))


# In[11]:

# Sample Output
8.19

