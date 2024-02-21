import numpy as np


EPSILON = 1e-06
max_iter = 100

f = np.poly1d([1/4, 0, -1/2, -1/16, 0])

def narrow(a, b, c, d, f):
    if f(d) < f(b):
        if d < b:
            c = b
            b = d
        else:
            a = b
            b = d
    else:
        if d < b:
            a = d
        else:
            c = d
    return a, b, c, d

def golden_ratio(a, b, c, f):
    w = (3 - np.sqrt(5)) / 2
    b_old = b
    for i in range(max_iter):
        if np.abs(c - b) > np.abs(b - a):
            d = b + w * np.abs(c - b)
        else:
            d = b - w * np.abs(b - a)
        a, b, c, _ = narrow(a, b, c, d, f)

        if (np.abs(c - a) - EPSILON * (np.abs(b_old) + np.abs(d))) < EPSILON:
            break
        
    return d, i + 1

def brent_method(a, b, c, f):
    b_old = b
    for i in range(max_iter):
        nom = a**2 * (f(c) - f(b)) + b**2 * (f(a) - f(c)) + c**2 * (f(b) - f(a))
        denom = 2 * (a * (f(c) - f(b)) + b * (f(a) - f(c)) + c * (f(b) - f(a)))
        d = nom / denom
        if d < c and d > a:
            a, b, c, d = narrow(a, b, c, d, f)
        else:
            d = (a + c) / 2
            a, b, c, d = narrow(a, b, c, d, f)

        if (np.abs(c - a) - EPSILON * (np.abs(b_old) + np.abs(d))) < EPSILON:
            break
    return d, i + 1


a = -1.4
b = -1.1
c = -0.9

golden_ratio_min, golden_ratio_iter = golden_ratio(a, b, c, f)
brent_method_min, brent_method_iter = brent_method(a, b, c, f)

print(f"Golden ratio: {golden_ratio_min}, iter: {golden_ratio_iter}")
print(f"Brent method: {brent_method_min}, iter: {brent_method_iter}")