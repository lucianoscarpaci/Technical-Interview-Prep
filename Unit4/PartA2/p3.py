def find_trending_memes(memes):
    # A meme is trending if its in the dataset multiple times
    # Create a dictionary to store frequency of each meme
    meme_freq = {}
    # Loop through the memes list
    for meme in memes:
        # If the meme is not in the dictionary, add it with a frequency of 1
        if meme not in meme_freq:
            meme_freq[meme] = 1
        else:
            meme_freq[meme] += 1
    # Create a list to store the memes that are trending
    trending_memes = []
    # Loop through the dictionary
    for meme, frequency in meme_freq.items():
        # If the name is trending add it to the list
        if frequency > 1:
            trending_memes.append(meme)
    # Return the list of trending memes
    return trending_memes

memes = ["Dogecoin to the moon!", "One does not simply walk into Mordor", "Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine", "Surprised Pikachu", "Surprised Pikachu"]
memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

print(find_trending_memes(memes))
print(find_trending_memes(memes_2))
print(find_trending_memes(memes_3))