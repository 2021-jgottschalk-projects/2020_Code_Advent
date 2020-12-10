string = "3111311313"
   
num_replaced = 0

find_11 = ""
while find_11 != -1:
    find_11 = string.find("11")

    if find_11 != -1:
        string = string.replace("11", "2")
        num_replaced += 1
        print(string)

num_2s = string.count('2')

find_21 = ""
while find_21 != -1:
    find_21 = string.find("21")

    if find_21 != -1:
        string = string.replace("21", "z")
        print(string)


num_z = string.count('z')

total = num_2s + num_z
print(total)
print("changes: {}".format(2**total))

