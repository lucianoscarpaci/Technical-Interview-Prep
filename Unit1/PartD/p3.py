def shuffle(message, indices):
    shuffled_message = [""] * len(message)
    for i in range(len(message)):
        shuffled_message[indices[i]] = message[i]
    return "".join(shuffled_message)


message = "evil"
indices = [3, 1, 2, 0]
print(shuffle(message, indices))

message = "findme"
indices = [0, 1, 2, 3, 4, 5]
print(shuffle(message, indices))
