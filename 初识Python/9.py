# -*- coding:utf-8 -*-
L = range(1, 101)
for l in L:
  if l % 7 == 0:
    print l

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
  print index, '-', name

Name = ['Adam', 'Lisa', 'Bart', 'Paul']
Sorce = range(1, 5)

for n, s in zip(Name, Sorce):
  print n, '-', s

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for v in d.itervalues():
    sum += v
print sum / len(d)

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
print d.iteritems()

for name, score in d.iteritems():
  print name, ':', score
  sum += score
print 'average', ':', sum / len(d)