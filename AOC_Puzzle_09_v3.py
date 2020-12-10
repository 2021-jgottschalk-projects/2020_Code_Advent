# write data from file
f = open("2020_advent_09_data.txt", "r")

content = f.read()
numbers = content.splitlines()
f.close()

# Change data to integers...
integer_list = []
for item in numbers:
    item = int(item)
    integer_list.append(item)

target = 1721308972
# target = 127
add_list = []
list_item = -1

keep_going = "yes"
while keep_going == "yes":

    list_item += 1

    # add item to list
    add_list.append(integer_list[list_item])

    # Check to see if list total is target
    total = sum(add_list)
    print("Total: ", total)

    # too high? remove first item from list
    if total > target:
        while total > target:
            del add_list[0]
            print("remove it")
            total = sum(add_list)

    # too low? add next item to list
    if total < target:
        continue

    # equal?  End loop
    elif total == target:
        print()
        print("Addition list", add_list)
        break

    else:
        print("Houstan we have a problem")


add_list.sort()
answer = add_list[-1] + add_list[0]
print("Answer: ", answer)

too_low = 59335062
check  = answer - too_low
print(check)



