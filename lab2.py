import matplotlib.pyplot as plt
import numpy as np
#from decimal import Decimal


def F(x):
    return pow(x,3) - 3*x*x - 14*x - 8

def dF(x):
    return 3*x*x - 6*x - 14


def dichotomy(a, b, eps):
    while (b-a > eps):
        c = (a + b) / 2
        if F(b) * F(a) < 0:
            a = c
        else:
            b = c
    return c
    

def newton(a, eps):
    xnext = a
    x = xnext
    count = 1
    xnext = x - F(x) / dF(x)
    
    while abs(xnext - x) >= abs(eps) or abs(F(x)) >= abs(eps):
        x = xnext
        xnext = x - F(x) / dF(x)
        count += 1
    print(count)
    return xnext


option = 10
x0 = -4
x1 = 2
N = 1000
E = float(input('epsilon = '))
h = (x1 - x0) / N
print("0) Выход из программы")
print("1) Метод дихотомии")
print("2) Метод Ньютона")
option = int(input())

if option == 0:
    raise SystemExit(0)
elif option == 1:
    count = 0
    x = dichotomy(x0, x1, E)
    print(x)
elif option == 2:
    x = newton(6, E)
    print(x)

F2 = np.vectorize(F)
fig, ax = plt.subplots(figsize=(10, 5))
plt.grid()
Xs = np.array([i for i in np.arange(x0, x1, h)])
Ys = F2(Xs)
plt.plot(Xs, Ys)
plt.show()