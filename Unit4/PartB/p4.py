# Analyze the frequency of each word in a given text and identify the most frequent word.
# Write a function that returns the unqiue words and the number of times they appear in the text.
# Return the list of words that appear most frequently.
def word_frequency_analysis(text):
 # Create a dictionary to store the frequency of each word
    word_freq = {}
 # Loop through the text
    for word in text.split():
    #convert the word to lowercase
        word = word.lower()
    # remove any punctuation
        word = word.strip(".,")
    # If the word is not in the dictionary, set it with a frequency of 1
        if word not in word_freq:
            word_freq[word] = 1
    # If the word is in the dictionary, increment the frequency by 1
        else:
            word_freq[word] += 1
    # Find the highest frequency
    most_frequent_value = max(word_freq.values())
    # Create a list to store the words with the highest frequency
    most_frequent_word = []
    # Loop through the dictionary
    for word, frequency in word_freq.items():
        # If the frequency is equal to the highest frequency, add the word to the list
        if frequency == most_frequent_value:
            most_frequent_word.append(word)
    return word_freq, most_frequent_word

text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
print(word_frequency_analysis(text))

text_2 = "Digital nomads love to travel. Travel is their passion."
print(word_frequency_analysis(text_2))

text_3 = "Stay connected. Stay productive. Stay happy."
print(word_frequency_analysis(text_3))

'''
({'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 2, 'was': 1, 'not': 1, 'amused': 1}, ['the'])
({'digital': 1, 'nomads': 1, 'love': 1, 'to': 1, 'travel': 2, 'is': 1, 'their': 1, 'passion': 1}, ['travel'])
({'stay': 3, 'connected': 1, 'productive': 1, 'happy': 1}, ['stay'])
'''