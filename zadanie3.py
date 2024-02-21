import numpy as np

A = np.array(
        [
            [19/12, 13/12, 5/6, 5/6, 13/12, -17/12],
            [13/12, 13/12, 5/6, 5/6, -11/12, 13/12],
            [5/6,   5/6,   5/6, -1/6, 5/6,   5/6],
            [5/6,   5/6,   -1/6, 5/6, 5/6,   5/6],
            [13/12, -11/12, 5/6, 5/6, 13/12, 13/12],
            [-17/12, 13/12, 5/6, 5/6, 13/12, 19/12]
        ]
    )


def power_iteration(A):
    iter = 2500
    eps = 1e-12
    n = A.shape[0]
    eigenValues = []
    eigenVectors = np.zeros((n,n))
    for x in range(n):
        V = np.random.rand(A.shape[0])
        V = V/np.linalg.norm(V)

        for i in range(iter):
            AV = np.dot(A, V)
            e_Value = np.dot(V.T, AV)
            V = AV/np.linalg.norm(AV)

            if np.linalg.norm(AV - e_Value * V) < eps:
                print(i)
                break

        eigenValues.append(e_Value)
        eigenVectors[:,x] = V

        A -= e_Value * np.outer(V, V)

    
    return eigenValues, eigenVectors

Values , Vectors = power_iteration(A)

for i in range(len(Values)):
    Values[i] = np.round(Values[i], 4)

for i in range(Vectors.shape[0]):
    Vectors[i] = np.round(Vectors[i], 6)

sorted_Values = np.zeros(A.shape[0])
sorted_Vectors = np.zeros((A.shape[0], A.shape[0]))
sorted = np.argsort(Values)[::-1]
sorted_Values = np.array(Values)[sorted.astype(int)]
sorted_Vectors = np.array(Vectors)[:, sorted.astype(int)]


for i in range(2):
    print(f"najwieksza wartosc wlasna {i+1}: {sorted_Values[i]}")
    print(f"odpowiadajacy jej wektor: ")
    print(sorted_Vectors[:, i])
    print()