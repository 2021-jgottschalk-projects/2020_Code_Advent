# write data from file
f = open("2020_advent_09_data.txt", "r")

content = f.read()
numbers = content.splitlines()
f.close()

print(numbers)

# Change data to integers...
integer_list = []
for item in numbers:
    item = int(item)
    integer_list.append(item)


n = 25
item_ok = ""

for item in integer_list[25:]:
    # print(item)

    # print("numbers in sublist...")
    for entity in integer_list[n-25:n]:
        # print(entity)
        target = item - entity
        if target in integer_list[n-25:n]:
            item_ok = "yes"
            break
        else:
            item_ok = "no"
    n += 1

    if item_ok == "no":
        print("not OK:", item)



