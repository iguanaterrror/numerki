import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_fwf('dane.txt')
dane.to_csv('dane.csv', index=False)
dane.columns = ['x', 'y']

x = dane['x'].to_numpy()
y = dane['y'].to_numpy()

#sprawdzam czy wezly sa rownoodlegle
h = np.abs(x[0] - x[1])
for i in range (len(x) - 1):
    if np.abs(x[i] - x[i + 1]) - h > 1e-6:
        print('wezly nie sa rownoodlegle')  
        break
    else:
        print('wezly sa rownoodlegle')
        break  

def A(xj, xj1):
    nom = np.poly1d([-1, xj1])
    denom = xj1 - xj
    return nom/denom

def B(xj, xj1):
    nom = np.poly1d([1, -xj])
    denom = xj1 - xj
    return nom/denom

def C(xj, xj1):
    a = A(xj, xj1)
    c = ((a**3 - a)*(xj1 - xj)**2)/6
    return c

def D(xj, xj1):
    b = B(xj, xj1)
    d = ((b**3 - b)*(xj1 - xj)**2)/6
    return d

def thomas(a, b, c, d):
    n = len(d)
    
    gamma, delta = [], []

    gamma.append(c[0]/b[0])
    delta.append(d[0]/b[0])

    for i in range(1, n):
        gamma.append(c[i] / (b[i] - a[i] * gamma[i - 1]))
        delta.append((d[i] - a[i] * delta[i - 1])/(b[i] - a[i] * gamma[i - 1]))


    
    x = np.zeros(n)
    x[-1] = delta[-1]
    for i in range(n - 2, -1, -1):
        x[i] = delta[i] - gamma[i] * x[i+1]

    return x

def zeta(x, f):
    h = x[1] - x[0]
    n = x.shape[0] - 2

    d = np.zeros(n)

    z = np.array([0])
    a, b, c = np.zeros(n), np.zeros(n), np.zeros(n)
    a[0] = 0
    for i in range(0, n):
        a[i - 1] = 1 
        b[i] = 4
        c[i] = 1

    c[n - 1] = 0

    m = 6/(h**2)

    for i in range(n):
        v = f[i] - 2 * f[i + 1] + f[i + 2]
        d[i] = m * v
    sol = thomas(a, b, c, d)
    z = np.append(z, sol)
    z = np.append(z, [0])

    return z

def spline(x, f, z):
    poly = []

    for i in range(x.shape[0]-1):
        yj = A(x[i], x[i+1]) * f[i] + B(x[i], x[i+1]) * f[i+1] + C(x[i], x[i+1]) * z[i] + D(x[i], x[i+1]) * z[i+1]
        poly.append(yj)
    return poly

z = zeta(x, y)

poly = spline(x, y, z)
plt.figure(figsize=(20, 20))
plt.scatter(x, y, color = 'black',s = 10, alpha=0.5, label = 'points', zorder=10)
for i in range(x.shape[0] - 1):
    r = np.linspace(x[i], x[i+1], 1000)
    plt.plot(r, poly[i](r), zorder=0)
plt.legend()
plt.show()