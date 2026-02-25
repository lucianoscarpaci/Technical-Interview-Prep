def print_catchphrase(character):

    character = character.lower()
    hashmap = {
        "pooh": "Oh, bother!",
        "tigger": "TTFN: Ta-ta for now!",
        "eeyore": "Thanks for noticing me.",
        "christopher robin": "Silly old bear.",
    }
    if character in hashmap:
        print(hashmap[character])
    else:
        print("Sorry, I don't know Piglet's catchphrase.")


character = "Pooh"
print_catchphrase(character)
character = "Piglet"
print_catchphrase(character)
