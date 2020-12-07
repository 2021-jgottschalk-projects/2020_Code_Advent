import re

# Main routine goes here

# write data from file
f = open("2020_advent_07_data.txt", "r")

content = f.read()

content = "light red bags contain 1 bright white bag, " \
              "2 muted yellow bags. " \
              "dark orange bags contain 3 bright white bags, " \
              "4 muted yellow bags. bright white bags contain 1 shiny gold bag. " \
              "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags. " \
              "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags. " \
              "dark olive bags contain 3 faded blue bags, 4 dotted black bags. " \
              "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags. " \
              "faded blue bags contain no other bags. dotted black bags contain no other bags."

whole_rules = content.split(". ")

f.close()

all_rules = []



for item in whole_rules:
    rules = re.split(r"contain | ,", item)
    all_rules.append(rules)


total = 0

colors = ["bright white"]

for color in colors:

    for item in all_rules:

        for thing in item:
            print(thing)
            print()
            print("color list", colors)

            color_result = re.search(color, thing)
            if color_result is not None:
                print("we have white!!")
                total += 1
                get_new = all_rules.index(item)
                new_color_raw = item[0]
                new_color_list = new_color_raw.split(" ")
                print("colour list", new_color_list)
                new_color = "{} {}".format(new_color_list[0], new_color_list[1])
                if new_color not in colors:
                    colors.append(new_color)

print("total: ", total)
# answer not 104
# it's not 6 either!
# it's not 8


