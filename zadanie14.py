import numpy as np
import matplotlib.pyplot as plt

EPSILON = 1e-06
max_iter = 1000

def f1(x, y):
    return 2*x**2 + y**2 - 2

def f2(x, y):
    return (x - 1/2)**2 + (y - 1)**2 - 1/4

def f1x(x, y):
    return 4*x

def f1y(x, y):
    return 2*y

def f2x(x, y):
    return 2*x - 1

def f2y(x, y):
    return 2*y - 2

def jacobian(x, y):
    J = np.zeros((2, 2))
    J[0, 0] = f1x(x, y)
    J[0, 1] = f1y(x, y)
    J[1, 0] = f2x(x, y)
    J[1, 1] = f2y(x, y)

    return J

def newton(x, y):
    for i in range(max_iter):
        J = jacobian(x, y)
        F = np.array([f1(x, y), f2(x, y)])
        d = np.linalg.solve(J, F)
        x -= d[0]
        y -= d[1]
        if np.linalg.norm(d) < EPSILON or np.linalg.norm(F) < EPSILON:
            return x, y, i + 1
    return x, y, i + 1

x1, y1, i1 = newton(0, 1)
x2, y2, i2 = newton(1, 0)

print(x1, y1, i1)
print(x2, y2, i2)

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)

X, Y = np.meshgrid(x, y)

Z1 = f1(X, Y)
Z2 = f2(X, Y)
plt.scatter(x1, y1, color='black', s=20, alpha=1, label=f'{x1, y1}', zorder=2)
plt.scatter(x2, y2, color='black', s=20, alpha=1, label=f'{x2, y2}',zorder=2)
plt.contour(X, Y, Z1, [0], alpha = 0.8, colors = 'red',zorder=1)
plt.contour(X, Y, Z2, [0], alpha =0.8, colors = 'blue',zorder=1)

plt.legend()
plt.show()