# -*- coding:utf-8 -*-
L = range(1, 101)
print L
print L[:10]
print L[2:100:3]
print L[4:50:5]

L = ['Adam', 'Lisa', 'Bart', 'Paul']
print L
print L[-2:]
print L[:-2]
print L[-3:-1]
print L[-4:-1:2]

L = range(1, 101)
print L
print L[-10:]
print L[-46::5]

print 'abc'.upper()

def firstCharUpper(str):
    return str[0].upper() + str[1:]

print firstCharUpper('asd')