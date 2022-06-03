from xml.dom.xmlbuilder import DOMInputSource
from dinosaurs import Dinosaur

class Herd:
    def __init__(self, herd_health):
        self.dinos = []
        self.populate_herd()
        self.dino_total_health(self.herd_health)

    def populate_herd(self):
        dino_name = ['Rex', 'Duke', 'Otto']
        dinosaur1 = Dinosaur(dino_name[0], 100)
        dinosaur2 = Dinosaur(dino_name[1], 100)
        dinosaur3 = Dinosaur(dino_name[2], 100)
        
        self.dinos.extend([dinosaur1, dinosaur2, dinosaur3])

    def dino_total_health(self, herd_health):
        self.herd_health = total_hp
        for dinosaur in self.dinos:
            total_hp = 0
            total_hp += dinosaur.health
        return total_hp
        
        
        
        # self.dino_total_health = sum(self.dinosaur1.health, self.dinosaur2.health, self.dinosaur3.health)
        