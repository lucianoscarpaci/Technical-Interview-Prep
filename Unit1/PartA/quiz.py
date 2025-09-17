def tiggerfy(s):
    ans = ""
    for c in s:
        if c in "tigger":
            continue
        ans += c
    return ans


s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))
tiggerfy(s)
s = "Hunny"
print(tiggerfy(s))
tiggerfy(s)
