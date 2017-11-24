import random

pole_kwadratu = 4
n = 100000
wpadlo = 0.0

for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if (pow(x, 2)+pow(y, 2)) < 1:
        wpadlo += 1

p = wpadlo/n
print 4*p