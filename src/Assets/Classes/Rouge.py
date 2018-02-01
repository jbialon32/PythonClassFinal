'''
Created on Oct 25, 2017

@author: James
'''

from Assets.Items.HealthPotion import HealthPotion
from Assets.Items.ManaPotion import ManaPotion
from Assets.Items.EnergyPotion import EnergyPotion

class Rouge:
    def __init__(self, name):
        self.name = name
        self.className = 'Rouge'
        self.descrip = 'Sneak, steal, and assassinate your way through any obstacle.'
        self.damage = 1
        self.level = 1
        self.xp = 0
        self.levelUp = 5
        self.maxHP = 9
        self.hp = self.maxHP
        self.maxMana = 6
        self.mana = self.maxMana
        self.maxEnergy = 8
        self.energy = self.maxEnergy
        self.str = 1
        self.agi = 3
        self.wis = 2
        self.luck = 2
        self.abilities = ['Swift Strikes', 'Backstab']
        self.hpPotions = HealthPotion(3)
        self.manaPotions = ManaPotion(3)
        self.energyPotions = EnergyPotion(3)
        self.items = [self.hpPotions, self.manaPotions, self.energyPotions]
        
    def __str__(self):
        return '%s' % self.descrip
    
    def Attack(self, other):
        other.hp -= self.damage
        return other.hp

    def LevelUp(self):
        if self.level < 999:                
            if self.xp >= self.levelUp:
                self.level += 1
                self.xp = 0
                self.levelUp = int(self.levelUp * 2)
                self.xp = 0
                self.maxHP += 1
                self.hp += self.maxHP
                self.maxMana += 1
                self.mana = self.maxMana
                self.maxEnergy += 2
                self.energy = self.maxEnergy
                self.damage +=1
                self.str += 2
                self.agi += 2
                self.wis += 1
    
    def AbilityOne(self):
        minLevel = 5
        damageMod = 0
        if self.level >= minLevel:
            damageMod = self.damage * 2
            self.energy -= int(self.energy/5)
        return damageMod
    
    def AbilityTwo(self):
        minLevel = 10
        damageMod = 0
        if self.level >= minLevel:
            damageMod = self.agi
            self.energy -= int(self.energy/3)
        return damageMod