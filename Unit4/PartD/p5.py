def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    s_freq = {}
    t_freq = {}

    for char in s:
        s_freq[char] = s_freq.get(char, 0) + 1