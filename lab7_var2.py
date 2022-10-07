import numpy as np
from math import sqrt, cos, sin
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def r(t, u):
    return np.sqrt((2 + cos(t) - (cos(u)**3))**2 + (sin(t) - 4 - (sin(u)**3))**2)

def df_du(h, t, u):
    return (r(t, u + h) - r(t, u - h)) / (2 * h)

def df_dt(h, t, u):
    return (r(t + h, u) - r(t - h, u)) / (2 * h)

lmd1 = 0.001
lmd2 = 0.001
E = 0.00001
uu = 4.71
tt = 0
rr = r(tt, uu)
step = 0.001

tt_v = [tt]
uu_v = [uu]
rr_v = [rr]

while abs(df_dt(step, tt, uu)) > E and abs(df_du(step, tt, uu)) > E :
    tt = tt - lmd1 * df_dt(step, tt, uu)
    uu = uu - lmd2 * df_du(step, tt, uu)
    rr = r(tt, uu)
    tt_v.append(tt)
    uu_v.append(uu)
    rr_v.append(rr)

print(tt_v[-1], uu_v[-1], rr_v[-1])

u_plt, t_plt = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
R_plt = np.sqrt((2 + np.cos(t_plt) - (np.cos(u_plt)**3))**2 + (np.sin(t_plt) - 4 - (np.sin(u_plt)**3)) ** 2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(t_plt, u_plt, R_plt)
ax.scatter(tt_v, uu_v, rr_v, s=2, color="red")
ax.scatter(tt_v[-1], uu_v[-1], rr_v[-1], s=10, color="black")
ax.set_xlabel("t")
ax.set_ylabel("u")
ax.set_zlabel("z")
plt.show()