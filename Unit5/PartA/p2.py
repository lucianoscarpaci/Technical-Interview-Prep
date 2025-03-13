class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    
    def greet_player(self, name, player_name, catchphrase):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

bones = Villager("Bones", "Dog", "yip yip").greet_player("Bones", "player_name", "catchphrase")
print(bones)
