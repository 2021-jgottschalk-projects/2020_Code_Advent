import re

f = open("2020_advent_02_data.txt", "r")

content = f.read()

content_list = content.splitlines()

f.close()

num_valid = 0

for item in content_list:
  thing = re.split('[- :]', item)
  #print(thing)

  first = int(thing[0])
  third = int(thing[1])
  target = thing[2]
  pword = thing[4]


  if target==pword[0] and target!=pword[2]:
    num_valid += 1

print("Valid", num_valid)