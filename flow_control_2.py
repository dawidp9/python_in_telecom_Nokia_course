plik = open('three_rings.txt', 'r')
plik_string = plik.read().lower().replace("ring", "wing")
plik.close()

plik2 = open('three_wings.txt', 'w')
plik2.write(plik_string)
plik2.close()

