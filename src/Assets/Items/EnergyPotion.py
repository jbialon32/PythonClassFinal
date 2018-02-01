'''
Created on Nov 29, 2017

@author: James
'''

class EnergyPotion():
    '''Item used to restore players health'''
    def __init__(self, qty):
        self.item = 'Energy Potion'
        self.qty = qty
        
    def UseEnergyPotion(self, char):
        energy = int(char.maxEnergy/3)
        self.qty -= 1
        return energy