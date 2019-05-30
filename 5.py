# -*- coding:utf-8 -*-
# if age >= 18:
#     print 'your age is', age
#     print 'adult'
# print 'END'
score = 20
if score >= 90:
    print 'excellent'
elif score >= 80:
    print 'good'
elif score >= 60:
    print 'passed'
else:
    print 'failed'

L = ['A', 'B', 'C', 'D']
for z in L:
    print z

sum = 0
x = 1
n = 1
while True:
    sum = sum + x
    x = x * 2
    n = n + 1
    if n > 20:
        break
print sum

L = [75, 98, 59, 81, 66, 43, 69, 85]
sum = 0.0
n = 0
for x in L:
    sum += x
    n += 1
print sum / n

L = [75, 98, 59, 81, 66, 43, 69, 85]
sum = 0.0
n = 0
for x in L:
    if x < 60:
        continue
    sum += x
    n += 1
print sum / n #79

for x in ['A', 'B', 'C']:
    for y in ['1', '2', '3']:
        print x + y

for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if x < y:
            print x * 10 + y