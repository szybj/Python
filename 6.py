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
for a in s:
    print a[0] + ':', a[1]