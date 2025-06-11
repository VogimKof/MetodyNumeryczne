
def Gauss(A, b):

    n= len(A)

    for i in range(n): # wiersz
        for j in range(i+1, n): #kolejne wiersze
            m = A[j][i] / A[i][i] # mnoznik
            b[j] = b[j] - b[i]*m

            for k in range(i, n) : # wybór kolumny od której odejmuje
                A[j][k] = A[j][k] - A[i][k] * m

A = [[1, 2, 3],
    [4, 5, 6],
    [7, 8 ,5]]

b = [1, 2, 3]

Gauss(A, b)
print(A)
print(b)







