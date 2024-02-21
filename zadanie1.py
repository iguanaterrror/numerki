import numpy as np

A = np.array(
    [
    [3,1,0,0,0,0,0],
    [1,4,1,0,0,0,0],
    [0,1,4,1,0,0,0],
    [0,0,1,4,1,0,0],
    [0,0,0,1,4,1,0],
    [0,0,0,0,1,4,1],
    [0,0,0,0,0,1,3]
    ]
)
B = np.array(
    [
    [4,1,0,0,0,0,1],
    [1,4,1,0,0,0,0],
    [0,1,4,1,0,0,0],
    [0,0,1,4,1,0,0],
    [0,0,0,1,4,1,0],
    [0,0,0,0,1,4,1],
    [1,0,0,0,0,1,4]
    ]
)

X = np.array([1, 2, 3, 4, 5, 6, 7])

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


def sherman_morrison(a, b, c, d, u):
    z = thomas(a, b, c, d)
    q = thomas(a, b, c, u)
    w = z - (np.dot((np.dot(u.T, z)), q)) / (1 + np.dot(u.T, q))

    return w


#rowziazywanie macierzy A
a = A.diagonal(-1)
b = A.diagonal()
c = A.diagonal(1)

a = np.append(np.array([0]), a, axis = 0)
c = np.append(c, np.array([0]))

sol_1 = thomas(a, b, c, X)

#rozwiazywanie macierzy B
u = np.fliplr(B).diagonal().T
u = np.copy(u)
u[3] = 0
u = u.T

sol_2 = sherman_morrison(a, b, c, X, u)

for i in range(7):
    sol_1[i] = np.round(sol_1[i], 10)
    sol_2[i] = np.round(sol_2[i], 10)

print('Rozwiązania macierzy A')
for i in range(7):
    print(f'x{i + 1} = {sol_1[i]}')

print('Rozwiązania macierzy B')
for i in range(7):
    print(f'x{i + 1} = {sol_2[i]}')