'''
Calculo das integrais de caminho para um oscilador harmonico
utilizando um algoritmo de cadeia de Markov
'''


import numpy as np

def en_free(n, L):
    return 2.*n*n(np.pi**2)/(L*L)

def rho_free(beta, n, L, x1, x2):
    rho = np.zeros(n)
    _temp1 = .0
    _temp2 = .0
    for iter in range(n):
        _temp1 = np.exp(2j*np.pi*iter*(x1 - x2)/L)
        _temp2 = np.exp(-(beta*2.*n*n*(np.pi**2))/(L*L))
        rho[iter] = _temp1 * _temp2
    return np.sum(rho)

N = 8
beta = 4
mc_iter = 10**6
delta = 0.1
num_points = 20

xi = -2.0
xf = 2.0

path = np.arange(xi, xf, N-1)
path2 = np.arange(xi, xf, N-1)

L = np.linspace(xi, xf, num_points)

k = np.random.randint(0, N-1)
kp = k + 1
km = k -1

if km == -1:
    km = N

path2[k] = path[k] + np.random.rand(-delta, delta)
