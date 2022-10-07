import numpy as np
from math import sqrt

import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D


def r(t, u):
    """Function of distance between two points"""
    return sqrt((t - 1 - (u + 1)) ** 2 + ((t - 1) / 2 - (u - 2)) ** 2 + ((t - 2) - (t + 1) / 3) ** 2)


def plot_lines():
    """Get values for a plot of straight lines"""
    a = np.array([i for i in np.arange(-2, 10, 0.01)])

    x1 = a - 1
    y1 = (a - 1) / 2
    z1 = a - 2

    x2 = a + 1
    y2 = a - 2
    z2 = (a + 1) / 3
    return [x1, y1, z1, x2, y2, z2]

def sub(t, u):
    """Get values for a plot of straight lines"""
    a = np.array([i for i in np.arange(-2, 10, 0.01)])

    x1 = t - 1
    y1 = (t - 1) / 2
    z1 = t - 2

    x2 = (u + 1)
    y2 = u - 2
    z2 = (u + 1) / 3
    return [x1, y1, z1, x2, y2, z2]


def df_du(h, t, u):
    """Partial derivative of second parameter - u"""
    return (r(t, u + h) - r(t, u - h)) / (2 * h)


def df_dt(h, t, u):
    """Partial derivative of first parameter - u"""
    return (r(t + h, u) - r(t - h, u)) / (2 * h)

#Initial parameters
lmd1 = 0.01
lmd2 = 0.01
Niter = 10000 # Количество итeраций
uu = 10 # Начальное значение u
tt = 10 # Начальное значение t
rr = r(tt, uu) # Начальное значение r
step = 0.001 # Шаг
E = 0.01
tt_v = [uu]
uu_v = [tt]
rr_v = [rr]
# Метод нискорейшего спуска
for n in range(Niter):
    tt = tt - lmd1 * df_dt(step, tt, uu)
    uu = uu - lmd2 * df_du(step, tt, uu)
    rr = r(tt, uu)
    tt_v.append(tt)
    uu_v.append(uu)
    rr_v.append(rr)
    if abs(df_dt(step, tt, uu)) < E and abs(df_du(step, tt, uu)) < E:
        break
print(n)

#Вывод ответа
tur = f"t = {tt_v[-1]}, u = {uu_v[-1]}, r_min = {rr_v[-1]}"
print(tur)

#Рассчитать значения для построения трехмерного графика для расстояния между двумя прямыми
u_plt, t_plt = np.mgrid[-10:10:20j, -10:10:20j]
R_plt = np.sqrt((t_plt - 1 - (u_plt + 1)) ** 2 + ((t_plt - 1) / 2 - (u_plt - 2)) ** 2 + ((t_plt - 2) - (t_plt + 1) / 3) ** 2)

#Рассчитать значения для прямых
values_lines = plot_lines()
fig = plt.figure()

#Построить прямые
ax = fig.add_subplot(111, projection='3d')
ax.plot(values_lines[0], values_lines[1], values_lines[2])
ax.plot(values_lines[3], values_lines[4], values_lines[5])
plt.show()

#Построить график функции для наискорейшего спуска (расстояние)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(t_plt, u_plt, R_plt)
ax.scatter(tt_v, uu_v, rr_v, s=2, color="red", label="Спуск")
ax.scatter(tt_v[-1], uu_v[-1], rr_v[-1], s=14, color="black", label="Минимум")
ax.set_title("График функции расстояния от параметров, задающих прямые")
ax.set_xlabel("t")
ax.set_ylabel("u")
ax.set_zlabel("r")
ax.legend()
plt.show()

array = sub(tt_v[-1], uu_v[-1])
x_r = (array[3] - array[0]) / 4 + array[0]
y_r = (array[4] - array[1]) / 4 + array[1]
z_r = (array[5] - array[2]) / 4 + array[2]

print(array)
print(x_r, y_r, z_r)
