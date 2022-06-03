import random
from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

    def run_game(self):
        self.welcome_msg()
        self.battle()
        self.end_game_msg()
        
    def welcome_msg(self):
        print("ROBOTS VS DINOSAURS - WHAT WE'VE ALL BEEN WAITING FOR")

    def battle(self):
        while int(self.herd.herd_health) > 0 and int(self.fleet.fleet_health) > 0:
            dice_roll = random.randint(1, 10)
            if dice_roll % 2 == 0:
                self.dino_turn()
                if len(self.fleet.robots):
                    self.robo_turn()
            else:
                self.robo_turn()
                if int(self.herd.herd_health) > 0:
                    self.dino_turn()

    def dino_turn(self):
        self.show_dino_victim_options()
        dino_choice = int(input("Which dinosaur will attack?"))
        print("")
        self.show_robot_victim_options()
        robot_choice = int(input("Which robot will defend?"))
        print("")
        self.herd.dinos[dino_choice].attack(
            self.fleet.robots[robot_choice])
        if self.fleet.robots[robot_choice].health <= 0:
            print(f"{self.fleet.robots[robot_choice].name} has died :(")
            self.fleet.robots.remove(self.fleet.robots[robot_choice])

    def robo_turn(self):
        self.show_robot_victim_options()
        robot_choice = int(input('Which robot will attack?'))
        print("")
        self.show_dino_victim_options()
        dino_choice = int(input("What dinosaur will defend?"))
        print("")
        self.fleet.robots[robot_choice].attack(
            self.herd.dinos[robot_choice])
        if self.herd.dinos[dino_choice].health <= 0:
            print(f'{self.herd.dinos[dino_choice].name} has died :(')
            self.herd.dinos.remove(self.herd.dinos[dino_choice])

    def show_dino_victim_options(self):
        print('Choose your battling dinosaur!')
        index = 0 
        for dinosaur in self.herd.dinos:
            print(f'Press {index} for {dinosaur.name} with {dinosaur.health} health')
            index += 1

    def show_robot_victim_options(self):
        print('Choose the robot fighter!')
        index = 0
        for robot in self.fleet.robots:
            print(f'Press {index} for {robot.name} with {robot.health} health')
            index += 1

    def end_game_msg(self):
        if int(self.fleet.robot_total_health) > int(self.herd.dino_total_health):
            print("The robots have won the game!!!")
        else: 
            print("The dinosaurs have won the game !!")