'''
Created on Oct 27, 2017

@author: James
'''

from random import randint
import tkinter as tk
from Mechanics.MonsterLoader import Generate
from Mechanics.UpdateConsoleFeed import SetConsoleFeed as ActionFeed
from Mechanics.Saver import SaveChar
from pathlib import Path
from os.path import join as PathJoin

## Ties everything together in main UI program
class UI:
    
    ## Initiates main variables varName is player controlled character
    def __init__(self, varName=None):
        self.roomNum = 1
        self.varName = varName
        self.monster = Generate()
        while self.monster.minAppear > self.varName.level or self.monster.maxAppear < self.varName.level:
            self.monster = Generate() 
        self.xpGained = False
        self.monsterHp = self.monster.hp
        
    ## Runs check to see if character levels up
    def LevelUpdate(self):
        char = self.varName
        enemy = self.monster
    
        char.xp += enemy.xpValue
        char.LevelUp()
        self.charLevel.set(str(char.level))
        self.charHP.set(str(char.hp))
        self.charMana.set(str(char.mana))
        self.charEnergy.set(str(char.energy))
        
    ## Defines the attack process
    def Attack(self, event=None):
        char = self.varName
        enemy = self.monster
        
        ## Checks if attack button is enabled
        if str(self.atkButton['state']) == 'normal':
            
            ## If the enemy enemy and player is alive continue
            if enemy.hp > 0 and char.hp > 0:
                self.monsterHp = char.Attack(enemy)
                ActionFeed('You attack %s.' % enemy.name, self.updatePane) 
                
                ##  If monster is dead...
                if self.monsterHp <= 0:
                    enemy.hp = 0
                    self.monster.Loot(self.varName)
                    self.monHP.set(str(enemy.hp))
                    self.LevelUpdate()
                    self.xpGained = True
                    ActionFeed('You killed %s' % enemy.name, self.updatePane)
                    
                ## if monster is alive they strike back
                elif self.monsterHp > 0:
                    self.monHP.set(str(enemy.hp))
                    self.hp = enemy.Attack(char)
                
                ## If character is dead update consoles text
                if self.varName.hp < 0:
                    char.hp = 0
                    ActionFeed('You are dead.', self.updatePane)
                
                ## Updates players current health
                self.charHP.set(str(char.hp))
                
            ## If enemy is dead and player is alive and the xp hasn't been gained  
            elif enemy.hp == 0 and self.xpGained == False:
                self.LevelUpdate()
                self.xpGained = True
                ActionFeed('You killed %s' % enemy.name, self.updatePane)
                
            ## If enemy is dead and xp has been gained you do not gain more xp...
            elif enemy.hp == 0 and self.xpGained == True:
                ActionFeed('%s is dead' % enemy.name, self.updatePane)
                
            ## If you are dead you can't attack
            elif  char.hp == 0:
                ActionFeed("You can't attack while dead.", self.updatePane)
    
    ## Creates Room label feature giving current room character is in            
    def RoomLabel(self, Frame):
        self.roomNumber = tk.StringVar()
        
        roomLabel1 = tk.Label(Frame, text=('Room: '))
        roomLabel1.grid(column=0, row=0)
        
        roomLabel2 = tk.Label(Frame, textvariable=self.roomNumber)
        self.roomNumber.set(str(self.roomNum))
        roomLabel2.grid(column=1, row=0)
    
    ## Gives functionality to the abilities button by showing frame
    def CharAbilities(self, Frame):
        
        ## Hides frame when closed and returns button states to normal
        def HideCharAbilities(event):
            self.charButton.configure(state='normal')
            self.charButton.configure(state='normal')
            self.atkButton.configure(state='normal')
            self.menuButton.configure(state='normal')
            self.nextRoomButton.configure(state='normal')
            self.abilityButton.configure(state='normal')
            self.itemsButton.configure(state='normal')
            charAbilitiesFrame.place_forget()
            
        ## Checks characters first ability requirements    
        def UseAbilityOne(event):
            char = self.varName
            enemy = self.monster
            abilityOne = char.AbilityOne()
            
            ## If character meets requirements use ability much like attack function earlier
            if abilityOne > 0:
                if enemy.hp > 0 and char.hp > 0:
                    self.monsterHp -= char.AbilityOne()
                    enemy.hp = self.monsterHp
                    self.monster.Loot(self.varName)
                    self.charHP.set(str(char.hp))
                    self.charEnergy.set(str(self.varName.energy))
                    self.charMana.set(str(self.varName.mana))
                    ActionFeed('You use %s.' % char.abilities[0], self.updatePane) 
                    if self.monsterHp <= 0:
                        enemy.hp = 0
                        self.monHP.set(str(enemy.hp))
                        self.LevelUpdate()
                        self.xpGained = True
                        ActionFeed('You killed %s' % enemy.name, self.updatePane)
                    elif self.monsterHp > 0:
                        self.monHP.set(str(enemy.hp))
                        self.hp = enemy.Attack(char)
                    if self.varName.hp < 0:
                        char.hp = 0
                        ActionFeed('You are dead.', self.updatePane)
                    self.charHP.set(str(char.hp))
                elif enemy.hp == 0 and self.xpGained == False:
                    self.LevelUpdate()
                    self.xpGained = True
                    ActionFeed('You killed %s' % enemy.name, self.updatePane)
                elif enemy.hp == 0 and self.xpGained == True:
                    ActionFeed('%s is dead' % enemy.name, self.updatePane)
                elif  char.hp == 0:
                    ActionFeed("You can't attack while dead.", self.updatePane)
                
            ## If character does not meet requirements ability is not casted
            if abilityOne == 0:
                ActionFeed('You must be level 5 to use %s.' % char.abilities[0], self.updatePane)
        
        ## SEE USEABILITYONE
        def UseAbilityTwo(event):
            char = self.varName
            enemy = self.monster
            abilityTwo = char.AbilityTwo()
            if abilityTwo > 0:
                if enemy.hp > 0 and char.hp > 0:
                    self.monsterHp -= char.AbilityTwo()
                    enemy.hp = self.monsterHp
                    self.monster.Loot(self.varName)
                    self.charHP.set(str(char.hp))
                    self.charEnergy.set(str(self.varName.energy))
                    self.charMana.set(str(self.varName.mana))
                    ActionFeed('You use %s.' % char.abilities[1], self.updatePane) 
                    if self.monsterHp <= 0:
                        enemy.hp = 0
                        self.monHP.set(str(enemy.hp))
                        self.LevelUpdate()
                        self.xpGained = True
                        ActionFeed('You killed %s' % enemy.name, self.updatePane)
                    elif self.monsterHp > 0:
                        self.monHP.set(str(enemy.hp))
                        self.hp = enemy.Attack(char)
                    if self.varName.hp < 0:
                        char.hp = 0
                        ActionFeed('You are dead.', self.updatePane)
                    self.charHP.set(str(char.hp))
                elif enemy.hp == 0 and self.xpGained == False:
                    self.LevelUpdate()
                    self.xpGained = True
                    ActionFeed('You killed %s' % enemy.name, self.updatePane)
                elif enemy.hp == 0 and self.xpGained == True:
                    ActionFeed('%s is dead' % enemy.name, self.updatePane)
                elif  char.hp == 0:
                    ActionFeed("You can't attack while dead.", self.updatePane)
            
            if abilityTwo == 0:
                ActionFeed('You must be level 10 to use %s.' % char.abilities[1], self.updatePane)
        
        ## Sets up a close button to be used
        def CloseButton(Frame, GridColumn, GridRow):
            close = tk.Button(Frame,
                              text='Close',
                              bg='red',
                              fg='white')
            
            ## Binds close button with HideCharAbilities
            close.bind('<Button-1>', HideCharAbilities)
            close.grid(column=GridColumn, row=GridRow, padx=3, pady=3)
        
        ## Puts together everything based off of characters own attributes
            
        char = self.varName
            
        charAbilitiesFrame = tk.Frame(Frame)
        charAbilitiesFrame.place(x=0, y=170)
        
        ## Creates ability buttons
            
        ability1 = tk.Button(charAbilitiesFrame,
                            text='None',
                            bg='green',
                            fg='white',
                            height=3,
                            width=14)    
        ability1.bind('<Button-1>', UseAbilityOne)
            
        ability2 = tk.Button(charAbilitiesFrame,
                            text='None',
                            bg='green',
                            fg='white',
                            height=3,
                            width=14)    
        ability2.grid(column=0, row=1, padx=7)
        ability2.bind('<Button-1>', UseAbilityTwo)
            
        buttons = [ability1, ability2]
        
        ## For loop creating ability buttons with corresponding skills
            
        for ability in range(len(char.abilities)):
            buttons[ability].configure(text=char.abilities[ability])
            
        ability1.grid(column=0, row=0, padx=7, pady=7)
        ability2.grid(column=0, row=1, padx=7, pady=7)
        
        ## Implements Close Button
            
        CloseButton(charAbilitiesFrame, 0, 2)
    
    ## Create Menu button functionality
    def Menu(self, Frame):
        
        def HideMenu(event):
            self.charButton.configure(state='normal')
            self.charButton.configure(state='normal')
            self.atkButton.configure(state='normal')
            self.menuButton.configure(state='normal')
            self.nextRoomButton.configure(state='normal')
            self.abilityButton.configure(state='normal')
            self.itemsButton.configure(state='normal')
            menuFrame.place_forget()
        
        ## Implements save script as button event
        def Save(event):
            SaveChar(self.varName)
            
        def CloseButton(Frame, GridColumn, GridRow):
            close = tk.Button(Frame,
                              text='Close',
                            bg='red',
                                fg='white')
                
            close.bind('<Button-1>', HideMenu)
            close.grid(column=GridColumn, row=GridRow, padx=3, pady=3)
                
        menuFrame = tk.Frame(Frame)
        menuFrame.place(x=0, y=170)
                
        saveGame = tk.Button(menuFrame,
                              text='Save',
                              bg='green',
                              fg='white',
                              height=3,
                              width=14)    
        saveGame.bind('<Button-1>', Save)
            
        saveGame.grid(column=0, row=0, padx=7, pady=7)
                
        CloseButton(menuFrame, 0, 1)
    
    ## Inventory functionality    
    def Inventory(self, Frame):
        def HideInventory(event):
            self.charButton.configure(state='normal')
            self.charButton.configure(state='normal')
            self.atkButton.configure(state='normal')
            self.menuButton.configure(state='normal')
            self.nextRoomButton.configure(state='normal')
            self.abilityButton.configure(state='normal')
            self.itemsButton.configure(state='normal')
            inventoryFrame.place_forget()
        
        ## Uses health potion from characters inventory
        def UseHpPot(event):
            
            ## Checks if character is at max health
            if self.varName.hp != self.varName.maxHP:
                
                ## If character is dead no heals
                if self.varName.hp == 0:
                    ActionFeed('You are dead.', self.updatePane)
                    
                ## If character is alive and has potions thar be heals m8y.
                if self.varName.items[0].qty > 0 and self.varName.hp > 0:
                    self.varName.hp += self.varName.items[0].UseHealthPotion(self.varName)
                    self.charHP.set(str(self.varName.hp))
                    ActionFeed('You use a Health Potion', self.updatePane)
                    item1.config(text='Health Potion x %s' % str(self.varName.items[0].qty))
                    
                    ## If overhealed reduces to characters max possible health
                    if self.varName.hp > self.varName.maxHP:
                        self.varName.hp = self.varName.maxHP
                
                ## If out of potions no heals for you.
                if self.varName.items[0].qty == 0:
                    ActionFeed('You have no Health Potions', self.updatePane)
                    
            ## Stops user from wasting potions while at full health.
            if self.varName.hp == self.varName.maxHP:
                    ActionFeed('You are already at max health.', self.updatePane)
                
        ## SEE USEHEALTHPOT
        def UseManaPot(event):
            if self.varName.mana != self.varName.maxMana:
                if self.varName.hp == 0:
                    ActionFeed('You are dead.', self.updatePane)
                if self.varName.items[1].qty > 0 and self.varName.hp > 0:
                    self.varName.hp += self.varName.items[1].UseManaPotion(self.varName)
                    self.charMana.set(str(self.varName.mana))
                    ActionFeed('You use a Mana Potion', self.updatePane)
                    item2.config(text='Mana Potion x %s' % str(self.varName.items[1].qty))
                    if self.varName.mana > self.varName.maxMana:
                        self.varName.mana = self.varName.maxMana
                if self.varName.items[1].qty == 0:
                    ActionFeed('You have no Mana Potions', self.updatePane)
            if self.varName.mana == self.varName.maxMana:
                    ActionFeed('You are at max mana.', self.updatePane)
        
        ## SEE USEHEALTHPOT        
        def UseEnergyPot(event):
            if self.varName.energy != self.varName.maxEnergy:
                if self.varName.hp == 0:
                    ActionFeed('You are dead.', self.updatePane)
                if self.varName.items[2].qty > 0 and self.varName.hp > 0:
                    self.varName.hp += self.varName.items[2].UseEnergyPotion(self.varName)
                    self.charHP.set(str(self.varName.hp))
                    ActionFeed('You use an Energy Potion', self.updatePane)
                    item3.config(text='Energy Potion x %s' % str(self.varName.items[2].qty))
                    if self.varName.energy > self.varName.maxEnergy:
                        self.varName.energy = self.varName.maxEnergy
                if self.varName.items[2].qty == 0:
                    ActionFeed('You have no Energy Potions', self.updatePane)
            if self.varName.energy == self.varName.maxEnergy:
                    ActionFeed('You are at max energy.', self.updatePane)
                
        def CloseButton(Frame, GridColumn, GridRow):
            close = tk.Button(Frame,
                              text='Close',
                              bg='red',
                              fg='white')
            
            close.bind('<Button-1>', HideInventory)
            close.grid(column=GridColumn, row=GridRow, padx=3, pady=3)
                
        inventoryFrame = tk.Frame(Frame)
        inventoryFrame.place(x=0, y=350)
            
        item1 = tk.Button(inventoryFrame,
                            text=('Health Potion x %s' % str(self.varName.items[0].qty)),
                            bg='green',
                            fg='white',
                            height=3,
                            width=14)    
        item1.bind('<Button-1>', UseHpPot)
        
        item2 = tk.Button(inventoryFrame,
                            text=('Mana Potion x %s' % str(self.varName.items[1].qty)),
                            bg='green',
                            fg='white',
                            height=3,
                            width=14)    
        item2.bind('<Button-1>', UseManaPot)
        
        item3 = tk.Button(inventoryFrame,
                            text=('Energy Potion x %s' % str(self.varName.items[2].qty)),
                            bg='green',
                            fg='white',
                            height=3,
                            width=14)    
        item3.bind('<Button-1>', UseEnergyPot)
        
        item1.grid(column=0, row=0, padx=7, pady=7)
        item2.grid(column=1, row=0, padx=7, pady=7)
        item3.grid(column=2, row=0, padx=7, pady=7)
            
        CloseButton(inventoryFrame, 3, 1)
    
    ## Builds frame for extra character information
    def CharDetail(self, Frame):
        def HideCharInfo(event):
            self.charButton.configure(state='normal')
            self.charButton.configure(state='normal')
            self.atkButton.configure(state='normal')
            self.menuButton.configure(state='normal')
            self.nextRoomButton.configure(state='normal')
            self.abilityButton.configure(state='normal')
            self.itemsButton.configure(state='normal')
            charDetailFrame.place_forget()
            
        def CloseButton(Frame, GridColumn, GridRow):
            close = tk.Button(Frame,
                              text='Close',
                              bg='red',
                              fg='white')
            
            close.bind('<Button-1>', HideCharInfo)
            close.grid(column=GridColumn, row=GridRow, padx=3, pady=3)
            
        char = self.varName
        
        charDetailFrame = tk.Frame(Frame)
        charDetailFrame.place(x=0, y=170)
        
        infoLabelFrame = tk.Frame(charDetailFrame)
        infoLabelFrame.grid(column=0, row=0, padx=10)
        
        infoStatsFrame = tk.Frame(charDetailFrame)
        infoStatsFrame.grid(column=1, row=0, padx=10)
        
        nameLabelMenu = tk.Label(infoLabelFrame, text=('%11s' % 'Name:'))
        classLabelMenu = tk.Label(infoLabelFrame, text=('%11s' % 'Class:'))
        levelLabelMenu = tk.Label(infoLabelFrame, text=('%11s' % 'Level:'))
        hpLabelMenu = tk.Label(infoLabelFrame, text=('%11s' % 'Health:'))
        manaLabelMenu = tk.Label(infoLabelFrame, text=('%11s' % 'Mana:'))
        energyLabelMenu = tk.Label(infoLabelFrame, text=('%11s' % 'Energy:'))
        xpLabelMenu = tk.Label(infoLabelFrame, text=('%11s' % 'XP:'))
        xpReqLabelMenu = tk.Label(infoLabelFrame, text=('%11s' % 'Level up:'))
        strLabelMenu = tk.Label(infoLabelFrame, text=('%11s' % 'Str:'))
        agiLabelMenu = tk.Label(infoLabelFrame, text=('%11s' % 'Agi:'))
        wisLabelMenu = tk.Label(infoLabelFrame, text=('%11s' % 'Wis:'))
        luckLabelMenu = tk.Label(infoLabelFrame, text=('%11s' % 'Luck:'))
        
        nameLabelMenu.grid(column=0, row=0)
        classLabelMenu.grid(column=0, row=1)
        levelLabelMenu.grid(column=0, row=2)
        xpLabelMenu.grid(column=0, row=3)
        xpReqLabelMenu.grid(column=0, row=4)
        hpLabelMenu.grid(column=0, row=5)
        manaLabelMenu.grid(column=0, row=6)
        energyLabelMenu.grid(column=0, row=7)
        strLabelMenu.grid(column=0, row=8)
        agiLabelMenu.grid(column=0, row=9)
        wisLabelMenu.grid(column=0, row=10)
        luckLabelMenu.grid(column=0, row=111) 
        
        self.charNameMenu = tk.StringVar()
        self.classNameMenu = tk.StringVar()
        self.charLevelMenu = tk.StringVar()
        self.charHPMenu = tk.StringVar()
        self.charXPMenu = tk.StringVar()
        self.charXpReqMenu = tk.StringVar()
        self.charStrMenu = tk.StringVar()
        self.charAgiMenu = tk.StringVar()
        self.charWisMenu = tk.StringVar()
        self.charLuckMenu = tk.StringVar()
        self.charEnergyMenu = tk.StringVar()
        self.charManaMenu = tk.StringVar()
        
        nameStatMenu = tk.Label(infoStatsFrame, textvariable=self.charNameMenu)
        classNameMenu = tk.Label(infoStatsFrame, textvariable=self.classNameMenu)
        levelStatMenu = tk.Label(infoStatsFrame, textvariable=self.charLevelMenu)
        hpStatMenu = tk.Label(infoStatsFrame, textvariable=self.charHPMenu)
        xpStatMenu = tk.Label(infoStatsFrame, textvariable=self.charXPMenu)
        xpReqStatMenu = tk.Label(infoStatsFrame, textvariable=self.charXpReqMenu)
        manaStatMenu = tk.Label(infoStatsFrame, textvariable=self.charManaMenu)
        energyStatMenu = tk.Label(infoStatsFrame, textvariable=self.charEnergyMenu)
        strStatMenu = tk.Label(infoStatsFrame, textvariable=self.charStrMenu)
        agiStatMenu = tk.Label(infoStatsFrame, textvariable=self.charAgiMenu)
        wisStatMenu = tk.Label(infoStatsFrame, textvariable=self.charWisMenu)
        luckStatMenu = tk.Label(infoStatsFrame, textvariable=self.charLuckMenu)
        
        self.charNameMenu.set(str(char.name))
        self.classNameMenu.set(str(char.className))
        self.charLevelMenu.set(str(char.level))
        self.charHPMenu.set(str(char.hp))
        self.charXPMenu.set(str(char.xp))
        self.charXpReqMenu.set(str(char.levelUp))
        self.charManaMenu.set(str(char.mana))
        self.charEnergyMenu.set(str(char.energy))
        self.charStrMenu.set(str(char.str))
        self.charAgiMenu.set(str(char.agi))
        self.charWisMenu.set(str(char.wis))
        self.charLuckMenu.set(str(char.luck))
        
        nameStatMenu.grid(column=0, row=0)
        classNameMenu.grid(column=0, row=1)
        levelStatMenu.grid(column=0, row=2)
        xpStatMenu.grid(column=0, row=3)
        xpReqStatMenu.grid(column=0, row=4)
        hpStatMenu.grid(column=0, row=5)
        manaStatMenu.grid(column=0, row=6)
        energyStatMenu.grid(column=0, row=7)
        strStatMenu.grid(column=0, row=8)
        agiStatMenu.grid(column=0, row=9)
        wisStatMenu.grid(column=0, row=10)
        luckStatMenu.grid(column=0, row=11)
        
        CloseButton(charDetailFrame, 1, 5)
    
    ## Shows basic character stats on main UI no menu    
    def CharInfo(self, Frame): 
        char = self.varName
          
        infoLabelFrame = tk.Frame(Frame,
                                   width=200,
                                   height=50)
        infoLabelFrame.grid(column=4, row=0, padx=10) 
        
        nameLabel = tk.Label(infoLabelFrame, text=('%9s' % 'Name:'))
        levelLabel = tk.Label(infoLabelFrame, text=('%9s' % 'Level:'))
        hpLabel = tk.Label(infoLabelFrame, text=('%9s' % 'Health:'))
        manaLabel = tk.Label(infoLabelFrame, text=('%9s' % 'Mana:'))
        energyLabel = tk.Label(infoLabelFrame, text=('%s' % 'Energy:'))
        
        nameLabel.grid(column=0, row=0)
        levelLabel.grid(column=0, row=1)
        hpLabel.grid(column=0, row=2)
        manaLabel.grid(column=0, row=3)
        energyLabel.grid(column=0, row=4)
        
        infoStatsFrame = tk.Frame(Frame,
                                  width=200,
                                  height=50)
        infoStatsFrame.grid(column=5, row=0, padx=10)
        
        self.charName = tk.StringVar()
        self.charLevel = tk.StringVar()
        self.charHP = tk.StringVar()
        self.charMana = tk.StringVar()
        self.charEnergy = tk.StringVar()
        
        nameStat = tk.Label(infoStatsFrame, textvariable=self.charName)
        levelStat = tk.Label(infoStatsFrame, textvariable=self.charLevel)
        hpStat = tk.Label(infoStatsFrame, textvariable=self.charHP)
        manaStat = tk.Label(infoStatsFrame, textvariable=self.charMana)
        energyStat = tk.Label(infoStatsFrame, textvariable=self.charEnergy)
        
        self.charName.set(str(char.name))
        self.charLevel.set(str(char.level))
        self.charHP.set(str(char.hp))
        self.charMana.set(str(char.mana))
        self.charEnergy.set(str(char.energy))
         
        nameStat.grid(column=0, row=0)
        levelStat.grid(column=0, row=1)
        hpStat.grid(column=0, row=2)
        manaStat.grid(column=0, row=3)
        energyStat.grid(column=0, row=4)
        
    ## Basic Monster information embeded in main UI
    def MonsterInfo(self, Frame):
        mon = self.monster
        
        labelFrameMonster = tk.Frame(Frame,
                                    width=200,
                                    height=50)
        labelFrameMonster.grid(column=6, row=0, padx=10)
        
        monsterNameLabel = tk.Label(labelFrameMonster, text=('%10s' % 'Enemy: '))
        monsterHPLabel = tk.Label(labelFrameMonster, text=('%10s' % 'Enemy HP: '))
        monsterNameLabel.grid(column=0, row=0)
        monsterHPLabel.grid(column=0, row=1)
                                    
        infoFrameMonster = tk.Frame(Frame,
                                    width=200,
                                    height=50)
        infoFrameMonster.grid(column=7, row=0, padx=10)
                                    
        self.monName = tk.StringVar()
        monsterNameInfo = tk.Label(infoFrameMonster, textvariable=self.monName)
        self.monName.set(str(mon.name))
        
        self.monHP = tk.StringVar()
        monsterHpinfo = tk.Label(infoFrameMonster, textvariable=self.monHP)
        self.monHP.set(str(mon.hp))
        
        monsterNameInfo.grid(column=0, row=0)
        monsterHpinfo.grid(column=0, row=1)
    
    ## Main UI builds everything and ties it all together    
    def mainGame(self):
        
        def ShowCharInfo(event):
            if str(self.charButton['state']) == 'normal':
                self.CharDetail(bigPicture)
                self.charButton.configure(state='disabled')
                self.atkButton.configure(state='disabled')
                self.menuButton.configure(state='disabled')
                self.nextRoomButton.configure(state='disabled')
                self.abilityButton.configure(state='disabled')
                self.itemsButton.configure(state='disabled')
                
        def ShowCharAbilities(event):
            if str(self.abilityButton['state']) == 'normal':
                self.CharAbilities(bigPicture)
                self.charButton.configure(state='disabled')
                self.atkButton.configure(state='disabled')
                self.menuButton.configure(state='disabled')
                self.nextRoomButton.configure(state='disabled')
                self.abilityButton.configure(state='disabled')
                self.itemsButton.configure(state='disabled')
                
        def ShowInventory(event):
            if str(self.itemsButton['state']) == 'normal':
                self.Inventory(bigPicture)
                self.charButton.configure(state='disabled')
                self.atkButton.configure(state='disabled')
                self.menuButton.configure(state='disabled')
                self.nextRoomButton.configure(state='disabled')
                self.abilityButton.configure(state='disabled')
                self.itemsButton.configure(state='disabled')
                
        def ShowMenu(event):
            if str(self.menuButton['state']) == 'normal':
                self.Menu(bigPicture)
                self.charButton.configure(state='disabled')
                self.atkButton.configure(state='disabled')
                self.menuButton.configure(state='disabled')
                self.nextRoomButton.configure(state='disabled')
                self.abilityButton.configure(state='disabled')
                self.itemsButton.configure(state='disabled')

        def NextRoom(event):
            if str(self.nextRoomButton['state']) == 'normal':
                char = self.varName
                mon = self.monster
                
                if mon.hp <= 0:
                    self.roomNum += 1
                    self.roomNumber.set(str(self.roomNum))
                    self.monster = Generate()
                    while self.monster.minAppear > self.varName.level or self.monster.maxAppear < self.varName.level:
                        self.monster = Generate()
                    mon = self.monster
                    self.monName.set(str(mon.name))
                    self.monHP.set(str(mon.hp))
                    self.monsterHp = self.monster.hp
                    caveChoice = randint(0, 1)
                    ActionFeed('You move ahead.', self.updatePane)
                    
                    if caveChoice == 0:
                        bgPath = mon.cave1
                        background_image=tk.PhotoImage(file=bgPath)
                        background_label.configure(image=background_image)
                        background_label.image = background_image
                        
                    if caveChoice == 1:
                        if self.monster.cave2 == None:
                            bgPath = mon.cave1
                            background_image=tk.PhotoImage(file=bgPath)
                            background_label.configure(image=background_image)
                            background_label.image = background_image
                        else:
                            bgPath = mon.cave2
                            background_image=tk.PhotoImage(file=bgPath)
                            background_label.configure(image=background_image)
                            background_label.image = background_image
                             
                elif char.hp <= 0:
                    ActionFeed('You cannot move while dead.', self.updatePane)
                
                elif char.hp >= 0 and mon.hp >= 0:
                    ActionFeed('The enemy blocks your path.', self.updatePane)
            
        root = tk.Tk()
        
        mainFrame = tk.Frame(root,
                             width=800,
                             height=600)
        mainFrame.pack(expand=True)
        
        mainFrame.master.title("Cave Explorer")
        iconPath = 'Assets|Icon|favicon.ico'.split('|')
        iconPath = Path(PathJoin(*iconPath))
        root.iconbitmap(iconPath)
        
        mainFrame.columnconfigure(0, weight=1)
        mainFrame.rowconfigure(0, weight=0)
        mainFrame.rowconfigure(1, weight=1)
        mainFrame.rowconfigure(2, weight=0)
        
        bigPicture = tk.Frame(mainFrame,
                             width=800,
                             height=450,
                             bg='blue')
        bigPicture.grid(column=0,
                        row=1)
        
        topFrame = tk.Frame(mainFrame,
                            width=800,
                            height=100)
        topFrame.grid(column=0, row=0)
        
        gameConsoleFrame = tk.Frame(mainFrame,
                                    width=800,
                                    height=100)
        gameConsoleFrame.grid(row=2)
        
        self.updatePane = tk.StringVar()
        updateLabel = tk.Label(gameConsoleFrame, textvar=self.updatePane)
        updateLabel.pack()
        
        bottomFrame = tk.Frame(mainFrame,
                               width=800,
                               height=50)
        bottomFrame.grid(column=0, row=3)
        
        self.charButton = tk.Button(bottomFrame,
                               text='Character',
                               bg='green',
                               fg='white',
                               height=3,
                               width=9)
        self.charButton.bind('<Button-1>', ShowCharInfo)
        self.charButton.grid(column=1, row=0, padx=7)
        
        self.nextRoomButton = tk.Button(bottomFrame,
                                   text='Move',
                                   bg='green',
                                   fg='white',
                                   height=3,
                                   width=9)
        self.nextRoomButton.bind('<Button-1>', NextRoom)
        self.nextRoomButton.grid(column=2, row=0, padx=7)
        
        self.atkButton = tk.Button(bottomFrame,
                              text='Attack',
                              bg='green',
                              fg='white', 
                              height=3,
                              width=10)
        self.atkButton.bind('<Button-1>', self.Attack)
        self.atkButton.grid(column=8, row=0, padx=9)
        
        self.abilityButton = tk.Button(bottomFrame,
                                  text='Abilities',
                                  bg='green',
                                  fg='white',
                                  height=3,
                                  width=10)
        self.abilityButton.bind('<Button-1>', ShowCharAbilities)
        self.abilityButton.grid(column=9, row=0, padx=7)
        
        self.menuButton = tk.Button(bottomFrame,
                               text='Menu',
                               bg='green',
                               fg='white',
                               height=3,
                               width=9)
        self.menuButton.bind('<Button-1>', ShowMenu)      
        self.menuButton.grid(column=0, row=0, padx=7)
        
        self.itemsButton = tk.Button(bottomFrame,
                                text='Items',
                                bg='green',
                                fg='white',
                                height=3,
                                width=9)
        self.itemsButton.bind('<Button-1>', ShowInventory)    
        self.itemsButton.grid(column=10, row=0, padx=7)
        
        bgPath = self.monster.cave1
        background_image=tk.PhotoImage(file=bgPath)  
        background_label = tk.Label(bigPicture, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.RoomLabel(topFrame)
        self.CharInfo(bottomFrame)
        self.MonsterInfo(bottomFrame)

        root.mainloop()
