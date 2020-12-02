import re

f = open("2020_advent_02_data.txt", "r")

content = f.read()

content_list = content.splitlines()

f.close()

num_valid = 0

for item in content_list:
  thing = re.split('[- :]', item)
  # print(thing)

  pos_1 = int(thing[0])
  pos_2 = int(thing[1])
  target = thing[2]
  pword = thing[4]

  if target == pword[pos_1-1] and target != pword[pos_2-1]:
    num_valid += 1
  elif target != pword[pos_1-1] and target == pword[pos_2-1]:
    num_valid += 1

print("Valid", num_valid)
