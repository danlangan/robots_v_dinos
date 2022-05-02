from robots import Robot

class Fleet:
    def __init__(self):
        self.robots = []   #leaving the backets open here so that when the robots get appended later on in the code it creates a list of robots that will populate the Fleet
        self.populate_fleet()
        self.robot_total_health()

    def populate_fleet(self):
        robot1 = Robot()
        robot2 = Robot()
        robot3 = Robot()
        
        self.robots.extend([robot1, robot2, robot3])

    def robot_total_health(self):
        self.robot_total_health = sum(self.health.robot1, self.health.robot2, self.health.robot3)

