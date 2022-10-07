import numpy as np
import math

def rectangles():
    global a, b, h
    sum = 0
    for x in np.arange(a, b+h, h):
        sum += (math.cos(x*x) + math.cos(x*x-h)) / 2 
    return sum * h

def trapeze():
    global a, b, h
    sum = 0
    for x in np.arange(a, b+h, h):
        sum += 2 * math.cos(x*x)
    sum -= (math.cos(a*a) + math.cos(b*b))
    return sum * h * 0.5

def simpson():
    global a, b, h
    sum = 0
    i = 1
    sum += math.cos(a*a) + math.cos(b*b)
    for x in np.arange(a+h, b, h):
        if i == 0:
            sum += 2 * math.cos(x*x)
            i = 1
        elif i == 1:
            sum += 4 * math.cos(x*x)
            i = 0
    return (sum * h) / 3

a = 1
b = 4
N = 50
h = (b - a) / N
decimals = 7

square = rectangles()
accuracy = math.fabs(0.841470984808 - square)
print("\nМетод прямоугольников: ", round(square, decimals), "(", round(accuracy, decimals), ")")

square = trapeze()
accuracy = math.fabs(0.841470984808 - square)
print("Метод трапеций: ", round(square, decimals), "(", round(accuracy, decimals), ")")

square = simpson()
accuracy = math.fabs(0.841470984808 - square)
print("Метод Симпсона: ", round(square, decimals), "(", round(accuracy, decimals), ")\n")