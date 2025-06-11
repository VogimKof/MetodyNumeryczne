import numpy as np

def f(x, y):
    return np.array([f1(x, y), f2(x, y)])

def f1(x, y):
    return x**2 + y**2 - 4

def f2(x, y):
    return x + 2*x**2 + 3*y**2

def Jacobian(x, y):
    df1_dx = 2*x
    df1_dy = 2*y
    df2_dx = 1 + 4*x
    df2_dy = 6*y
    return np.array([
        [df1_dx, df1_dy],
        [df2_dx, df2_dy]
    ])

def Newton(eps=1e-6, max_iter=1000):

    x, y = 1.0, 1.0  
    for _ in range(max_iter):
        J = Jacobian(x, y)
        F = f(x, y)

        #J * delta = -F
        try:
            delta = np.linalg.solve(J, -F)
        except np.linalg.LinAlgError:
            print("Jacobian is singular.")
            return None

        x_new = x + delta[0]
        y_new = y + delta[1]

        if np.linalg.norm([x_new - x, y_new - y], ord=2) < eps:
            return x_new, y_new

        x, y = x_new, y_new


