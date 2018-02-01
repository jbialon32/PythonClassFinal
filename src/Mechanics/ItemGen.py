'''
Created on Dec 2, 2017

@author: James
'''

from random import randint

## Random number picker for what will drop off an enemy
def LootDrop(Character, Monster):
    if Character.luck == 1:
        luck = randint(1, 10)
        if luck == 5:
            Character.items[0].qty += 1
        if luck == 7:
            Character.items[1].qty += 1
        if luck == 3:
            Character.items[2].qty += 1
    
    if Character.luck == 2:
        luck = randint(1, 8)
        if luck == 2:
            Character.items[0].qty += 1
        if luck == 4:
            Character.items[1].qty += 1
        if luck == 6:
            Character.items[2].qty += 1