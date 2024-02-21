import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

#węzły są równoodległe
def w(x_nodes, d):
    n = x_nodes.shape[0]
    w = np.zeros(n+1)
    for k in range(n+1):
        J_k = range(max(0, k-d), min(n, k+d)+1)
        w[k] = (-1)**(k-d) * sum(sp.comb(d , k - i) for i in J_k)
    return w
def floater_hormann(x_nodes, f, d, x):
    n = x_nodes.shape[0]
   
    wk = w(x_nodes, d)
    def r(x):
        nom = sum(wk[k] * f[k] / (x - x_nodes[k]) for k in range(n))
        denom = sum(wk[k] / (x - x_nodes[k]) for k in range(n))         
        return nom / denom
    
    for i in range(n):
        if np.isclose(x, x_nodes[i], atol=1e-08):
            return f[i]
        
    return r(x)

x_nodes = np.array([-7/8, -5/8, -3/8, -1/8, 1/8, 3/8, 5/8, 7/8])

f = np.zeros(x_nodes.shape[0])

for i in range(x_nodes.shape[0]):
    f[i] = 1/(1 + 5 * x_nodes[i]**2)

x_range = np.linspace(-1, 1, 1000)
y = []
for x in x_range:
    y.append(floater_hormann(x_nodes, f, 3, x))

plt.plot(x_range, y, color = 'g', label='floater hormann')
plt.scatter(x_nodes, f, label = 'points')
plt.legend()
plt.show()