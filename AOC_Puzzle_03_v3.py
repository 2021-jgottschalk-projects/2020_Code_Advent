import re

f = open("2020_advent_03_data.txt", "r")

content = f.read()

content_list = content.splitlines()

f.close()

big_list = []

for item in content_list:
    big = item * 100
    big_list.append(big)

print("Length: ", len(big_list))

num_trees = 0

count_x = 0
count_y = 0

inc_x = 3
inc_y = 1

lines = int(len(big_list) / inc_y)

for item in range (0, lines):
    row = big_list[count_y]
    to_check = row[count_x]

    if to_check == "#":
        num_trees += 1
        print("TREE")

    count_x += inc_x
    count_y += inc_y

print(num_trees)
