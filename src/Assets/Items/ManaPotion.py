'''
Created on Nov 29, 2017

@author: James
'''

class ManaPotion():
    '''Item used to restore players health'''
    def __init__(self, qty):
        self.item = 'Mana Potion'
        self.qty = qty
        
    def UseManaPotion(self, char):
        mana = int(char.maxMana/3)
        self.qty -= 1
        return mana