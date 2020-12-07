import re

# Main routine goes here

# write data from file
f = open("2020_advent_07_data.txt", "r")

content = f.read()

content_list = content.splitlines()

f.close()

all_rules = [['light red bags ', '1 bright white bag, '
                                 '2 muted yellow bags'],
             ['dark orange bags ', '3 bright white bags, '
                                   '4 muted yellow bags'],
             ['bright white bags ', '1 shiny gold bag'],
             ['muted yellow bags ', '2 shiny gold bags, '
                                    '9 faded blue bags'],
             ['shiny gold bags ', '1 dark olive bag, '
                                  '2 vibrant plum bags'],
             ['dark olive bags ', '3 faded blue bags, '
                                  '4 dotted black bags'],
             ['vibrant plum bags ', '5 faded blue bags, '
                                    '6 dotted black bags'],
             ['faded blue bags ', 'no other bags'],
             ['dotted black bags ', 'no other bags.']]


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


