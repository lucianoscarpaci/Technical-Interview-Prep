class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def get_player(self):
        return f"{self.character} driving the {self.kart}"


player_one = Player("Yoshi", "Super Blooper")
player_two = Player("Bowser", "Piranha Prowler")
# Print the player_two with the get_player method
# we need to print character. kart, items
print(f"Match: {player_two.get_player()} vs {player_one.get_player()}")
