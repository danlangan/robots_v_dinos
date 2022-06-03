import random

class Weapon:
    def __init__(self):
        pass
    
    def __str__(self, weapon_type) -> str:
        self.weapon_type = ['sword','spear','lazers']
        self.weapon_damage = [30, 30, 35]
        
        print(f"Using a {self.random.weapon_type}")
        if str == 'sword':
            Weapon("Sword", {random.choice.weapon_damage})
        elif str == 'lazers':
            Weapon("Lazers", {random.choice.weapon_damage})
        else:
            Weapon("Spear", {random.choice.weapon_damage})

        self.weapon_type = ['sword','spear','lazers']
        self.weapon_damage = [30, 30, 35]
