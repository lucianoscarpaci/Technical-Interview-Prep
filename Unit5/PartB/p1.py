# In the villager class below, each villager has a friends attribute, which is a list of other
# villagers they are friends with.
# Write a method get_mutuals that takes one parameter a villager instance new_contact and returns a list
# with the name of all friends the current villager and new_contact have in common.
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        # Create new instance
        stack = []
        for i in self.friends:
            if i in new_contact.friends:
                stack.append(i.name)

        return stack


bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
print(bob.get_mutuals(ankha))
