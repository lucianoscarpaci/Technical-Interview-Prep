def count_evens(lst):
    count = 0
    for word in lst:
        if len(word) % 2 == 0:
            count += 1
    return count

lst = ["na", "nana", "nanana", "batman", "!"]
print(count_evens(lst))

lst = ["the", "joker", "robin"]
print(count_evens(lst))

lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
print(count_evens(lst))