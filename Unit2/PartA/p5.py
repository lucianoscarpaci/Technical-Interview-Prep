def best_set(votes):
    # Create a dictionary to store the number of votes for each candidate
    vote_count = {}
    for vote in votes.values():
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1

    # Find the candidate with the most votes
    max_votes = 0
    best_candidates = []
    # vote_count {'SZA': 3, 'Yo-Yo Ma': 1, 'Ethel Cain': 2}
    for candidate, votes in vote_count.items():
        if votes > max_votes:
            max_votes = votes
            best_candidates = candidate
        elif votes == max_votes:
            best_candidates = candidate
    # return the candidate(s) with the most votes
    return best_candidates

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