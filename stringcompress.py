def string(s):
    compressed = ""
    count = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed += s[i-1] + str(count) if count > 1 else s[i-1]
            count = 1
    compressed += s[ -1] + str(count) if count > 1 else s[ -1]
    return compressed


s = "aaabbcccdd"
result = string(s)

print(f"Original String is {s}")
print(f"compressed string is {result}")

def compressed_string(s):
    if len(s) == 1:
        return s
    compressed_string = ""
    count = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed_string += s[i-1] + str(count)
            count = 1
    compressed_string += s[ -1] + str(count)
    return compressed_string if len(compressed_string) < len(s) else s


s = "aaabbcccdd"
result = compressed_string(s)

print(f"Original String is {s}")
print(f"compressed string is {result}")





