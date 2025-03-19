class Player:
    def __init__(self, character, kart, outcomes):
        self.character = character
        self.kart = kart
        self.items = []
        self.race_outcomes = outcomes

    def get_tournament_place(self, opponents):
        # Calculate the average race outcome position for the player
        self_avg = sum(self.race_outcomes) / len(self.race_outcomes)

        # Create a list to store averages of all players
        all_averages = [(self.character, self_avg)]

        # Iterate through opponents to calculate their average race outcomes
        for opponent in opponents:
            opponent_avg = sum(opponent.race_outcomes) / len(opponent.race_outcomes)
            all_averages.append((opponent.character, opponent_avg))

        # Sort players by their average outcomes in ascending order (best to worst)
        all_averages.sort(key=lambda x: x[1])

        # Find the position of the current player in the sorted list
        for index, (character, avg) in enumerate(all_averages):
            if character == self.character:
                return index + 1  # Position is index+1


player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3])
player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])
opponents = [player2, player3]
print(player1.get_tournament_place(opponents))
