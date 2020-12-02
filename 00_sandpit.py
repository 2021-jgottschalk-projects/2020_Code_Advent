import re

txt = "1-3 a: cbade"

print()

thing = re.split('[- :]', txt)
print(thing)

target = thing[2]
pword = thing[4]

print(pword[0])
print(pword[2])

print(target)

if target == pword[0] and target != pword[2]:
  print("valid")
elif target != pword[0] and target == pword[2]:
  print("valid")

else:
  print("no")
