def best_set(votes):
    # Create a dictionary to store the number of votes for each candidate
    vote_count = {}
    for vote in votes.values():
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1

    # Find the candidate with the most votes
    return max(vote_count, key=vote_count.get)

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))