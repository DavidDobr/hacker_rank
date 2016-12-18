

# In[6]:




# In[7]:




cross_product(AB, BC).gradient


# In[8]:

print(cross_product(AB, BC)) # it is a vector


# In[9]:



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
