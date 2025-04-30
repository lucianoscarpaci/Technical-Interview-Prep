def count_binary_substrings(s):
    groups = []
    count = 1

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            groups.append(count)
            count = 1
        else:
            count += 1
    groups.append(count)

    result = 0
    for i in range(1, len(groups)):
        result += min(groups[i-1], groups[i])
    return result

print(count_binary_substrings("00110011"))
print(count_binary_substrings("10101"))
print(count_binary_substrings("00011100"))
