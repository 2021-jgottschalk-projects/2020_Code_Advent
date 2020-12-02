import re

txt = "2-9 c: ccccccccc"

print()

thing = re.split('[- :]', txt)
print(thing)

first = int(thing[0])
third = int(thing[1])
target = thing[2]
pword = thing[4]

print(pword[0])
print(pword[2])

if target==pword[0] and target!=pword[2]:
  print("valid")

else:
  print("no")