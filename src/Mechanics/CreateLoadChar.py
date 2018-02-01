'''
Created on Nov 2, 2017

@author: jb189417
'''

from pathlib import Path
from os.path import join as PathJoin
import tkinter as tk

'''Starting screen where you choose to create or load your character'''

class CreateLoad:
    
    ''' Creates class list name space and load button each response
        giving off a different choice to the main loader script'''
    
    def __init__(self):
        self.root = tk.Tk()
        self.name = None
        self.classChoice = None
        

    def UserInfo(self, Frame, buttonFrame):
        
        ##Two events for the 2 buttons created for this step of program Load or Create
        
        def CreateCharacter(event):
            self.name = nameEntry.get()
            self.classChoice = classChosen.get()
            root.quit()
            
        def LoadCharacter(event):
            self.classChoice = 'Load'
            root.quit()
            
        root = self.root
        nameLabel = tk.Label(Frame, text='Character Name: ')
        classLabel = tk.Label(Frame, text='Choose A Class: ')
        nameEntry = tk.Entry(Frame)
        
        #variable holding current drop menu choice
        classChosen = tk.StringVar(Frame)
        
        #Dropdown menu choices
        classChoices = ['Warrior', 'Mage', 'Rouge']
        
        ## Sets default choice for drop menu.
        classChosen.set('Warrior')
        
        ## Creates a drop menu containing data from list classChoices
        dropMenu = tk.OptionMenu(Frame, classChosen, *classChoices)
        
        dropMenu.grid(column=1, row=1)
        nameLabel.grid(column=0, row=0, pady=10)
        classLabel.grid(column=0, row=1)
        nameEntry.grid(column=1, row=0, pady=10)
            
        create = tk.Button(buttonFrame,
                           text='Create',
                           bg='green',
                           fg='white',
                           height=2,
                           width=10)
        create.bind('<Button-1>', CreateCharacter)    
        create.grid(column=1, row=0, padx=20, pady=10)
        
        load = tk.Button(buttonFrame,
                           text='Load',
                           bg='green',
                           fg='white',
                           height=2,
                           width=10)
        load.bind('<Button-1>', LoadCharacter)     
        load.grid(column=0, row=0, padx=20, pady=10)
        
    ''' Mainframe holding all information created above '''
    
    def Mainframe(self):
            
        main = tk.Frame(self.root)
        main.pack(expand=True)
        
        main.master.title("Cave Explorer")
        iconPath = 'Assets|Icon|favicon.ico'.split('|')
        iconPath = Path(PathJoin(*iconPath))
        self.root.iconbitmap(iconPath)
        
        topFrame = tk.Frame(main)                       
        bottomFrame = tk.Frame(main)
                                
        topFrame.grid(row=0)
        bottomFrame.grid(row=1)
        
        self.UserInfo(topFrame, bottomFrame)
            
        self.root.mainloop()
        
