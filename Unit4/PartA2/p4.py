def is_anagram(s, t):
    if len(s) != len(t):
        return False

    s_freq = {}
    t_freq = {}

    for c in s:
        s_freq[c] = s_freq.get(c, 0) + 1

    for c in t:
        t_freq[c] = t_freq.get(c, 0) + 1

    return s_freq == t_freq


s = "anagram"
t = "nagaram"
print(is_anagram(s, t))  # True