'''
Created on Dec 12, 2017

@author: James
'''

from pathlib import Path
from os.path import join as PathJoin
from Mechanics.ItemGen import LootDrop

class Minotaur:
    
    def __init__(self):
        self.name = 'Minos'
        self.descrip = 'Big bad bull'
        self.minAppear = 10
        self.maxAppear = 1000
        self.maxHP = 50
        self.hp = 50
        self.damage = 10
        self.xpValue = 100
        self.cave1Path = 'Assets|Monsters|Images|MinoCave1.gif'.split('|')
        self.cave1 = Path(PathJoin(*self.cave1Path))
        self.cave2Path = 'Assets|Monsters|Images|MinoCave1.gif'.split('|')
        self.cave2 = Path(PathJoin(*self.cave2Path))

    def Attack(self, other):
        other.hp -= self.damage
        return other.hp
    
    def Loot(self, Character):
        LootDrop(Character, self.name)