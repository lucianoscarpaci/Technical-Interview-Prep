def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        pass
    else:
        print(f"I'm sorry, I don't know {character}'s catchphrase!")

character = "Pooh"
print_catchphrase(character)
character = "Piglet"
print_catchphrase(character)