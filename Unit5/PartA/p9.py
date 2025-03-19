class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def set_character(self, name):
        valid_names = [
            "Mario",
            "Luigi",
            "Peach",
            "Daisy",
            "Yoshi",
            "Toad",
            "Koopa Troopa",
            "Shy Guy",
            "Lakitu",
            "Toadette",
            "King Boo",
            "Baby Mario",
            "Baby Luigi",
            "Baby Peach",
            "Baby Daisy",
            "Baby Rosalina",
            "Metal Mario",
            "Larry",
            "Wendy",
            "Iggy",
            "Roy",
            "Lemmy",
            "Ludwig",
            "Dry Bones",
            "Bowser",
            "Donkey Kong",
            "Wario",
            "Waluigi",
            "Rosalina",
            "Mii",
        ]
        if name in valid_names:
            self.character = name
            print("Character updated!")
        else:
            print("Invalid character name")


player_three = Player("Donkey Kong", "Standard Kart")

player_three.set_character("Peach")
print(player_three.character)
player_three.set_character("Baby Peach")
print(player_three.character)
