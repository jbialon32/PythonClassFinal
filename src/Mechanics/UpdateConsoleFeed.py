'''
Created on Nov 27, 2017

@author: James
'''

## Writes and reads to games text alerts
def SetConsoleFeed(Text, ConsoleFeed):
    ''' Update players feed in the UI
        Text = Text you want in feed
        ConsoleFeed = Tkinter TextVar '''
    
    writeGameConsole = open('gameConsole.txt', 'w')
    writeGameConsole.write(Text)
    writeGameConsole.close()
    readGameConsole = open('gameConsole.txt', 'r')
    text = readGameConsole.read()
    readGameConsole.close()
    ConsoleFeed.set(str(text))