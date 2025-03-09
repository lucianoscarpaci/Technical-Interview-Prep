def identify_popular_creators(nft_collection):
    creator_count = {}
    for nft in nft_collection:
        creator = nft["creator"]
        if creator in creator_count:
            creator_count[creator] += 1
        else:
            creator_count[creator] = 1
    popular_creators = [creator for creator, count in creator_count.items() if count > 1]
    return popular_creators
'''
Time complexity is O(n) = O(n) + O(n) = O(2n) = O(n) 
'''
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))
