def GK_binary(decimal, symbol):
    total = 0
    for item in decimal:
        if item == symbol:
            total = total * 2 + 1
        else:
            total = total * 2

    return total

seat = "FFFBBBFRRR"
row = GK_binary(seat[:7], "B")
seat_ID = GK_binary(seat[7:], "R")
print(row)
print(seat_ID)
