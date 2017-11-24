plik = open('three_rings.txt', 'r')
list = []

plik_string = plik.read().replace(",", ' ').replace(".", ' ').lower().split()


for item in plik.read().split():
    if list.count(item.lower()) == 0:
        list.append(item.lower())
plik.close()

print sorted(list)


