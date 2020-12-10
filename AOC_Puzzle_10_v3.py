# write data from file
f = open("2020_advent_10_data.txt", "r")

content = f.read()
numbers = content.splitlines()
f.close()

# Change data to integers...
integer_list = []
for item in numbers:
    item = int(item)
    integer_list.append(item)

integer_list.sort()
# print(integer_list)

num_1s = 1
num_3s = 1

one_three_list = []

count = 0
for item in integer_list[1:]:
    ans = item - integer_list[count]
    count += 1

    if ans == 1:
        num_1s += 1
        one_three_list.append(1)
    elif ans == 3:
        num_3s += 1
        one_three_list.append(3)
    elif ans == 2:
        one_three_list.append(2)

# print(one_three_list)

# make list a one_three_str
one_three_str = ""
for item in one_three_list:
    item = str(item)
    one_three_str += item
 
num_replaced = 0

find_11 = ""
while find_11 != -1:
    find_11 = one_three_str.find("11")

    if find_11 != -1:
        one_three_str = one_three_str.replace("11", "2")
        num_replaced += 1
        print(one_three_str)

num_2s = one_three_str.count('2')

find_21 = ""
while find_21 != -1:
    find_21 = one_three_str.find("21")

    if find_21 != -1:
        one_three_str = one_three_str.replace("21", "z")
        print(one_three_str)


num_z = one_three_str.count('z')

total = num_2s + num_z
print(total)
print("changes: {}".format(2**total))


# I thought it was 2^36 = 68719476736 <too low!>
