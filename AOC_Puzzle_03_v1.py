import re

f = open("2020_advent_03_data.txt", "r")

content = f.read()

content_list = content.splitlines()

f.close()

big_list = []

for item in content_list:
    big = item * 100
    big_list.append(big)

var_row = 0
num_trees = 0
for item in big_list:
    print(item)
    check_position = var_row * 3
    print("check", check_position)
    if item[check_position] == "#":
        print("TREE")
        num_trees += 1
        print(num_trees)
    var_row += 1


print(num_trees)
