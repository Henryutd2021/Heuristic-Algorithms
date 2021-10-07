import numpy as np
l = []

x = range(1, 32)
for i in x:
    y = i**3-60*i**2+90*i
    l.append(y)
print(l)