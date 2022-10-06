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
        self.name = ''

# Enemy Subclass moderate


class ModerateEnemy(Enemy):
    def __init__(self):
        pass

# Enemy Subclass difficult


class DifficultEnemy(Enemy):
    def __init__(self):
        pass

# Building class


class Building:
    def __init__(self):
        pass
