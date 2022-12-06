from tkinter import font, Tk, constants, Canvas
from tkinter.ttk import *
import time
#from game import TicTacToe, play
#from dPlayer import HumanPlayer
'''
def generatePos(game, letter):
    if letter == 'O':
        nextLetter = 'X' 
        player = x_player
     else 'O'
    _,state_list = player.minimax(game,nextLetter)
'''

def setNextMove(player):
    pass

#function identifying the first differing index between 2 lists of equal length
def funcFirstDiffIndex(lsOne, lsTwo):
    for i in range(len(lsOne)):
        if lsOne[i] != lsTwo[i]:
            return str(i)
    return str(-1)

#function generating future boards along with the associated minimax score
def funcGenBoard(root, style, dictState, lsCurrent):
    frameState = Frame(root, style = style['Frame'])
    frameBoard = Frame(frameState, padding = 5, style = style['Frame'])
    lsButtonStore = []
    for item in dictState['position']:
        lsButtonStore.append(Button(frameBoard, width = 2, text = item, style = style['Button']))
    #button position assignment
    num = 0
    for i in range(3):
        for j in range(3):
            lsButtonStore[num].grid(row = i, column = j)
            num += 1
    #identify new position to retrieve 
    strNext = funcFirstDiffIndex(dictState['position'], lsCurrent) 
    frameBoard.grid(row = 0, column = 0)
    Label(frameState, text = 'P:' + strNext + '\n'+ str(dictState['score']), width = 3, style = style['Label'], padding = 3).grid(row = 0, column = 1)
    return frameState
 
#function generating the right panel of possible next moves
def funcBoardFrames(root, style, lsStates, lsCurrent):
    frameDisplay = Frame(root)
    i = 0
    j = 0
    for dictState in lsStates: #placing each possible future board in columns of 4
        if i < 4:
            i += 1
            funcGenBoard(frameDisplay, style, dictState, lsCurrent).grid(row = i, column = j)
        else:
            i = 1
            j += 1
            funcGenBoard(frameDisplay, style, dictState, lsCurrent).grid(row = i, column = j)
    Label(frameDisplay, text = 'Possible Moves', style = style['Label']).grid(row = 0, column = 0, columnspan = j+1)
    return frameDisplay

def updateNextMove(player, move):
    player.nextMove = move

def funcMainBoard(root,style,lsBoard,player):
    frameMain = Frame(root, style = style['Frame'])
    frameBoard = Frame(frameMain, style = style['Frame'])
    Label(frameMain, text = 'Current Move:', style = style['Label']).grid(row = 0, column = 0)
    lsButtonStore = []
    for move,item in enumerate(lsBoard):
        lsButtonStore.append(Button(frameBoard, width = 2, text = item, command=lambda:updateNextMove(player,move), style = style['Button']))
    num = 0
    for i in range(3):
        for j in range(3):
            lsButtonStore[num].grid(row = i, column = j)
            num += 1
    frameBoard.grid(row = 1, column = 0)
    return frameMain

def funcVictoryLabel(root, style, victor):
    return Label(root, style = style['Label'], text = victor + ' wins!')

def funcClearContainer(root):
    for child in root.winfo_children():
        child.destroy()

if __name__ == '__main__':
    tkWindow = Tk()
    tkWindow.title('Tic Tac Toe?')

    #Colours & fonts for the UI
    style = {'Button' : 'Yee.TButton',
            'Button2' : 'Yee2.TButton',
            'Frame' : 'Yee.TFrame',
            'Label' : 'Yee.TLabel'}
    fontBoard = font.Font(font = ('Times', 30))
    fontMain = font.Font(font = ('Consolas', 90))
    styleGen = Style()
    styleGen.configure(style['Button'], foreground = 'Black', background = 'Grey', font = fontBoard)
    styleGen.configure(style['Frame'], foreground = 'Yellow', background = 'White')
    styleGen.configure(style['Label'], foreground = 'Black', background = 'White', font = fontBoard)

    # Defining state_dict
    a = [{'position' : ['X','O','X','O','','O','X','O','X'],
        'score' : 10},
        {'position' : ['X','O','X','','','O','','O','X'],
        'score' : 1}]
        
    funcBoardFrames(tkWindow,style,a).grid(row = 0, column = 1)
    funcMainBoard(tkWindow,style,a[0]['position']).grid(row = 0, column = 0)

    print("Welcome to TicTacToe!")
    x_player = HumanPlayer('X')
    o_player = HumanPlayer('O')
    t=TicTacToe()
    play(t, x_player,o_player,print_game=True)

    funcBoardFrames(tkWindow,style,a).grid(row = 0, column = 1)
    funcMainBoard(tkWindow,style,a[0]['position']).grid(row = 0, column = 0)

    a = [{'position' : ['X','O','X','O','','O','X','O','X'],
        'score' : 10},
        {'position' : ['O','O','O','','','O','','O','O'],
        'score' : 3}]

    funcBoardFrames(tkWindow,style,a).grid(row = 0, column = 1)
    funcMainBoard(tkWindow,style,a[0]['position']).grid(row = 0, column = 0)

    tkWindow.mainloop()