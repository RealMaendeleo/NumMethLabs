import matplotlib.pyplot as plt
import math
from numpy import log as ln
import numpy as np


# 2 производная y по x
def dy2(y, x, z):  # y_pr - это производная у по х
    return 1 - y


# Решение диф. уравнения второго порядка методом
# Рунге-Кутты
# dy2 - функция второй производной
# y - Значение y в точке left
# y_pr - Значение производной в точке left

def runge4(dy2, y, y_pr, left, right, step=0.001):
    dataX, dataY = [], []
    xi = left
    while (xi <= right):
        dataX.append(xi)
        dataY.append(y)

        j1 = dy2(y, xi, y_pr)
        k1 = y_pr

        j2 = dy2(y + step * k1 / 2, xi, y_pr + step * j1 / 2)
        k2 = y_pr + step * j1 / 2

        j3 = dy2(y + step * k2 / 2, xi, y_pr + step * j2 / 2)
        k3 = y_pr + step * j2 / 2

        j4 = dy2(y + step * k3 / 2, xi, y_pr + step * j3 / 2)
        k4 = y_pr + step * j3 / 2

        y = y + (step / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        y_pr = y_pr + (step / 6) * (j1 + 2 * j2 + 2 * j3 + j4)
        xi = xi + step

    return dataX, dataY


# Вариант 3
left = 0  # Левая граница х
right = np.pi / 2 # Правая граница х
y0 = 0  # Значение у в точке 0
B = 0  # Значение y в точке 1
alpha = 1.0  # Начальное приближение alpha
eps = 0.0001
# Точность
# Решим диф.ур-е для начального alpha
dataX, dataY = runge4(dy2, y0, math.tan(alpha), left, right)
# Будем хранить значение y в 1 на предыдущем шаге
y_last = dataY[-1]
i = 0  # Счётчик для вывода графиков
while math.fabs(y_last - B) >= eps:
    # Решаем диф.ур-е для alpha+eps
    dataX, dataY = runge4(dy2, y0, math.tan(alpha + eps), left, right)
    # Находим величину изменения угла
    deltaAlpha = eps * (B - y_last) / (dataY[-1] - y_last)
    # Изменяем alpha
    alpha = alpha + deltaAlpha
    # Меняем y_last на вычисленный на этом шаге
    y_last = dataY[-1]

    i = i + 1
    #if i % 2 == 0:
    print(dataY[-1])
    plt.plot(dataX, dataY, color="green")

print("alpha = ", alpha)
plt.plot(dataX, dataY, color="red")
plt.show()
