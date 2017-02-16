file = open('rainfall.txt', 'r')
newFile = open('rainfallfmt.txt','w')
a = []
b = []
c = []
d = []
for line in file:
    el = line.split()
    if 60<= float(el[1])<=70:
        a.append(el)
    elif 71< float(el[1])<=80:
        b.append(el)
    elif 81< float(el[1])<=90:
        c.append(el)
    elif 91< float(el[1]):
        d.append(el)

newFile.write('[60-70]:\n')
for v in a:
    
    newFile.write('%+25s %5.1f \n' % (v[0], float(v[1])))
    
newFile.write('[71-80]:\n')
for v in b:
    newFile.write('%+25s %5.1f \n' % (v[0], float(v[1])))

newFile.write('[81-90]:\n')
for v in c:
    newFile.write('%+25s %5.1f \n' % (v[0], float(v[1])))

newFile.write('[90-]:\n')
for v in d:
    newFile.write('%+25s %5.1f \n' % (v[0], float(v[1])))

file.close()
newFile.close()
 
 