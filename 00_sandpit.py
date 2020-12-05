import re


def get_string(string, search, length):
    string_index = string.index(search)
    start_string = string_index + len(search)
    end_string = start_string + length
    final_string = string[start_string:end_string]
    return final_string

string = 'pid:337605855 cid:249 byr:1952 hgt:155cm,ecl:grn iyr:2017 eyr:2026 hcl:#866857'

valid_eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

eye_pattern = r"ecl:\w{3}"
eye_pattern = re.search(eye_pattern, string)

print(eye_pattern)

if eye_pattern is not None:
    eyes = eye_pattern.group()
    eyes_only = eyes[4:7]
    print("eyes:", eyes_only)

    if eyes_only in valid_eyes:
        print('yay')
    else:
        print("oops")
