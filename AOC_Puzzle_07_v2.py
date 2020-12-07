import re

# Main routine goes here

# write data from file
f = open("2020_advent_07_data.txt", "r")

content = f.read()

whole_rules = content.split(". ")

f.close()

all_rules = []

for item in whole_rules:
    rules = re.split(r"contain | ,", item)
    all_rules.append(rules)


total = 0

colors = ["white"]

for color in colors:

    for item in all_rules:

        for thing in item:
            print(thing)
            print()

            color_result = re.search(color, thing)
            if color_result is not None:
                print("we have white!!")
                total += 1
                get_new = all_rules.index(item)
                new_color_raw = item[0]
                new_color_list = new_color_raw.split(" ")
                print("colour list", new_color_list)
                new_color = new_color_list[1]
                if new_color not in colors:
                    colors.append(new_color)

print("total: ", total)


