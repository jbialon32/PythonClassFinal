'''
Created on Nov 29, 2017

@author: James
'''

from pathlib import Path
from os.path import join as PathJoin

## Writes character information to a text file
def SaveChar(Character):
    saveFile = open('Assets/Saves/Test.txt')
    writeSave = open(saveFile, 'w')
    name = str(Character.name)
    charClass = str(Character.className)
    damage = str(Character.damage)
    level = str(Character.level)
    xp = str(Character.xp)
    xpReq = str(Character.levelUp)
    maxHp = str(Character.maxHP)
    hp = str(Character.hp)
    maxMana = str(Character.maxMana)
    mana = str(Character.mana)
    maxEnergy = str(Character.maxEnergy)
    energy = str(Character.energy)
    strength = str(Character.str)
    agi = str(Character.agi)
    wis = str(Character.wis)
    luck = str(Character.luck)
    healthPotions = str(Character.items[0].qty)
    energyPotions = str(Character.items[2].qty)
    manaPotions = str(Character.items[1].qty)
    ## Format of save file
    textLines = ['0NAME|1CLASS|2DAMAGE|3LEVEL|4XP|5LEVELUP|6MAXHP|7HP|8MAXMANA|9MANA|10MAXENERGY|11ENERGY|12STR|13AGI|14WIS|15LUCK|16hpPots|17energyPots|18manaPots\n',
                 name+'|'+charClass+'|'+damage+'|'+level+'|'+xp+'|'+xpReq+'|'+maxHp+'|'+hp+'|'+maxMana+'|'+mana+'|'+maxEnergy+'|'+energy+'|'+strength+'|'+agi+'|'+wis+'|'+luck+'|'+healthPotions+'|'+energyPotions+'|'+manaPotions]
    writeSave.writelines(textLines)
    writeSave.close()