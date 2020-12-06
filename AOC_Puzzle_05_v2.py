import math


def to_decimal(binary, symbol):
    total = 0
    for char in binary:
        if char == symbol:
            total = total * 2 + 1
        else:
            total = total * 2

    return total


# Main routine goes here

f = open("2020_advent_05_data.txt", "r")

content = f.read()

content_list = content.splitlines()

f.close()

all_seats = []

for item in content_list:
    row = to_decimal(item[:7], "B")
    seat = to_decimal(item[7:], "R")
    seatID = row * 8 + seat

    all_seats.append(seatID)

all_seats = sorted(all_seats)

