# Write the find_closest_nft_values()
# That takes a sorted list of NFT values and a budget
# and returns the pair of the two closest NFT values.
def find_closest_nft_values(nft_values, budget):
    # set a counter to 0
    counter = 0
    # set a variable to store the closest pair of nft values
    closest_pair = []
    # set a variable to store the minimum difference between the nft values and the budget
    min_diff = float("inf")
    # loop through the nft values
    for nft in nft_values:
    # calculate the difference between the budget and the current nft value
        diff = abs(budget - nft)
    # if the difference is less than the minimum difference
        if diff < min_diff:
    # update the minimum difference and the closest pair of nft values
            min_diff = diff
            closest_pair = (nft_values[counter], nft_values[counter + 1])
            # shift the nft value to the next index
            counter += 1
    return closest_pair

nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

print(find_closest_nft_values(nft_values, 8.0))
print(find_closest_nft_values(nft_values_2, 6.5))
print(find_closest_nft_values(nft_values_3, 3.0))