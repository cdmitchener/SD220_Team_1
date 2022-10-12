# Zork 2 classes
# Joe Prater
# 10/05/2022
"""
OBJECTS FOR ZORK2:
PLAYER, ENEMIES, BUILDINGS
"""
# Player class
class Player:
    def __init__(self, pname):
        self.name = pname
        self.inventory = {'healing': ('Liu Ration'), 'weapon': (
            'Energy Revolver'), 'armor': ('Rad Suit')}
        self.health = 100

# Enemy class easy
class Enemy:
    def __init__(self):
        self.name = 'Radiated Skunk'
        self.damage = 40

    def attack(self):
        print('You are being attacked!')

    def info(self):
        print("Damage done by Radiated Skunk depletes 40 points from your health.")

# Enemy Subclass moderate
class ModerateEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Glowing Buffalo'
        self.damage = 90

    def attack(self):
        print('You are being attacked!')

    def info(self):
        print("Damage done by Glowing Buffalo depletes 90 points from your health.")

        pass

# Enemy Subclass difficult
class DifficultEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'A Hoard of Mutated Carniverous Ducks'
        self.damage = 110

    def attack(self):
        print('You are being attacked!')

    def info(self):
        print("Damage done by the hoard of Mutated Carniverous Ducks depletes 110 points from your health.")

        pass

class Building:
    def __init__(self, name, loot):
        self.name = name
        self.loot = loot
    # def info(self, info):  # Have to fill info below in methods
    #     print(info)

# Declare variables
note = "Dear Blake, I keep hearing rumors of a hidden vault in this region. The vault is supposed to be like the Noah's Ark of plants. I have been searching but there are just too many monsters out there. Looking through the binoculars, I noticed a glare coming from the Northwest. Perhaps it's a ventilation pipe sticking up from the ground. Well, I'm going to continue my search. Sincerily, Ryan"
password = 'The password is: PinkY_DustY_ToE'

# Creating the buildings
# building number is var, arguments are dicts with lists as values
# keys are healing, weapon, armor, quest items
# No ammo or duct tape installed yet

a1 = Building('Old Shack', {'healing': ['Liu Ration'], 'weapon': [
    'Nikola Rifle']})
a2 = Building('Abandoned Drive-In', {'armor': ['Torso Plates']})
a3 = Building('Burned Down House', {'quest item': note})
b1 = Building('Airport', {'armor': ['Kevlar Overalls', 'Torso Plates'], 'quest item': [
    password], })
b2 = Building('Military Base', {'healing': ['Vodka'], 'weapon': [
    'J.E.D']})
b3 = Building("Elon Musk's Vacation Home", {'healing': [
    'First-Aid-Kit'], 'quest item': ['Pet Python'], 'armor': ['Torso Plates']})
c1 = Building('The Seed Vault', {'healing': ['Liu Ration'], 'weapon': [
    'Energy Revolver'], 'armor': ['Rad Suit']})

"""
    TESTING THE OBJECTS AND THIER
    ATRIBUTES AND METHODS
"""
#player = Player('joe')
#print("player:", player.name, player.inventory, player.health)

#enemy = Enemy()
#print('Easy enemy', enemy.name, enemy.attack(), enemy.info())

#modenemy = ModerateEnemy()
#print("moderater enemy: ", modenemy.name, modenemy.attack(), modenemy.info())


#hardenemy = DifficultEnemy()
# print("Difficult enemy: ", hardenemy.name,
#      hardenemy.attack(), hardenemy.info())

#building = Building('house', ['gun', 'vodka'])
# print('This is building: ', building.name, building.loot,
#      building.info('house', ['gun', 'vodka']))