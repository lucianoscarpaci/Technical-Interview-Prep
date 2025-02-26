def get_top_player(dictionary):
    high_score = float('-inf')
    top_player = ""

    for name, score in dictionary.items():
        if score > high_score:
            high_score = score
            top_player = name
        
    return top_player, high_score