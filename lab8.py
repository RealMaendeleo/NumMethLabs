import numpy as np
from math import sqrt, cos, sin , log ,fabs , tan ,exp
import matplotlib.pyplot as plt
from numpy import log as ln
from mpl_toolkits.mplot3d import Axes3D

def var(x , ans): #ищем коэффициенты для матрицы
    if(ans == 0):
       return 1
    if(ans == 1):
      return exp(sqrt(abs(x)))
    if(ans == 2):
      return ln(cos(x))

def F_mnk(x ,c):
    return c[0] + c[1] * exp(sqrt(abs(x))) + c[2] * ln(cos(x))

def F(x): #идеальная функция из методички
    return 1.88 - 0.9 * exp(sqrt(abs(x))) + 1.09 * ln(cos(x))


def Forward(n,a,b):
    i=0
    j=0
    im=0
    v=0
    for k in range(0 , n-1):
        im = k
        for i in range(k+1, n):
            if (fabs(a[im][k]) < fabs(a[i][k])): im = i
        if (im != k):
            for j in range(0 , n):
                v=a[im][j]
                a[im][j]=a[k][j]
                a[k][j]=v
                v=b[im]
                b[im]=b[k]
                b[k]=v
        for i in range(k+1 , n):
            v = a[i][k] / a[k][k]
            a[i][k] = 0
            b[i] = b[i] - v * b[k]
            for j in range(k+1 , n):
                a[i][j]=a[i][j]-v * a[k][j]

def Back(n,a,b ,x):
    s = 0
    x[n - 1] = b[n - 1] / a[n - 1][n - 1]
    j=0
    i =n-2
    while(i>= 0):
        s = 0
        for j in range(i+1 , n):
            s=s+a[i][j ] *x[j]
        x[i]=(b[i]-s ) /a[i][i]
        i = i-1
    return x


def FancyPrint(A, B, selected):
    for row in range(len(B)):
        print("(", end='')
        for col in range(len(A[row])):
             print("\t{1:10.2f}{0}".format(" " if (selected is None
or selected != (row, col)) else "*", A[row][col]), end='')
        print("\t) * (\tX{0}) = (\t{1:10.2f})".format(row + 1, B[row]))

def SwapRows(A, B, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]
# --- end of перемена местами двух строк системы

# --- деление строки системы на число
def DivideRow(A, B, row, divider):
    A[row] = [a / divider for a in A[row]]
    B[row] /= divider
# --- end of деление строки системы на число

# --- сложение строки системы с другой строкой, умноженной на число
def CombineRows(A, B, row, source_row, weight):
    A[row] = [(a + k * weight) for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * weight
# --- end of сложение строки системы с другой строкой, умноженной начисло

# --- решение системы методом Гаусса (приведением к треугольному виду)
def Gauss(A, B):
    column = 0
    while (column < len(B)):
        print("Ищем максимальный по модулю элемент в {0}-м столбце:".format(column + 1))
        current_row = None
        for r in range(column, len(A)):
            if current_row is None or abs(A[r][column]) > abs(A[current_row][column]):
                 current_row = r
        if current_row is None:
            print("решений нет")
            return None
        FancyPrint(A, B, (current_row, column))
        if current_row != column:
            print("Переставляем строку с найденным элементом повыше:")
            SwapRows(A, B, current_row, column)
            FancyPrint(A, B, (column, column))
        print("Нормализуем строку с найденным элементом:")
        DivideRow(A, B, column, A[column][column])
        FancyPrint(A, B, (column, column))
        print("Обрабатываем нижележащие строки:")
        for r in range(column + 1, len(A)):
            CombineRows(A, B, r, column, -A[r][column])
        FancyPrint(A, B, (column, column))
        column += 1
    print("Матрица приведена к треугольному виду, считаем решение")
    X = [0 for b in B]
    for i in range(len(B) - 1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))
    print("Получили ответ:")
    print("\n".join("X{0} =\t{1:10.2f}".format(i + 1, x) for i, x in
enumerate(X)))
    return X



def MNK(x , y , n , k):
    a = [[0,0,0],[0,0,0],[0,0,0]]
    b=[0,0,0]
    c=[0,0,0]
    i=0
    j=0
    for m in range(0,k):
        for j in range(0,k):
            for i in range(0, n):
               a[m][j] += var(x[i],m) * var(x[i],j)
        for i in range(0, n):
            b[m] += var(x[i],m) * y[i]

    x = Gauss(a ,b)
    return x



lmd1 = 0.001
Niter = 20
uu = -1

rr = F(uu)
x_ex = [-1.0, -0.8, -0.6 , -0.4, -0.2 , 0.0,  0.2,0.4 , 0.6,0.8, 1.0]
y_ex = [-1.14,  -0.66,  0.07,0.10  ,0.47 ,1.07 , 0.46,  0.26  ,-0.82,  -0.41 ,-1.59]
uu_v = [uu]
rr_v = [rr]

while(uu<Niter):
    uu = uu + 0.1
    rr = F(uu)
    uu_v.append(uu)
    rr_v.append(rr)

c = MNK(x_ex , y_ex , 11 , 3)
x = [1]
y = [F_mnk(1 ,c)]
for g in range(-1,Niter):
    x.append(g)
    y.append( F_mnk(g ,c))


print(c)
plt.plot(uu_v, rr_v)
plt.scatter(x_ex, y_ex, color="red")
plt.plot(x, y , color="green")
plt.xlabel("u")
plt.ylabel("r")

plt.show()

