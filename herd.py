from xml.dom.xmlbuilder import DOMInputSource
from dinosaurs import Dinosaur

class Herd:
    def __init__(self):
        self.dinos = []
        self.populate_herd()
        self.dino_total_health()

    def populate_herd(self):
        dinosaur1 = Dinosaur(self.dino_name, self.health)
        dinosaur2 = Dinosaur(self.dino_name, self.health)
        dinosaur3 = Dinosaur(self.dino_name, self.health)

        dino_name = ['Rex', 'Duke', 'Otto']
        
        self.dinos.extend([dinosaur1, dinosaur2, dinosaur3])

    def dino_total_health(self):
        self.dino_total_health = sum(self.health.dinosaur1, self.health.dinosaur2, self.health.dinosaur3)
        