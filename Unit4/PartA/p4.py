# average value of nfts in a collection
# first access the nft collection by value
def average_nft_value(nft_collection):
    total_value = 0
    #Loop through each NFT in the collection
    for nft in nft_collection:
        # Access the 'value' of each nft and add it to the total_value
        total_value += nft["value"] #[5.4], [8.9], None
    # Calculate the average by dividing the total value by the number of nfts
    if len(nft_collection) > 0:
        average_value = total_value / len(nft_collection) #[17.1/3], [18.3]/2, 9.15/0
    else:
        average_value = 0
    
    return average_value

'''
Time complexity is O(n) + O(1) = O(n)
Space complexity is O(1)
'''

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2))

nft_collection_3 = []
print(average_nft_value(nft_collection_3))