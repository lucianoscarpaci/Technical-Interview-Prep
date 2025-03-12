def filter_meme_lengths(memes, max_length):
    # Create a list to store the memes that are shorter than max_length
    memes_list = []
    # Loop through the memes list
    for meme in memes:
    # If the length of the meme is less than or equal to max_length, add it to the list
        if len(meme) <= max_length:
            memes_list.append(meme)
    # Return the list of memes that are shorter than max_length
    return memes_list

memes = ["This is hilarious!", "A very long meme that goes on and on and on...", "Short and sweet", "Too long! Way too long!"]
memes_2 = ["Just right", "This one's too long though, sadly", "Perfect length", "A bit too wordy for a meme"]
memes_3 = ["Short", "Tiny meme", "Small but impactful", "Extremely lengthy meme that no one will read"]

print(filter_meme_lengths(memes, 20))
print(filter_meme_lengths(memes_2, 15))
print(filter_meme_lengths(memes_3, 10))
'''
['This is hilarious!', 'Short and sweet']
['Just right', 'Perfect length']
['Short', 'Tiny meme']
'''