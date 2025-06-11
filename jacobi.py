import numpy as np

A = [[5, 1, 2],
    [-2, 6 ,-3],
    [2, 2, 4]]

b = [3,4,1]

def Jacobi(A, b, epsilon):
    n = len(A)
    x = [1] * n

    while True:
        x_next = [1] * n

        print(x, x_next)
        for i in range(n):
            res= b[i]
            for j in range(n):
                if j != i:
                    res -= A[i][j] * x[j]

            res /= A[i][i]

            x[i] = res

        if abs(np.linalg.norm(x)-np.linalg.norm(x_next)) < epsilon:
            return False
        x = x_next

print(Jacobi(A,b, 0.02))