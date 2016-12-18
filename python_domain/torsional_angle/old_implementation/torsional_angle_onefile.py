

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
    ax, ay, az = v1.gradient
    bx, by, bz = v2.gradient

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

cross_product(AB, BC).gradient


# In[8]:

print(cross_product(AB, BC)) # it is a vector


# In[9]:

M = cross_product(AB, BC)
N = cross_product(BC, CD)

print(M.gradient)
print(N.gradient)


# In[10]:

# Calculating angles b/w planes

cos_phi = dot_product(M, N) / (M.length*N.length)
phi = acos(cos_phi)
print('{0:.2f}'.format(degrees(phi)))


# In[11]:

# Sample Output
8.19
