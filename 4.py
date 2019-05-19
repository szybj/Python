# -*- coding:utf-8 -*-

A = ['Michael', 100, True]
print A[0] # Michael
print A[1] # 100
print A[2] # True

A = ['Michael', 100, True]
print A[-1] # True
print A[-2] # 100
print A[-3] # Michael

Names = ['A', 'B', 'C']
Names.append('D')
print Names

Names = ['B', 'C', 'D']
Names.insert(0, 'A')
print Names # 

L = ['A', 'B', 'C', 'D']
print L.pop() # 'D'
print L.pop(1) # 'B'
print L # 'B'

L = ['A', 'C', 'C']
L[1] = 'B'
print L #

t = (1,)
print t
t = ('a', 'b', ['A', 'B'])
L = t[2]
L[0] = 'X'
L[1] = 'Y'
print t