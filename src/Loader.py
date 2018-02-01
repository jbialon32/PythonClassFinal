'''
Created on Oct 27, 2017

@author: James
'''

from Mechanics.UI import UI
from Mechanics.CreateLoadChar import CreateLoad
from Mechanics.Load import Load
from Assets.Classes.Warrior import Warrior
from Assets.Classes.Mage import Mage
from Assets.Classes.Rouge import Rouge

''' Ties character creator/loader and main game ui together'''

## Calls create load window

create = CreateLoad()
create.Mainframe()

## upon hitting load or create returns info for loading or creating the correct class


## WARRIOR
if create.classChoice == 'Warrior':
    name = create.name
    #Destroys the create load screen allowing for the main UI to be usable
    create.root.destroy()
    toon = Warrior(name)

## MAGE
if create.classChoice == 'Mage':
    name = create.name
    create.root.destroy()
    toon = Mage(name)

## ROUGE    
if create.classChoice == 'Rouge':
    name = create.name
    create.root.destroy()
    toon = Rouge(name)

## Calls the load function
if create.classChoice == 'Load':
    create.root.destroy()
    toon = Load()
    
## Calls main games UI passing in the players character

try:           
    main = UI(varName=toon)

    main.mainGame()
    
except NameError:
    None