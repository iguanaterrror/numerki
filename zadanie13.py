import numpy as np

EPSILON = 1e-6

def deflation(p, x):
    p, _ = p / np.poly1d([1, -x])
    return p

def laguerre(p, z = 1 + 1j, max_iter = 10000):
    n = len(p) + 1

    for _ in range(max_iter):
        nom = n * np.polyval(p, z)
        denom1 = np.polyval(np.polyder(p), z)
        der1 = np.polyder(p)
        der2 = np.polyder(der1)
        denom2 = np.sqrt((n - 1) * ((n - 1) * np.polyval(der1, z)**2 - n *np.polyval(p, z) * np.polyval(der2,z)))
        if np.abs(denom1 + denom2) > np.abs(denom1 - denom2):
            zk = z - (nom / (denom1 + denom2))
            
        elif np.abs(denom1 - denom2) > np.abs(denom1 + denom2):
            zk = z - (nom / (denom1 - denom2))
           
        else:
            break
        
        if np.abs(zk - z) < EPSILON:
                return zk
        z = zk
       
def solve(p):
    roots = np.zeros(len(p), dtype=np.complex128)
    roots[0] = laguerre(p)
    old_p = p
    for i in range(1, len(p)):
        new_p = deflation(old_p, roots[i - 1])
        temp_z = laguerre(new_p)
        roots[i] = laguerre(p, temp_z)
        old_p = new_p

    return roots
    
      

a = np.poly1d([243, -486, 783, -990, 558, -28, -72, 16])
b = np.poly1d([1, 1, 3, 2, -1, -3, -11, -8, -12, -4, -4])
c = np.poly1d([1, 1j, -1, -1j, 1])

a_poly = np.poly1d(a)
b_poly = np.poly1d(b)
c_poly = np.poly1d(c)

a_roots = solve(a)
b_roots = solve(b)
c_roots = solve(c)

print('Wielomian a: \n', a)
print('Miejsca zerowe: \n')
for root in a_roots:
    print(f"{np.round(root, 6)}")

print('\nWielomian b: \n', b)
print('Miejsca zerowe: \n')
for root in b_roots:
    print(f"{np.round(root, 6)}")

print('\nWielomian c: \n', c)
print('Miejsca zerowe: \n')
for root in c_roots:
    print(f"{np.round(root, 5)}")