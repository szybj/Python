# -*- coding:utf-8 -*-

def square_of_sum(list):
    sum = 0
    for l in list:
        sum += l * l
    return sum

print square_of_sum([-1, 3])

import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print x, y

import math
def quadratic_equation(a, b, c):
    t = math.sqrt(b * b - 4 * a * c)
    return (-b + t) / (2 * a), (-b - t) / (2 * a)

print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print fact(1)
print fact(5)
print fact(100)


def hanoi (n, a, b, c):
    if n == 1:
        print a, '===>', c
    else:
        hanoi(n - 1, a, c, b)
        print a, '===>', c
        hanoi(n - 1, b, a, c)

hanoi(4, 'A', 'B', 'C')

print int('123', 8)

def greet(name = 'World'):
    return 'Hello,' + name

print greet()

def fn(*args):
    print args

fn()
fn('a')
fn('f', 3)

def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    for i  in args:
        sum = sum + i
    return sum / len(args)

print average()
print average(1, 3, 4, 20)
print average(2, 4, 3, 1)