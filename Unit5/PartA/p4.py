# Update the villager class with a method set_catchphrase() that takes in one
# parameter new_catchphrase and print("Catchphrase updated")
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def set_catchphrase(self, new_catchphrase):
        # If new_catchphrase is valid, it should update the villager's catchphrase
        
        if new_catchphrase.replace(" ", "").isalnum() and len(new_catchphrase) < 20:
            self.catchphrase = new_catchphrase
            print("Catchphrase updated!")
        else:
            print("Invalid catchphrase")
    # attribute to have value new_catchphrase and print("Catchphrase updated")
    # Otherwise, it should print("Invalid catchphrase")
    # Valid catchphrases are less than 20 characters in length. They must contain only alphabetic and whitespace characters.


alice = Villager("Alice", "Koala", "guvnor")


alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)
