# The data structure we need is a frequecy list ? or just a regular list ?
# we loop through all the creators in nft_collection
# then count by the frequency list how many times each creator is counted
# then once we the count the creator
# return the creator names
def identify_popular_creators(nft_collection):
    creator_nft = {}
    for nfts in nft_collection:
        creator = nfts["creator"]
        if creator in creator_nft:
            creator_nft[creator] += 1
        else:
            creator_nft[creator] = 1

    popular = [creator for creator, count in creator_nft.items() if count > 1]
    return popular


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5},
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3},
]

nft_collection_3 = [{"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))
"""
['ArtByAlex']
['SpaceArt']
[]
"""
