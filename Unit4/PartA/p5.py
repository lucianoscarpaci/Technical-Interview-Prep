# Each NFT has a list of tags describing its style 
# "abstract", "landscape", "modern".
# goal return a list of NFT names that have specified tag
def search_nft_by_tag(nft_collections, tag):
    nft_names = []  # Use a list to store the names

    # Iterate over each sub-collection
    for sub_collection in nft_collections:
        # Iterate over each NFT dictionary within the sub-collection
        for nft in sub_collection: #[{'name': 'Abstract Horizon', 'tags': [...]}], [{'name': 'Urban Jungle', 'tags': [...]}]
            # Check if the tag is in the NFT's list of tags
            if tag in nft['tags']: #landscape, 
                # Append the name of the NFT to the list
                nft_names.append(nft['name']) #['Urban Jungle'], ['City Lights']

    return nft_names


# Example usage
nft_collections = [
    [
        {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
        {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
    ],
    [
        {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
        {"name": "City Lights", "tags": ["modern", "landscape"]}
    ]
]

nft_collections_2 = [
    [
        {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
        {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
    ],
    [
        {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
    ]
]

nft_collections_3 = [
    [
        {"name": "The Last Piece", "tags": ["finale", "abstract"]}
    ],
    [
        {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
        {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
    ]
]

print(search_nft_by_tag(nft_collections, "landscape"))
print(search_nft_by_tag(nft_collections_2, "sunset"))
print(search_nft_by_tag(nft_collections_3, "modern"))