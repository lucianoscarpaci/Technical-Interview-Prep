class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []


player_one = Player("Yoshi", "Super Blooper")
print(player_one.character)
print(player_one.kart)
print(player_one.items)
"""
Yoshi
Super Blooper
[]

"""
