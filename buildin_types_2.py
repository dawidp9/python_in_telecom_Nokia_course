file = open('people_age.txt', 'r')
d = dict()

for line in file:
    l = line.split()
    d[l[0]] = l[1]

file.close()
print d
