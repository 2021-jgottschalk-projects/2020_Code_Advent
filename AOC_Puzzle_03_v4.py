import re

# Check Trees


def get_trees(big_list, x, y):
    num_trees = 0

    count_x = 0
    count_y = 0

    inc_x = x
    inc_y = y

    lines = int(len(big_list) / inc_y)

    for item in range (0, lines):
        row = big_list[count_y]
        to_check = row[count_x]

        if to_check == "#":
            num_trees += 1

        count_x += inc_x
        count_y += inc_y

    return num_trees

# Get Data
f = open("2020_advent_03_data.txt", "r")

content = f.read()

content_list = content.splitlines()

f.close()

big_list = []

for item in content_list:
    big = item * 100
    big_list.append(big)

print("Length: ", len(big_list))

tree_total_list = []

cases = [
    [1, 1], [3, 1], [5, 1], [7, 1], [1, 2]
]

for item in cases:
    answer = get_trees(big_list, item[0], item[1])
    tree_total_list.append(answer)

for item in tree_total_list:
    print(item)

all_trees = 1
for item in tree_total_list:
    all_trees *= item

print(all_trees)
