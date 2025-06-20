def find_most_frequent_keywords(scenes):
    keyword_count = {}
    res = []
    for keywords in scenes.values():
        for keyword in keywords:
            if keyword in keyword_count:
                keyword_count[keyword] += 1
            else:
                keyword_count[keyword] = 1
    max_ = 0
    for k, v in keyword_count.items():
        if v > max_:
            max_ = v
            res = [k]
        elif v == max_:
            res.append(k)
    return res


scenes = {
    "Scene 1": ["action", "hero", "battle"],
    "Scene 2": ["hero", "action", "quest"],
    "Scene 3": ["battle", "strategy", "hero"],
    "Scene 4": ["action", "strategy"],
}
print(find_most_frequent_keywords(scenes))

scenes = {
    "Scene A": ["love", "drama"],
    "Scene B": ["drama", "love"],
    "Scene C": ["comedy", "love"],
    "Scene D": ["comedy", "drama"],
}
print(find_most_frequent_keywords(scenes))
