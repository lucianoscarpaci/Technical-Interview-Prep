class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []  # Add the furniture attribute

    # ... methods from previous problems
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    def set_catchphrase(self, new_catchphrase):
        # If new_catchphrase is valid, it should update the villager's catchphrase

        if new_catchphrase.replace(" ", "").isalnum() and len(new_catchphrase) < 20:
            self.catchphrase = new_catchphrase
            print("Catchphrase updated!")
        else:
            print("Invalid catchphrase")

    # New method
    def add_item(self, item_name):
        # Add item_name to the furniture list
        if item_name not in self.furniture:
            self.furniture.append(item_name)
        # If item_name is already in the furniture list, do not add it again


alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)
