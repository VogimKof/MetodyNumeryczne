import numpy as np
import math
import matplotlib.pyplot as plt

def Pszczółkowski_Mateusz_MNK(x, y, n):

    A = calc_A(x, n)
    AT = Transpose(A)
    ATA = np.matmul(AT,A)
    ATy = np.matmul(AT, y)
    
    L = Cholesky_L(ATA)
    # ATA*a = ATy - > LLTa = ATy

    # 1. L * p = ATy
    p = [0.0] * n
    for row in range(n):
        temp = ATy[row]
        for col in range(row):
            temp -= L[row][col] * p[col]
        p[row] = temp / L[row][row]

    # 2. LT * a = p
    LT = Transpose(L)
    a = [0.0] * n
    for row in range(n-1, -1, -1):
        temp = p[row]
        for col in range(row+1, n):
            temp -= LT[row][col] * a[col]
        a[row] = temp / LT[row][row]

    plt.plot(x, y, 'o', label="Węzły")
    X = np.linspace(min(x) - 0.1, max(x) + 0.1, 1000)
    plt.plot(X, wielomian(a, X), label="Wielomian")
    plt.grid(True)
    plt.legend()
    plt.show()

    return a

def wielomian(a, x):
    return sum(a[i] * x**i for i in range(len(a)))

def calc_A(x, n):
    A = [[0.0] * n for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(n):
            A[i][j] = x[i] ** j
    return A

def Cholesky_L(ATA):
    n = len(ATA)
    L = [[0.0] * n for _ in range(n)]
    for col in range(n):
        for row in range(col, n):
            temp = ATA[row][col]
            for i in range(col):
                temp -= L[row][i] * L[col][i]
            if row == col:
                L[row][col] = math.sqrt(temp)
            else:
                L[row][col] = temp / L[col][col]
    return L

def Transpose(A):
    cols = len(A[0])
    rows = len(A)
    AT = [[0.0] * rows for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            AT[col][row] = A[row][col]
    return AT


