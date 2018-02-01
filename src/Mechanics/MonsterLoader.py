'''
Created on Nov 2, 2017

@author: James
'''

from Assets.Monsters.Imp import Imp
from Assets.Monsters.Troll import Troll
from Assets.Monsters.Minotaur import Minotaur
from Assets.Monsters.FireElemental import FireElemental
from Assets.Monsters.WaterElemental import WaterElemental
from random import randint

## Creates a list of each existing monster and uses a random int to choose the enemy
def Generate():
    imp = Imp()
    troll = Troll()
    mino = Minotaur()
    fire = FireElemental()
    water = WaterElemental()
    monsters = [imp, troll, mino, fire, fire, water, water]
    test = randint(0, (len(monsters)-1))
    testMon = monsters[test]
    return testMon
        