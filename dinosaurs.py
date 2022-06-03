import random

class Dinosaur:
    def __init__(self, dino_name, health):
        dino_names = ['Rex', 'Duke', 'Otto']
        self.dino_name = random.choice(dino_names)
        self.health = health
        print(f"{self.dino_name} is this dinosaur's name!")

    def dino_attack(self, robot):
        dino_attack = ['Bite', 'Claw', 'Tail Sweep']
        attack_power = [35, 30, 30]
        self.robot = random.choice(dino_attack)
        self.attack_power = random.choice(attack_power)
        robot.health -= self.weapon.attack_power
        print(f"f{robot.name} is down to {robot.health}!")
        print("")
