def count_words(sentence):
    words = sentence.split() #['this', 'is', 'a', 'test', 'only']
    word_count = {}
    for word in words: # 'this'
        word_count[word] = words.count(word)
    return word_count

sentence = "this is a test only this will not be a test is it a test is it test or no test"
print(count_words(sentence))