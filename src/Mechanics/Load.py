'''
Created on Nov 30, 2017

@author: James
'''

from pathlib import Path
from os.path import join as PathJoin
from Assets.Classes.Warrior import Warrior
from Assets.Classes.Mage import Mage
from Assets.Classes.Rouge import Rouge

## Grabs info from save file and creates character with same values
def Load():
    loadFile = open('Assets/Saves/Test.txt')
    charInfo = loadFile.readlines()
    loadFile.close()
    charInfo = charInfo[1]
    charInfo = charInfo.split('|')
    
    if charInfo[1] == 'Warrior':
        toon = Warrior(charInfo[0])
        toon.damage = int(charInfo[2])
        toon.level = int(charInfo[3])
        toon.xp = int(charInfo[4])
        toon.levelUp = int(charInfo[5])
        toon.maxHP = int(charInfo[6])
        toon.hp = int(charInfo[7])
        toon.maxMana = int(charInfo[8])
        toon.mana = int(charInfo[9])
        toon.maxEnergy = int(charInfo[10])
        toon.energy = int(charInfo[11])
        toon.str = int(charInfo[12])
        toon.agi = int(charInfo[13])
        toon.wis = int(charInfo[14])
        toon.luck = int(charInfo[15])
        toon.items[0].qty = int(charInfo[16])
        toon.items[2].qty = int(charInfo[17])
        toon.items[1].qty = int(charInfo[18])
        
    if charInfo[1] == 'Mage':
        toon = Mage(charInfo[0])
        toon.damage = int(charInfo[2])
        toon.level = int(charInfo[3])
        toon.xp = int(charInfo[4])
        toon.levelUp = int(charInfo[5])
        toon.maxHP = int(charInfo[6])
        toon.hp = int(charInfo[7])
        toon.maxMana = int(charInfo[8])
        toon.mana = int(charInfo[9])
        toon.maxEnergy = int(charInfo[10])
        toon.energy = int(charInfo[11])
        toon.str = int(charInfo[12])
        toon.agi = int(charInfo[13])
        toon.wis = int(charInfo[14])
        toon.luck = int(charInfo[15])
        toon.items[0].qty = int(charInfo[16])
        toon.items[2].qty = int(charInfo[17])
        toon.items[1].qty = int(charInfo[18])
        
    if charInfo[1] == 'Rouge':
        toon = Rouge(charInfo[0])
        toon.damage = int(charInfo[2])
        toon.level = int(charInfo[3])
        toon.xp = int(charInfo[4])
        toon.levelUp = int(charInfo[5])
        toon.maxHP = int(charInfo[6])
        toon.hp = int(charInfo[7])
        toon.maxMana = int(charInfo[8])
        toon.mana = int(charInfo[9])
        toon.maxEnergy = int(charInfo[10])
        toon.energy = int(charInfo[11])
        toon.str = int(charInfo[12])
        toon.agi = int(charInfo[13])
        toon.wis = int(charInfo[14])
        toon.luck = int(charInfo[15])
        toon.items[0].qty = int(charInfo[16])
        toon.items[2].qty = int(charInfo[17])
        toon.items[1].qty = int(charInfo[18])
        
    return toon