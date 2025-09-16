def words_with_char(words, x):
    indices = []
    for i in range(len(words)):
        if x in words[i]:
            indices.append(i)
    return indices


words = ["batman", "superman"]
x = "a"
print(words_with_char(words, x))

words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
print(words_with_char(words, x))

words = ["star-lord", "gamora", "groot", "rocket"]
x = "z"
print(words_with_char(words, x))
