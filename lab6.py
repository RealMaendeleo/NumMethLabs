import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return math.cos(x) * math.cos(x) * math.exp(-x)

a = -5
b = 0
N = 1000
h = (b - a) / N
Xs = np.array([i for i in np.arange(a, b, h)])
Ys = np.array([0] * N, np.float_)
f1 = np.vectorize(f)
Ys = f1(Xs)

print("1) Минимум")
print("2) Максимум")
choice = int(input())
E = 0.0005
i = 0
while math.fabs(b-a) > E:
    i += 1
    x1 = a + 0.381966 * (b - a) #делит 1 к 1,618
    x2 = a + 0.618034 * (b - a)
    y1 = f(x1)
    y2 = f(x2)
    if choice == 1:
        if y1 > y2:
            a = x1
        else:
            b = x2
    elif choice == 2:
        if y1 < y2:
            a = x1
        else:
            b = x2
x = (a + b)/2
print(x, f(x))
print(i)
plt.plot(Xs, Ys)
plt.show()
