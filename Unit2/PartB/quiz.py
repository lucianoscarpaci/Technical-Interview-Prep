def count_words(sentence):
    words = sentence.split() #['this', 'is', 'a', 'test', 'only']
    word_count = {}
    for word in words: # 'this'
        word_count[word] = words.count(word)
    return word_count
# I dont understand why the output is not as expected
# The expected output is {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'only': 1}


sentence = "this is a test only"
print(count_words(sentence))