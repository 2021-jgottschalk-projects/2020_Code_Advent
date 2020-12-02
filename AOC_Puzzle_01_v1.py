f = open("2020_advent_01_data.txt", "r")

content = f.read()

content_list = content.splitlines()

f.close()

num_list = []
for item in content_list:
  item = int(item)
  num_list.append(item)

print(num_list)

for item in num_list:
  target = 2020 - item
  if target in num_list:
    initial = item
    print(target)
    print(item)
    break

answer = initial * target
print(answer)