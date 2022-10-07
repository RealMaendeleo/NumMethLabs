import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate


def f(x):
    return np.sin(2*x + x*x)


def extract_diag(mx):
    # Нижняя диагональ
    a = []
    # Главная диагональ
    b = []
    # Верхняя диагональ
    c = []

    for i in range(len(mx)):
        b.append(mx[i][i])

        if i == 0:
            a.append(0)
        else:
            a.append(mx[i][i-1])

        if i == len(mx)-1:
            c.append(0)
        else:
            c.append(mx[i][i+1])

    return a, b, c


def thomas(ABC, D):
    As = []
    Bs = []
    Xs = [0] * len(ABC)

    a, b, c = extract_diag(ABC)

    for i in range(len(ABC)):
        if i == 0:
            As.append(-c[i] / b[i])
            Bs.append(D[i] / b[i])
        else:
            e = a[i] * As[i - 1] + b[i]
            As.append(-c[i] / e)
            Bs.append((D[i] - a[i] * Bs[i - 1]) / e)

    for i in range(len(ABC) - 1, -1, -1):
        if i == len(ABC) - 1:
            Xs[i] = (D[i] - a[i] * Bs[i - 1]) / (b[i] + a[i] * As[i - 1])
        else:
            Xs[i] = As[i] * Xs[i + 1] + Bs[i]

    return Xs


a = 0
b = np.pi / 3
N = int(input("Введите количество шагов: "))
h = (b - a) / N

# y = a + b*h + c*h**2 + d*h**3

Xs = np.array([i for i in np.arange(a, b, h)])
Ys = f(Xs)
As = []
Bs = []
Cs = []
Ds = []

#Step 1

c_matrix = []
extend_matrix = []


for k in range(N-2):
    if k == N-2:
        extend_matrix.append(3 * (((Ys[N-1] - Ys[N-2]) / h) - ((Ys[N-2] - Ys[N-3]) / h)))
    else:
        extend_matrix.append(3 * (((Ys[k+2] - Ys[k+1]) / h) - ((Ys[k+1] - Ys[k]) / h)))

    new_row = [0]*(N-2)

    if k == 0:
        new_row[0] = 4*h
        new_row[1] = h
    elif k == N-3:
        new_row[N-4] = h
        new_row[N-3] = 4*h
    else:
        new_row[k-1] = h
        new_row[k] = 4*h
        new_row[k+1] = h

    c_matrix.append(new_row)

c_matrix = np.array(c_matrix)
Cs = thomas(c_matrix, extend_matrix)
Cs = [0] + Cs

#Step 2

true_func_x = np.array([i for i in np.arange(a,b,0.01)])
plt.plot(true_func_x, f(true_func_x))

for k in range(N-1):
    As.append(Ys[k])
    if k <= N-3:
        Ds.append((Cs[k+1]-Cs[k])/(3*h))
        Bs.append(((Ys[k+1]-Ys[k])/h)-(h*(2*Cs[k]+Cs[k+1]))/3)
    else:
        Ds.append(-(Cs[N-2])/(3*h))
        Bs.append(((Ys[N-1]-Ys[N-2])/h)-(h*(2*Cs[N-2]))/3)

for k in range(N-1):
    pXs = np.array([i for i in np.arange(Xs[k], Xs[k+1], 0.01)])
    func = As[k]+(Bs[k]*(pXs-Xs[k]))+(Cs[k]*((pXs-Xs[k])**2))+(Ds[k]*((pXs-Xs[k])**3))
    plt.plot(pXs, func)

function = []
xx = 0
while (xx <= np.pi / 3):
    function.append(f(xx))
    xx += N / (np.pi / 3)

print(func)

plt.plot(function)
plt.scatter(Xs, Ys)
plt.show()