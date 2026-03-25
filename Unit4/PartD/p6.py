# Uderstand
# We have nfts that we need to process order them using a queue, and get the nft name key
#  and dequeue the names until we have the process order
# return the process order.
# Plan
# Implement
from collections import deque


def process_nft_queue(nft_queue):
    process_order = []
    queue = deque(nft_queue)

    while queue:
        nft = queue.popleft()
        process_order.append(nft["name"])
    return process_order


nft_queue = [
    {"name": "Abstract Horizon", "processing_time": 2},
    {"name": "Pixel Dreams", "processing_time": 3},
    {"name": "Urban Jungle", "processing_time": 1},
]
print(process_nft_queue(nft_queue))

nft_queue_2 = [
    {"name": "Golden Hour", "processing_time": 4},
    {"name": "Sunset Serenade", "processing_time": 2},
    {"name": "Ocean Waves", "processing_time": 3},
]
print(process_nft_queue(nft_queue_2))

nft_queue_3 = [
    {"name": "Crypto Kitty", "processing_time": 5},
    {"name": "Galactic Voyage", "processing_time": 6},
]
print(process_nft_queue(nft_queue_3))
