# f(x) = -12*x**4*sin(cos(x)) -18*x**3 + 5*x**2 + 10*x - 30
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

import numpy as np
import matplotlib.pyplot as plt

limit = 100
step = 0.01

a, b, c, d, e = -12, -18, 5, 10, -30

x = np.arange(-limit, limit, step)
def func(x):
    return a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e

plt.plot(x, func(x), 'b')
plt.show()