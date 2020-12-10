# write data from file
f = open("2020_advent_10_tiny_data.txt", "r")

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

count = 0
for item in integer_list[1:]:
    ans = item - integer_list[count]

    if ans < 3:
        next_ans = item - integer_list[count + 1]

