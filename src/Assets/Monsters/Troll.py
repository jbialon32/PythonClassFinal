'''
Created on Oct 30, 2017

@author: James
'''

from pathlib import Path
from os.path import join as PathJoin
from Mechanics.ItemGen import LootDrop

class Troll:
    
    def __init__(self):
        self.name = 'Troll'
        self.descrip = 'Mighty smasher of wee thing'
        self.minAppear = 5
        self.maxAppear = 1000
        self.maxHP = 15
        self.hp = 15
        self.damage = 5
        self.xpValue = 50
        self.cave1Path = 'Assets|Monsters|Images|TrollCave1.gif'.split('|')
        self.cave1 = Path(PathJoin(*self.cave1Path))
        self.cave2Path = 'Assets|Monsters|Images|TrollCave2.gif'.split('|')
        self.cave2 = Path(PathJoin(*self.cave2Path))
        
    def Attack(self, other):
        other.hp -= self.damage
        return other.hp
    
    def Loot(self, Character):
        LootDrop(Character, self.name)