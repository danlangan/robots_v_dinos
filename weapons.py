import random

class Weapon:
    def __init__(self, weapon_type, weapon_damage):
        self.weapon_type = weapon_type
        self.weapon_damage = weapon_damage
    
    def __str__(self) -> str:
        print(f"Using a {self.random.weapon_type}")
        if str == 'sword':
            Weapon("Sword", {random.choice.weapon_damage})
        elif str == 'lazers':
            Weapon("Lazers", {random.choice.weapon_damage})
        else:
            Weapon("Spear", {random.choice.weapon_damage})

    weapon_type = ['sword','spear','lazers']
    weapon_damage = [30, 30, 35]
