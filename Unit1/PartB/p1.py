def reverse_sentence(sentence):
    word_list = sentence.split()
    return " ".join(reversed(word_list))


sentence = "tubby little cubby all stuffed with fluff"
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)
sentence = "Pooh"
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)
