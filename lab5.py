import matplotlib.pyplot as plt
import numpy as np
import math

def dy(x, y, z):
    return math.log(2*x + math.sqrt(4*x*x + z*z)) - 2*x*y + z - x - 1

def dz(x, y, z):
    return -math.sqrt(4*x*x + y*y)
    

y = 0.5
z = 1
x = 0
right = 1
h = 0.01
n = int((right - x)/h)

Xs = np.array([i for i in np.arange(x - h, right, h)])
Ys = np.array([0] * (n+1), np.float_)
Ys[0] = y
Zs = np.array([0] * (n+1), np.float_)
Zs[0] = z

i = 1
while x <= right:
    a1 = h * dy(x, y, z)
    b1 = h * dz(x, y, z)

    a2 = h * dy(x + h / 2, y + a1 / 2, z + b1 / 2)
    b2 = h * dz(x + h / 2, y + a1 / 2, z + b1 / 2)

    a3 = h * dy(x + h / 2, y + a2 / 2, z + b2 / 2)
    b3 = h * dz(x + h / 2, y + a2 / 2, z + b2 / 2)

    a4 = h * dy(x + h, y + a3, z + b3)
    b4 = h * dz(x + h, y + a3, z + b3)
    
    y += (a1 + 2*a2 + 2*a3 + a4) / 6
    Ys[i] = y
    z += (b1 + 2*b2 + 2*b3 + b4) / 6
    Zs[i] = z
    x += h
    i += 1

plt.grid()
plt.plot(Xs, Ys, label="y(x) 4 порядок")
plt.plot(Xs, Zs, color="red", label="z(x) 4 порядок")


y = 0.5
z = 1
x = 0
i = 1
Ys1 = np.array([0] * (n+1), np.float_)
Ys1[0] = y
Zs1 = np.array([0] * (n+1), np.float_)
Zs1[0] = z

while x <= right:    
    a1 = dy(x, y, z)
    b1 = dz(x, y, z)
    a2 = dy(x + h, y + h * a1, z + h * b1)
    b2 = dz(x + h, y + h * a1, z + h * b1)
    y += h * (a1 + a2) / 2
    Ys[i] = y
    z += h * (b1 + b2) / 2
    Zs[i] = z
    
    y += h * dy(x + h/2, y + y*h/2, z + z*h/2)
    Ys1[i] = y
    z += h * dz(x + h / 2, y + y * h / 2, z + z * h / 2)
    Zs1[i] = z
    x += h
    i += 1

plt.plot(Xs, Ys1, label="y(x) 2 порядок")
plt.plot(Xs, Zs1, label="z(x) 2 порядок")


plt.legend()
plt.show()