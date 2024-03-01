import matplotlib . pyplot as plt
import numpy as np


# integral[0, pi/2] integral[0, 1] cos(x + y) e^x dx dy


# case 1:
#   c = integral[0, pi/2] integral[0, 1] e^x dx dy
#
#   integral[0, pi/2] integral[0, 1] c * cos(x + y) * (e^x / c) dx dy
#   
#   g(x, y) = c * cos(x + y)
#   p(x) = (e^x / c) => 
#       
#           integral[0, pi/2] integral[0, 1] (e^x / c) dx dy = 1
#           integral[0, pi/2] integral[0, 1] (f(x) / c) dx dy = 1 , f(x) = e^x

g1  = lambda x, y, c:np.cos((x[0] + x[1]) + (y[0] + y[1])) * c
f   = lambda x, c: np.exp(x) / c

a = [0, 0]
b = [(np.pi / 2), 1]
nsim = 1550 # numero de puntos a generar
x = []
y = []
Ia = 0 # para aproximar la esperanza
Naceptados = 0
x0 = np.random.uniform(a[0], b[0])
y0 = np.random.uniform(a[1], b[1])
x.append(x0)
y.append(y0)
for n in range(1, nsim):
    gx = np.random.uniform(-1.2, 1.2)
    gy = np.random.uniform(-1.2, 1.2)
    xs = x0 + gx
    ys = y0 + gy
    # controlo no salirme
    if (xs < a[0] or xs > b[0] or ys < a[1] or ys > b[1]):
        v = [np.random.uniform(0, 1), np.random.uniform(0, 1)]
        xs = a + (b - a) * v
    mc = montecarloCrudo()
    c = [f(xs, mc) / f(x0, mc), f(ys, mc) / f(x0, mc)]
    A = np.minimum(1., c)
    if A[0] == 1 and A[1] == 1:
        x0 = xs
        x.append(x0)
        Naceptados += 1
        Ia += g1(x, y, mc)
    elif A[0] < 1. or A[1] < 1.:
        u = [np.random.uniform(0, 1), np.random.uniform(0, 1)]
        if u[0] < A[0] and u[1] < A[1]:
            x0 = xs
            y0 = ys
            x.append(x0)
            y.append(y0)
            Naceptados += 1
            Ia += g1(x, y, mc)
Ia /= Naceptados
print('Ia = ', Ia)
# xx = np.linspace(a, b)
# plt.plot(xx, f(xx))
# plt.plot(x, np.zeros_like(x), 'x')


#
# case 2:
#   c = integral[0, pi/2] integral[0, 1] cos(x + y) dx dy
#
#   integral[0, pi/2] integral[0, 1] (cos(x + y) / c) * (c * e^x) dx dy
#   
#   g(x) = c * e^x
#   p(x, y) = (cos(x + y) / c) => 
#       
#           integral[0, pi/2] integral[0, 1] (cos(x + y) / c) dx dy = 1
#           integral[0, pi/2] integral[0, 1] (f(x, y) / c) dx dy = 1 , f(x, y) = cos(x + y)

g1  = lambda x, y, c:np.exp(x[0] + x[1]) * c
f   = lambda x, y, c: np.cos(x, y) / c

a = [0, 0]
b = [(np.pi / 2), 1]
nsim = 1550 # numero de puntos a generar
x = []
y = []
Ia = 0 # para aproximar la esperanza
Naceptados = 0
x0 = np.random.uniform(a[0], b[0])
y0 = np.random.uniform(a[1], b[1])
x.append(x0)
y.append(y0)
for n in range(1, nsim):
    gx = np.random.uniform(-1.2, 1.2)
    gy = np.random.uniform(-1.2, 1.2)
    xs = x0 + gx
    ys = y0 + gy
    # controlo no salirme
    if (xs < a[0] or xs > b[0] or ys < a[1] or ys > b[1]):
        v = [np.random.uniform(0, 1), np.random.uniform(0, 1)]
        xs = a + (b - a) * v
    mc = montecarloCrudo()
    c = [f(xs, mc) / f(x0, mc), f(ys, mc) / f(x0, mc)]
    A = np.minimum(1., c)
    if A[0] == 1 and A[1] == 1:
        x0 = xs
        x.append(x0)
        Naceptados += 1
        Ia += g1(x, y, mc)
    elif A[0] < 1. or A[1] < 1.:
        u = [np.random.uniform(0, 1), np.random.uniform(0, 1)]
        if u[0] < A[0] and u[1] < A[1]:
            x0 = xs
            y0 = ys
            x.append(x0)
            y.append(y0)
            Naceptados += 1
            Ia += g1(x, y, mc)
Ia /= Naceptados
print('Ia = ', Ia)
# xx = np.linspace(a, b)
# plt.plot(xx, f(xx))
# plt.plot(x, np.zeros_like(x), 'x')
