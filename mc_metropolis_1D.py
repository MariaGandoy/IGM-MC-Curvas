import matplotlib . pyplot as plt
import numpy as np

g1 = lambda x:2*(x[0] + x[1])
f  = lambda x:np.sin(x)/2

# integral[0, pi] x * sin(x) dx

#   c = integral[0, pi] sin(x) dx = 2
#
#   integral[0, pi] (c * x) * (sin(x) / c) dx , c = 2
#   
#   g(x) = c * x
#   p(x) = sin(x) / c => 
#       
#           integral[0, pi] sin(x) / c dx = 1
#           integral[0, pi] (f(x) / c) dx = 1 , f(x) = sin(x)


a = 0
b = np.pi
nsim = 3000 # numero de puntos a generar
x = []
Ia = 0 # para aproximar la esperanza
Naceptados = 0
x0 = np.random.uniform(a, b)
x.append(x0)
for n in  range(1, nsim):
    g = np.random.uniform(-1.2, 1.2)
    xs = x0 + g
    # controlo no salirme
    if (xs < a or xs > b):
        v = np.random.uniform(0, 1)
        xs = a + (b - a) * v
    c = f(xs) / f(x0)
    A = np.minimum(1., c)
    if A == 1: # me quedo el punto
        x0 = xs
        x.append(x0)
        Naceptados += 1
        Ia += g1(x)
    elif A < 1.: # decido aleatoriamente que hacer
        u = np.random.uniform(0, 1)
        if u < A:
            x0 = xs
            x.append(x0)
            Naceptados += 1
            Ia += g1(x)

Ia /= Naceptados
print('Ia = ', Ia)
xx = np.linspace(a, b)
plt.plot(xx, f(xx))
plt.plot(x, np.zeros_like(x), 'x')
