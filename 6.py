# -*- coding:utf-8 -*-
d = {
    'Adam': 98,
    'Lisa': 94,
    'Bart': 59
}
print len(d)
print d['Adam'] # 98 
if 'Dav' in d:
    print d['Dav']

d['Paul'] = 72

print d
d['Lisa'] = 99
print d

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
for key in d:
    print key

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key in d:
    print key+ ':', d[key]

s = set(['A', 'B', 'C', 'D'])
print s

print 'A' in s

s = set(['Adam', 'Lisa', 'Bart'])
for name in s:
    print name

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for item in s:
    print item[0] + ':', item[1]

s = set([1, 2, 3, 4])
s.add(4)
print s

s = set([1, 2, 3])
s.remove(2)
print s