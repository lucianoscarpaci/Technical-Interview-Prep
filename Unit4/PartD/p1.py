# Understand
# We need empty list for nft names.
# loop through all nfts in nft collections.
# add to the list the nfts, extract the names.
# append value to nft list.
# return the list
# Plan
# Implement
def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names


# Example usage:
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8},
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
]

nft_collection_3 = [{"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}]

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))

"""
['Abstract Horizon', 'Pixel Dreams', 'Future City']
['Crypto Kitty', 'Galactic Voyage']
['Golden Hour']
"""
