file = open('three_rings.txt', 'r')

for line in file:
    for word in line.split():
        print "{0:>20}".format(word)

file.close()