# Дана функция f(x) = 5*x**2 + 10*x - 30
# 4. Построить график
# 1. Определить корни
# 5. Вычислить вершину
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0
# import numpy as np
# import matplotlib.pyplot as plt

# limit = 10
# step = 0.01

# a, b, c =5, 10, -30
# x = np.arange(-limit, limit, step)
# def func(x):
#     return a*x**2+b*x+c
# def take_roots(a, b, c):
#     discr = b**2-4*a*c
#     if discr > 0:
#         x1 = (-b + discr**0.5)/(2*a)
#         x2 = (-b - discr**0.5)/(2*a)
#         return x1, x2
#     elif discr == 0:
#         x = -b/(2*a)
#         return x, x
#     else:
#         return None, None
# roots = take_roots(a, b, c)
# min_y = min(func(x))
# min_x = take_roots(a, b, c - min_y)[0]
# x_down_pos = np.arange(-limit, min(roots), step)
# x_down_neg = np.arange(min(roots), min_x, step)
# x_up_neg = np.arange(min_x, max(roots), step)
# x_up_pos = np.arange(max(roots), limit, step)

# plt.rcParams['lines.linestyle'] = '-'
# plt.plot(x_down_pos, func(x_down_pos), 'r', label = 'Убывание выше 0')
# plt.plot(x_up_pos, func(x_up_pos), 'b', label = 'Возрастание выше 0')
# plt.rcParams['lines.linestyle'] = '--'
# plt.plot(x_down_neg, func(x_down_neg), 'r', label = 'Убывание ниже 0')
# plt.plot(x_up_neg, func(x_up_neg), 'b', label = 'Возрастание ниже 0')
# plt.plot(roots[0], func(roots[0]), 'go', label = f'Корни ({round(min(roots)), 2}, {round(max(roots)), 2})')
# plt.plot(roots[1], func(roots[1]), 'go')
# plt.plot(min_x, min_y, 'cx', label = f'Экстремум ({min_x}, {min_y})')
# plt.grid()
# plt.legend()


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
