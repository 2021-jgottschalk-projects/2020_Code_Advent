data_list = [
    ['kimczeyaqwbs', 'pwmsf', 'wgmfus', 'lofjwnms', 'rwsum'],
['cxns', 'c', 'cbv', 'c']
    ]

grand_total = 0

for item in data_list:
    people = len(item)
    common = 0
    total = 0

    # Generate entire string
    item_string = ""
    for word in item:
        item_string += word
    print("Item string", item_string)
    print()

    # get letters of first item in list
    for letter in item[0]:
        print(letter)
        letter_count = item_string.count(letter)
        print("letter count: ", letter_count)

        if letter_count == people:
            total += 1

    grand_total += total

    print("total", total)

    print()

print("Grand Total: ", grand_total)


