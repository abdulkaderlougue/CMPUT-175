file = open('earthquake.txt', 'r')
a = ['2006/10/18']
b = ['2006/10/19']
c = ['2006/10/20']
for line in file:
    el = line.split()
    if el[1] == '2006/10/18':
        a.append(el[0])
    if el[1] == '2006/10/19':
        b.append(el[0])
    if el[1] == '2006/10/20':
        c.append(el[0])
print (a,b,c)