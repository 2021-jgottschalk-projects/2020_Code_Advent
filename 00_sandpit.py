addition_list = [72411414, 78244973, 89011657, 112923589, 91455753, 87306899, 90675247, 94458958, 91090610, 105713231, 137282719, 108211332, 110549131, 110710483, 112694288, 114082556, 114486132]

target = 1721308972

total = 0
for item in addition_list:
    total += item

print("Target: {}, Total: {}".format(target, total))
difference = target - total
print("Diference", difference)

