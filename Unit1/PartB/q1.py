def are_equivalent(word1, word2):
    word1 = "".join(word1)
    word2 = "".join(word2)
    if word1 != word2:
        return False
    return True

word1 = ["bat", "man"]
word2 = ["b", "atman"]
print(are_equivalent(word1, word2))
word1 = ["alfred", "pennyworth"]
word2 = ["alfredpenny", "word"]
print(are_equivalent(word1, word2))

word1  = ["cat", "wom", "an"]
word2 = ["catwoman"]
print(are_equivalent(word1, word2))
