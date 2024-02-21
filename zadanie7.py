import numpy as np
import matplotlib.pyplot as plt

x = np.array([-0.75, -0.50, -0.25, 0.00, 0.25, 0.50, 0.75, 1.])
fx = np.array([1.1309204101562500, 2.3203125000000000, 1.9284057617187500,
1., 0.0554809570312500, -0.6015625000000000, -0.7525024414062500, 0.])

def l2(x, j):
    denom = 1
    for i in range(x.shape[0]):
        if i != j:
            denom *= (x[j] - x[i])
    return denom

def l1(x, j):
    poly = np.poly1d([1])
    for i in range(x.shape[0]):
        if i != j:
            poly *= np.poly1d([1, -x[i]])
    nom = np.array([a for a in poly])
    return nom

def Lagrange(x, f):
    l = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        l += (f[i] * l1(x, i) / l2(x, i))
    return l

coef = Lagrange(x, fx)

for c in range(len(coef)):
    coef[c] = np.round(coef[c], 12)

x_range = np.linspace(-1.25, 1.25, 100)

y = np.polyval(coef, x_range)

fig = plt.figure(figsize = (10, 5))

plt.plot(x_range, y, label = "polynomial")
plt.scatter(x, fx, color = 'r', label = "points")

plt.legend()
plt.show()