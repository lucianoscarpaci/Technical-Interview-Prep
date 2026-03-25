# Understand
# Make an empty list of nft to store the names of NFTs that match the tag.
# There is a collection of nfts, and tags which means we need to add nfts and the tags. to the list.
# Iterate through the collection and each NFT in the collection. If the nft tag is in the list,
# add the nft name to the result.
# Plan
# Implement


def search_nft_by_tag(nft_collections, tag):
    nft_tags = []
    for collection in nft_collections:
        for nfts in collection:
            if tag in nfts["tags"]:
                nft_tags.append(nfts["name"])
    return nft_tags


nft_collections = [
    [
        {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
        {"name": "Pixel Dreams", "tags": ["pixel", "retro"]},
    ],
    [
        {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
        {"name": "City Lights", "tags": ["modern", "landscape"]},
    ],
]

nft_collections_2 = [
    [
        {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
        {"name": "Sunset Serenade", "tags": ["sunset", "serene"]},
    ],
    [{"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}],
]

nft_collections_3 = [
    [{"name": "The Last Piece", "tags": ["finale", "abstract"]}],
    [
        {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
        {"name": "Mountain Peak", "tags": ["landscape", "adventure"]},
    ],
]

print(search_nft_by_tag(nft_collections, "landscape"))
print(search_nft_by_tag(nft_collections_2, "sunset"))
print(search_nft_by_tag(nft_collections_3, "modern"))
"""
['Urban Jungle', 'City Lights']
['Golden Hour', 'Sunset Serenade']
[]
"""
