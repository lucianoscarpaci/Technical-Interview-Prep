def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if s.count(char) != t.count(char):
            return False
    return True

print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))
print(is_anagram("ack", "kac"))