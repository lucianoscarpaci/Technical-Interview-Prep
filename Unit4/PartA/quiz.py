def count_meme_creators(memes):
    # Create a dictionary to store frequency of each name
    name_freq = {}
    # Loop through the memes list
    for meme in memes:
    # For each meme, get the creator name
        creator = meme["creator"]
        if creator not in name_freq:
    # If the creator name is not in the dictionary, add it with a frequency of 1
            name_freq[creator] = 1
    # If the creator name is in the dictionary, increment the frequency by 1
        else:
            name_freq[creator] += 1
    # return the dictionary
    return name_freq


memes = [
    {"creator": "Alex", "text": "Meme 1"},
    {"creator": "Jordan", "text": "Meme 2"},
    {"creator": "Alex", "text": "Meme 3"},
    {"creator": "Chris", "text": "Meme 4"},
    {"creator": "Jordan", "text": "Meme 5"}
]

memes_2 = [
    {"creator": "Sam", "text": "Meme 1"},
    {"creator": "Sam", "text": "Meme 2"},
    {"creator": "Sam", "text": "Meme 3"},
    {"creator": "Taylor", "text": "Meme 4"}
]

memes_3 = [
    {"creator": "Blake", "text": "Meme 1"},
    {"creator": "Blake", "text": "Meme 2"}
]

print(count_meme_creators(memes))
print(count_meme_creators(memes_2))
print(count_meme_creators(memes_3))
'''
{'Alex': 2, 'Jordan': 2, 'Chris': 1}
{'Sam': 3, 'Taylor': 1}
{'Blake': 2}
'''