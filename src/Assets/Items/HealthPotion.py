'''
Created on Nov 28, 2017

@author: James
'''

class HealthPotion():
    '''Item used to restore players health'''
    def __init__(self, qty):
        self.item = 'Health Potion'
        self.qty = qty
        
    def UseHealthPotion(self, char):
        hp = int(char.maxHP/3)
        self.qty -= 1
        return hp
        
    
    