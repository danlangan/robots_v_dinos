import random
from weapons import Weapon

class Robot:
    def __init__(self, robot_name, health):
        robot_names = ['Curly', 'Moe', 'Larry']
        self.robot_name = random.choice(robot_names)
        self.health = health
        print(f"{self.robot_name} is this Robot's name!")
        self.weapon = Weapon()

    def attack(self, dinosaur, weapon_type):
        self.dinosaur = random.choice(weapon_type)
        dinosaur.health -= self.weapon.weapon_damage
        print(f"f{dinosaur.name} is down to {dinosaur.health}!")
        print("")