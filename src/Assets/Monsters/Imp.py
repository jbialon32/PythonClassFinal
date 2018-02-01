'''
Created on Oct 27, 2017

@author: James
'''

from pathlib import Path
from os.path import join as PathJoin
from Mechanics.ItemGen import LootDrop

class Imp:
    
    def __init__(self):
        self.name = 'Imp'
        self.descrip = 'Weak little demon creature'
        self.minAppear = 1
        self.maxAppear = 5
        self.maxHP = 5
        self.hp = 5
        self.damage = 2
        self.xpValue = 3
        self.cave1Path = 'Assets|Monsters|Images|ImpCave1.gif'.split('|')
        self.cave1 = Path(PathJoin(*self.cave1Path))
        self.cave2Path = 'Assets|Monsters|Images|ImpCave2.gif'.split('|')
        self.cave2 = Path(PathJoin(*self.cave2Path))

    def Attack(self, other):
        other.hp -= self.damage
        return other.hp
    
    def Loot(self, Character):
        LootDrop(Character, self.name)