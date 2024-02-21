import numpy as np

A = np.array(
    [[2., -1., 0., 0., 1.],
     [-1., 2., 1., 0., 0.],
     [0., 1., 1., 1., 0.],
     [0., 0., 1., 2., -1.],
     [1., 0., 0., -1., 2.]
     ]
)

eigen_val = 0.38197

def inv_iter(A, eigen_val):
    iter = 1000
    eps = 1e-5

    v = np.ones(A.shape[0])

    for i in range(iter):
        x = np.linalg.solve(A - eigen_val*np.identity(A.shape[0]), v)
        x = x / np.linalg.norm(x)

        if(np.linalg.norm(A @ x - eigen_val * x)) < eps:
            break
            
        v = x

    return x

eigen_vector = inv_iter(A, eigen_val)

for i in range((len(eigen_vector))):
    eigen_vector[i] = np.round(eigen_vector[i], 5)

print("Przybliżony wektor własny: ", eigen_vector)