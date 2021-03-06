import re


def lookIn(outerBag, trail):
  """
  This function looks in the rules dictionary to see if the outer bag contains 'shiny gold'.
  If it does, it returns true, ending the recursive tree.
  If it does not, it calls itself with each inner bag to check them.
  The trail keeps track of bags we've already checked just to keep from looping.
  """
  if 'shiny gold' in rules[outerBag]:
    return True
  else:
    for innerBag in rules[outerBag]:
      if innerBag not in trail:
        trail.append(innerBag)
        if lookIn(innerBag,trail):
          return True
    return False

def star1():
  """
  Star 1: Count how many bags contain directly or indirectly shiny gold bags
  Solved by recursively looking at the rules of inner bags and returning true if found.
  """
  count = 0
  for rule in rules:
    trail = []
    if lookIn(rule,trail):
      count += 1
  print(count)

def countBags(outerBag):
  """
  This function adds the number of each inner bag and multiplies that count by the count returned
  by calling itself on the inner bag color. If the bag contains no other bags, do not return a count.
  """
  count = 0
  if len(rules[outerBag]):
    for innerBag in rules[outerBag]:
      # Add the number of bags of that color
      count += rules[outerBag][innerBag]
      # Add the bags that they contain
      count += rules[outerBag][innerBag] * countBags(innerBag)
    return count
  else:
    return 0

def star2():
  """
  Star 2: Count how many bags in all are contained in your shiny gold bag.
  Solved by recursively counting the number of bags in each color of bag.
  """
  print(countBags('shiny gold'))


with open('2020_advent_07_data.txt') as f:
#with open('example.txt') as f:
  data = f.read().splitlines()

# Set up our regex rules
reOuter = re.compile('^([\w ]*) bags contain ')
reInner = re.compile('(\d{1,}) ([\w ]*) bag(?:s)?')

# Parse the data into a rules dictionary
rules = {}

for rule in data:
  # First get the outer bag
  outer = reOuter.findall(rule)[0]
  # Create key in the rules dictionary
  rules[outer] = {}
  # Find the color and number of bags that the outer bag hold
  inner = reInner.findall(rule)
  # Add these rules to the outer bag's key
  for bag in inner:
    rules[outer][bag[1]] = int(bag[0])   # Tuple is (num, 'color')

star1()
star2()
