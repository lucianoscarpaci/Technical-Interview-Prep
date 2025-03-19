class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def get_player(self):
        return f"{self.character} driving the {self.kart}"


player_one = Player("Yoshi", "Super Blooper")
player_two = Player("Bowser", "Piranha Prowler")
player_one.kart = "Dolphin Dasher"
print(player_one.get_player())
