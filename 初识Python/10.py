# -*- coding:utf-8 -*-

L = []
for x in range(1, 11):
  L.append(x * x)
print L

L = [x * x for x in range(1, 11)]
print L

p = [x * (x + 1) for x in range(1, 100, 2)]
print p

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
tds = ['<tr><td>%s</td><td>%s</td></tr>'%(name, score) for name, score in d.iteritems()]
print '<table>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'


d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
tds = [generate_tr(name, score) for name, score in d.iteritems()]
print  '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

print [x * x for x in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print [x * x for x in range(1, 11) if x % 2 == 0]
# [4, 16, 36, 64, 100]

def toUppers(L):
  return [x.upper() for x in L if isinstance(x, str)]
print toUppers(['asd', 123])

print [m + n for m in 'ABC' for n in '123']

print [(100 * x + 10 * y + z) for x in range(1, 10) for y in range(10) for z in range(10) if x == z]