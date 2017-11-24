def my_fun(list):
    return map(lambda word: str(word).replace("o", "."), list)

file = open('three_rings.txt', 'r')
file_list = file.read().split()
file.close()

print my_fun(file_list)