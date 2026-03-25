# Understand
# We need to access the dictionary for the nft value.
# Using a loop through all the nfts, we calculate average of nft values
# Do the average of nft values by using sum of the nft names / how many nfts (length)
# Return the average of nft values.
# Plan
# Implement
def average_nft_value(nft_collection):
    if not nft_collection:
        return 0
    total_nfts = 0
    for nft_names in nft_collection:
        total_nfts += nft_names["value"]
    avg_nft_values = total_nfts / len(nft_collection)
    return avg_nft_values


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5},
]
print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4},
]
print(average_nft_value(nft_collection_2))

nft_collection_3 = []
print(average_nft_value(nft_collection_3))
