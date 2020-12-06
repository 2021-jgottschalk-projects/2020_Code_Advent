content_list = [
    "abc", "abc", "abac", "aaaa", "b"
]

sum = 0

for item in content_list:
    unique = set(item)
    print(unique)
    sum += len(unique)

print(sum)

