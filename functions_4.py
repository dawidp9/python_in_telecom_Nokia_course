def my_fun(input):
    return filter(lambda word: word[0] == 'b', input)

file = open('three_rings.txt', 'r')
file_list = file.read().split()
file.close()

print my_fun(file_list)
