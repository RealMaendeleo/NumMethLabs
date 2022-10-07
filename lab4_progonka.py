import numpy as np

def Sweep():
    ''' [2, 1, 0, 0, 0, 0, 0],  
        [1, 3, 1, 0, 0, 0, 0],  
        [0, 2, 5, 2, 0, 0, 0],  
        [0, 0, 3, 7, 3, 0, 0],  
        [0, 0, 0, 2, 5, 2, 0],  
        [0, 0, 0, 0, 1, 3, 1],  
        [0, 0, 0, 0, 0, 1, 2] 
        
        [  4],
        [ 10],
        [ 27],
        [ 46],
        [ 27],
        [ 10],
        [  4]
         '''

    matrix = np.array([
        [-1,  1,  0,  0,  0,  0 ],
        [-7, -2,  5,  0,  0,  0 ],
        [ 0, -6,  5,  4,  0,  0 ],
        [ 0,  0,  1,  6, -1,  0 ],
        [ 0,  0,  0,  6,  5, -6 ],
        [ 0,  0,  0,  0,  2,  8 ]
    ], np.float_)

    a = np.array([
        [-1,  1,  0,  0,  0,  0 ],
        [-7, -2,  5,  0,  0,  0 ],
        [ 0, -6,  5,  4,  0,  0 ],
        [ 0,  0,  1,  6, -1,  0 ],
        [ 0,  0,  0,  6,  5, -6 ],
        [ 0,  0,  0,  0,  2,  8 ]
    ], np.float_)

    matrix2 = np.array([
        [  2 ],
        [-69 ],
        [-38 ],
        [ 26 ],
        [ 66 ],
        [ 12 ]
    ], np.float_)

    b = np.array([
        [  2 ],
        [-69 ],
        [-38 ],
        [ 26 ],
        [ 66 ],
        [ 12 ]
    ], np.float_)

    n = len(matrix)
    A = np.array([0] * n, np.float_)
    B = np.array([0] * n, np.float_)
    Xs = np.array([0] * n, np.float_)

    A[0] = -matrix[0][1] / matrix[0][0]
    B[0] = matrix2[0] / matrix[0][0]

    for i in range(1, n-1):
        E = matrix[i][i-1] * A[i-1] + matrix[i][i]
        A[i] = -matrix[i][i+1] / E
        B[i] = (matrix2[i] - matrix[i][i-1] * B[i-1]) / E

    Xs[n-1] = (matrix2[n-1] - matrix[n-1][n-2] * B[n-2]) / (matrix[n-1][n-1] + matrix[n-1][n-2] * A[n-2])
    for i in range(n-2, -1, -1):
        Xs[i] = A[i] * Xs[i+1] + B[i]
    print(Xs)

    row_res = 0
    for i in range(n):
        for j in range(n):
            row_res += a[i][j] * Xs[j]
        print(row_res, " = ", b[i])
        row_res = 0
        


Sweep()