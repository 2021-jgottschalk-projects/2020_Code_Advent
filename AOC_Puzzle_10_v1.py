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

count = 0
for item in integer_list[1:]:
    ans = item - integer_list[count]
    count += 1

    if ans == 1:
        num_1s += 1
    elif ans == 3:
        num_3s += 1

print("1's: {} | 3's: {}".format(num_1s, num_3s))

print("Final Answer: ", num_3s * num_1s)
# final answer is 2244
