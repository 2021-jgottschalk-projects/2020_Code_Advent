# Main routine goes here

f = open("2020_advent_06_data_v2.txt", "r")

content = f.read()

content_list = content.splitlines()

f.close()

sum = 0
for item in content_list:
    unique = set(item)
    sum += len(unique)

print(sum)
