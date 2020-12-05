import re

f = open("2020_advent_04_data_v2.txt", "r")

content = f.read()

content_list = content.splitlines()

f.close()

# Set up counter...
num_valid = 0

for item in content_list:
    # num_colons = item.count(":")
    num_byr = item.count("byr:")
    num_iyr = item.count("iyr:")
    num_eyr = item.count("eyr:")
    num_hgt = item.count("hgt:")
    num_hcl = item.count("hcl:")
    num_ecl = item.count("ecl:")
    num_pid = item.count("pid:")
    # num_cid = item.count("cid:")

    all_fields = [num_byr, num_iyr ,num_eyr, num_hgt, num_hcl,
                  num_ecl, num_pid]

    total = sum(all_fields)

    if total == 7:
        num_valid += 1

print("Number of valid passports: ", num_valid)
