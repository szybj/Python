print abs(-90)
print abs
a = abs
print a(-90)
abs = len
# print abs(-8)
print abs([1,2,3])

import math
def add (x, y, f): 
    return f(x) + f(y)
print add(3, -9, abs)
print add(25, 9, math.sqrt)

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def f(x):
    return x * x
print map(f, L)
print L

N = ['adam', 'LISA', 'barT']
def s(n):
    return n[0].upper() + n[1:].lower()
print map(s, N)

def ff(x, y):
  return x * y

print reduce(ff, [2, 4, 5, 7, 12])

def is_odd(x):
  return x % 2 == 1

print filter(is_odd, [1, 4, 6, 7, 9, 12, 17])

def is_not_empty(s):
  return s and len(s.strip()) > 0

print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])

import math
def is_sqr(x):
  r = int(math.sqrt(x))
  return r * r == x

print filter(is_sqr, range(1, 101))

def cmp_ignore_case(s1, s2):
  u1 = s1.upper()
  u2 = s2.upper()
  if u1 < u2:
    return -1
  if u1 > u2:
    return 1
  return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)