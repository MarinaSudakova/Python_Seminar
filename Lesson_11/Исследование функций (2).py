# -*- coding: utf-8 -*-

# -- Семинар --

from sympy import *
from sympy.plotting import plot
init_printing()


# 1. Определить корни
#    Нули функции

x = Symbol('x')
f = 5 * x**2 + 10 * x - 30
a = plot(f, (x, -5, 2.5))

solveset(f, x)

# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает

b = [-oo, oo]
b[1:1] = solve(diff(f, x))
b

c = []
d = []
for i in range(1, len(b)):
    boo = is_increasing(f, Interval.open(b[i-1], b[i]))
    if boo:
        c.append(f'{b[i-1]} {b[i]}')
    else:
        d.append(f'{b[i-1]} {b[i]}')

print(c)
print(d)

# 5. Вычислить вершину
#    Экстремумы функции

e = solve(diff(f), x)
for i in e:
    g = f.subs(x, i)
    if g < 0:
        print(f'Minimum: x{i} y{g}')
    elif g > 0:
        print(f'Maximum: x{i} y{g}')


# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0
#    Знакопостоянства функции

m = [-oo, oo]

h = []
l = []
m[1:1] = solve(f, x)
for i in range(1, len(m)):
    boo = is_increasing(f, Interval.open(m[i-1], m[i]))
    if boo:
        h.append(f'{m[i-1]}, {m[i]}')
    else:
        l.append(f'{m[i-1]}, {m[i]}')

print("f > 0:", *h, sep="\n")
print("f < 0:", *l, sep="\n")

from sympy import *
from sympy.plotting import plot
init_printing()


# 1. Определить корни
#    Нули функции

x = Symbol('x')
f = 5 * x**2 + 10 * x - 30
a = plot(f, (x, -5, 2.5))

solveset(f, x)

# -- Задача 1 --

from sympy import *
from sympy.plotting import plot


#Построить график функции

x = Symbol('x')
f = -18 * x ** 3 + 5 * x ** 2 + 10 * x - 30
a = plot(f, (x, -5, 5))

# 1. Определить корни
#    Нули функции

solveset(f, x)

# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает

b = [-oo, oo]
b[1:1] = solve(diff(f, x))
b

c = []
d = []
for i in range(1, len(b)):
    boo = is_increasing(f, Interval.open(b[i-1], b[i]))
    if boo:
        c.append(f'{b[i-1]} {b[i]}')
    else:
        d.append(f'{b[i-1]} {b[i]}')

print(c)
print(d)

# 5. Вычислить вершину
#    Экстремумы функции

from random import uniform

f_diff = sorted(solveset(diff(f), x, Reals).evalf(2))
f_diff.insert(0, f_diff[0] - 1)
f_1 = diff(f)

ext_list = []

for i, val in enumerate(f_diff):
    ext_list.append(f_1.subs(x, uniform(val, f_diff[i] + 1)))
    if i != 0:
        if ext_list[i - 1] < 0 < ext_list[i]:
            print(f"Точка минимума: {val}, {f.subs(x, val).evalf(2)}")
        elif ext_list[i - 1] > 0 > ext_list[i]:
            print(f"Точка максимума: {val}, {f.subs(x, val).evalf(2)}")

# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0

m = [-oo, oo]

h = []
l = []
m[1:1] = solve(f, x)
for i in range(1, len(m)):
    boo = is_increasing(f, Interval.open(m[i-1], m[i]))
    if boo:
        h.append(f'{m[i-1]}, {m[i]}')
    else:
        l.append(f'{m[i-1]}, {m[i]}')

print("f > 0:", *h, sep="\n")
print("f < 0:", *l, sep="\n")

# -- Задача 2 --

from sympy import *
from sympy.plotting import plot


#Построить график функции

x = Symbol('x')
f = 2 * x ** 3 + 2 * x ** 2 - 18 * x - 18
a = plot(f, (x, -5, 5))

# 1. Определить корни
#    Нули функции

solveset(f, x)

# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает

b = [-oo, oo]
b[1:1] = solve(diff(f, x))
b

c = []
d = []
for i in range(1, len(b)):
    boo = is_increasing(f, Interval.open(b[i-1], b[i]))
    if boo:
        c.append(f'{b[i-1]} {b[i]}')
    else:
        d.append(f'{b[i-1]} {b[i]}')

print(c)
print(d)

# 5. Вычислить вершину
#    Экстремумы функции

from random import uniform

f_diff = sorted(solveset(diff(f), x, Reals).evalf(2))
f_diff.insert(0, f_diff[0] - 1)
f_1 = diff(f)

ext_list = []

for i, val in enumerate(f_diff):
    ext_list.append(f_1.subs(x, uniform(val, f_diff[i] + 1)))
    if i != 0:
        if ext_list[i - 1] < 0 < ext_list[i]:
            print(f"Точка минимума: {val}, {f.subs(x, val).evalf(2)}")
        elif ext_list[i - 1] > 0 > ext_list[i]:
            print(f"Точка максимума: {val}, {f.subs(x, val).evalf(2)}")

# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0

m = [-oo, oo]

h = []
l = []
m[1:1] = solve(f, x)
for i in range(1, len(m)):
    boo = is_increasing(f, Interval.open(m[i-1], m[i]))
    if boo:
        h.append(f'{m[i-1]}, {m[i]}')
    else:
        l.append(f'{m[i-1]}, {m[i]}')

print("f > 0:", *h, sep="\n")
print("f < 0:", *l, sep="\n")

# -- Задача 3 --

from sympy import *
from sympy.plotting import plot


#Построить график функции

x = Symbol('x')
f = (x ** 2 + 3) / (3 * (x + 1))
a = plot(f, (x, -10, 10))

# 1. Определить корни
#    Нули функции

solveset(f, x)

# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает

b = [-oo, oo]
b[1:1] = solve(diff(f, x))
b

c = []
d = []
for i in range(1, len(b)):
    boo = is_increasing(f, Interval.open(b[i-1], b[i]))
    if boo:
        c.append(f'{b[i-1]} {b[i]}')
    else:
        d.append(f'{b[i-1]} {b[i]}')

print(c)
print(d)

# 5. Вычислить вершину
#    Экстремумы функции

from random import uniform

f_diff = sorted(solveset(diff(f), x, Reals).evalf(2))
f_diff.insert(0, f_diff[0] - 1)
f_1 = diff(f)

ext_list = []

for i, val in enumerate(f_diff):
    ext_list.append(f_1.subs(x, uniform(val, f_diff[i] + 1)))
    if i != 0:
        if ext_list[i - 1] < 0 < ext_list[i]:
            print(f"Точка минимума: {val}, {f.subs(x, val).evalf(2)}")
        elif ext_list[i - 1] > 0 > ext_list[i]:
            print(f"Точка максимума: {val}, {f.subs(x, val).evalf(2)}")

