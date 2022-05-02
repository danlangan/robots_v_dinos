import random
from weapons import Weapon

class Robot:
    def __init__(self, robot_name):
        self.robot_name = random.choice(robot_name)
        self.health = [100]
        self.weapon = Weapon()



    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.weapon_damage
        print(f"f{dinosaur.name} is down to {dinosaur.health}!")
        print("")