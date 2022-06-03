from robots import Robot

class Fleet:
    def __init__(self):
        self.robots = []   #leaving the backets open here so that when the robots get appended later on in the code it creates a list of robots that will populate the Fleet
        self.populate_fleet()
        self.robot_total_health(self.fleet_health)

    def populate_fleet(self):
        robot_name = ['Curly', 'Moe', 'Larry']
        robot1 = Robot(robot_name[0], 100)
        robot2 = Robot(robot_name[1], 100)
        robot3 = Robot(robot_name[2], 100)
        
        self.robots.extend([robot1, robot2, robot3])

    def robot_total_health(self, fleet_health):
        self.fleet_health = total_hp
        for robot in self.robots:
            total_hp = 0
            total_hp += robot.health
        return total_hp



        #self.robot_total_health = sum(self.health.robot1, self.health.robot2, self.health.robot3)

