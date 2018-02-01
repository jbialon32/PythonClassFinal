'''
Created on Dec 12, 2017

@author: James
'''

from pathlib import Path
from os.path import join as PathJoin
from Mechanics.ItemGen import LootDrop

class FireElemental:
    
    def __init__(self):
        self.name = 'Fiera'
        self.descrip = 'Live bundle of flames'
        self.minAppear = 10
        self.maxAppear = 999
        self.maxHP = 50
        self.hp = 40
        self.damage = 15
        self.xpValue = 100
        self.cave1Path = 'Assets|Monsters|Images|FireCave1.gif'.split('|')
        self.cave1 = Path(PathJoin(*self.cave1Path))
        self.cave2 = None

    def Attack(self, other):
        other.hp -= self.damage
        return other.hp
    
    def Loot(self, Character):
        LootDrop(Character, self.name)