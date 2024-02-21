import numpy as np
import math
EPSILON = 1e-7

def find_A():
    for a in range(10000):
        if math.exp(-a) < EPSILON:
            return a
    return 0
def f(x):
    return math.exp(-x) * math.sin((np.pi * (1 + np.sqrt(x))/(1 + x**2)))

def trapezoidal(a, b, e):
    h = (b - a) / e
    integral = f(a) + f(b)
    for i in range(1, e):
        integral += 2 * f(a + i * h)

    return integral * h / 2

def romberg(a, b, l = 100):
    A = np.zeros((l, l))
    for i in range(l):
        A[i, 0] = trapezoidal(a, b, 2**i)
        for j in range(1, i + 1):
            A[i, j] = (4**j * A[i, j - 1] - A[i - 1, j - 1]) / (4**j - 1)

        if abs(A[i, i] - A[i - 1, i - 1]) < EPSILON and i != 0:
            return A[i, i]
        
    return A[l - 1, l - 1]

A = find_A()
print(trapezoidal(0, A, 10000))
r = romberg(0, A)
print(r)