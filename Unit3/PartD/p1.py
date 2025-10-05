def reverse_vowels(s):
    stack = []
    vowels = set("aeiouAEIOU")
    s = list(s)
    for char in s:
        if char in vowels:
            stack.append(char)
    for i in range(len(s)):
        if s[i] in vowels:
            s[i] = stack.pop()
    return "".join(s)


s = "hello"
print(reverse_vowels(s))  # Output: "holle"
s = "leetcode"
print(reverse_vowels(s))  # Output: "leotcede"
s = "aA"
print(reverse_vowels(s))  # Output: "Aa"
