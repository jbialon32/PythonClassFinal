'''
Created on Oct 25, 2017

@author: James
'''

from Assets.Items.HealthPotion import HealthPotion
from Assets.Items.ManaPotion import ManaPotion
from Assets.Items.EnergyPotion import EnergyPotion

class Mage:
    def __init__(self, name):
        self.name = name
        self.className = 'Mage'
        self.descrip = 'Manipulate the powers of mana to turn the tides of battle.'
        self.damage = 1
        self.level = 1
        self.xp = 0
        self.levelUp = 5
        self.maxHP = 7
        self.hp = self.maxHP
        self.maxMana = 12
        self.mana = self.maxMana
        self.maxEnergy = 4
        self.energy = self.maxEnergy
        self.str = 1
        self.agi = 2
        self.wis = 3
        self.luck = 1
        self.abilities = ['Arcane Bolt', 'Arcane Volley']
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
                self.mana += 3
                self.energy += 2
                self.damage += 1
                self.str += 1
                self.agi += 2
                self.wis += 3
            
    def AbilityOne(self):
        minLevel = 5
        damageMod = 0
        if self.level >= minLevel:
            damageMod = self.damage * 2
            self.mana -= int(self.mana/5)
        return damageMod
    
    def AbilityTwo(self):
        minLevel = 10
        damageMod = 0
        if self.level >= minLevel:
            damageMod = self.wis
            self.mana -= int(self.mana/3)
        return damageMod