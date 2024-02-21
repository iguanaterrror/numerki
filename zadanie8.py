import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as polyn
import numpy as np

x = np.array([-7/8, -5/8, -3/8, -1/8, 1/8, 3/8, 5/8, 7/8])

f = np.zeros(x.shape[0])

for i in range(x.shape[0]):
    f[i] = 1/(1 + 5 * x[i]**2)

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

coef = Lagrange(x, f)
for c in range(len(coef)):
    coef[c] = np.round(coef[c], 12)
    
coef = np.flip(coef)
poly = polyn.Polynomial(coef)

range = np.linspace(-1, 1, 1000)

plt.plot(range, poly(range), label = 'polynomial')
plt.scatter(x, f, color='r', label='points')

plt.legend()
plt.show()