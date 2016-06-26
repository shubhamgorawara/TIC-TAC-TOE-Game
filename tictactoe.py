# Tic Tac Toe Game

#Following modules to be imported

from random import *
import os 

os.system("color f9")	#change background of cmd and the font 
os.system("cls")		#clear screen

def drawtheboard(gameboard):
     """This function prints out the board that was passed."""
     print('   |   |')
     print(' ' + gameboard[7] + ' | ' + gameboard[8] + ' | ' + gameboard[9]) 	
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + gameboard[4] + ' | ' + gameboard[5] + ' | ' + gameboard[6])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + gameboard[1] + ' | ' + gameboard[2] + ' | ' + gameboard[3])
     print('   |   |')

def whowillstart():
     """Randomly choose which person will go first."""
     if randint(0, 1) == 1:
         return 'player'
     else:
         return 'computer'
		 
def Winner(gameboard, letter):   
	 """This function returns True if a player has won the game otherwise False is returned"""
	 return ((gameboard[7] == letter and gameboard[8] == letter and gameboard[9] == letter) or 
     (gameboard[4] == letter and gameboard[5] == letter and gameboard[6] == letter) or 
     (gameboard[1] == letter and gameboard[2] == letter and gameboard[3] == letter) or 
     (gameboard[7] == letter and gameboard[4] == letter and gameboard[1] == letter) or 
     (gameboard[8] == letter and gameboard[5] == letter and gameboard[2] == letter) or 
     (gameboard[9] == letter and gameboard[6] == letter and gameboard[3] == letter) or 
     (gameboard[7] == letter and gameboard[5] == letter and gameboard[3] == letter) or 
     (gameboard[9] == letter and gameboard[5] == letter and gameboard[1] == letter))

def playagain():
     """This returns True if the player wishes to play again, otherwise False is returned."""
     answer = raw_input('Do you want to play again? ')
     return answer.lower().startswith('y')

def makeamove(gameboard, letter, move):
	 """This is used to make a move by a player"""
	 gameboard[move] = letter

def Playerletter():
     """It lets the player select which letter(X or O) he/she wants to be."""
     letter = ''
     while not (letter == 'O' or letter == 'X'):
		letter = raw_input('\nEnter the symbol(X or O) you want to be: ') 
		letter = letter.upper()
    
     if letter == 'O':
         return ['O', 'X']
     else:
         return ['X', 'O']

def makecopyofboard(gameboard):
     """This function is used to make a duplicate of the board list and return the duplicate."""
     DuplicateBoard = []

     for each in gameboard:
         DuplicateBoard.append(each)

     return DuplicateBoard

def choosearandommove(gameboard, movesList):
     """This function returns a valid move from the passed list on the passed board."""
    
     possibleMoves = []
     for each in movesList:
         if isthespacefree(gameboard, each):
             possibleMoves.append(each)

     if len(possibleMoves) != 0:
         return choice(possibleMoves)
     else:
         return None
	 
def choosearandommove(gameboard, movesList):
     """This function returns a valid move from the passed list on the passed board."""
    
     possibleMoves = []
     for each in movesList:
         if isthespacefree(gameboard, each):
             possibleMoves.append(each)

     if len(possibleMoves) != 0:
         return choice(possibleMoves)
     else:
         return None
	 
def isthespacefree(gameboard, move):
     """this function returns True if the passed move is free on the passed board."""
     return gameboard[move] == ' '

def getmoveofplayer(gameboard):
     """This function lets the player type in their move."""
     move = ' '
     while move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or not isthespacefree(gameboard, int(move)):
         move = raw_input('What is your next move? (1-9)')      
     return int(move)

def istheboardfull(gameboard):
     """This function returns True if every space on the board has been taken, otherwise False is returned."""
     for each in xrange(1, 10):
         if isthespacefree(gameboard, each):
             return False
     return True	 
	 
def getmoveofcomputer(gameboard, computerLetter):
     """This function determines the computer's next move."""
     if computerLetter == 'O':
         playerLetter = 'X'
     else:
         playerLetter = 'O'

     for each in xrange(1, 10):		#Firstly, the computer checks if it can win in the next move
         copy = makecopyofboard(gameboard)
         if isthespacefree(copy, each):
             makeamove(copy, computerLetter, each)
             if Winner(copy, computerLetter):
                 return each

     for each in xrange(1, 10):		#Then, we check if the player could win on his/her next move, and if it is so, then we block him/her.
         copy = makecopyofboard(gameboard)
         if isthespacefree(copy, each):
             makeamove(copy, playerLetter, each)
             if Winner(copy, playerLetter):
                 return each

     move = choosearandommove(gameboard, [1, 3, 7, 9])		#Computer takes a corner, if it is free
     if move != None:
         return move

     if isthespacefree(gameboard, 5):		#Computer takes the center, if it is free
         return 5

     return choosearandommove(gameboard, [2, 4, 6, 8])		#Computer takes a side



print('****************TIC TAC TOE****************')

while True:
     Board = [' '] * 10		#This resets the board
     playerLetter, computerLetter = Playerletter()
     firstturn = whowillstart()
     print('The ' + firstturn + ' will go first.')
     gameIsPlaying = True

     while gameIsPlaying:
         if firstturn == 'player':
            
             drawtheboard(Board)
             move = getmoveofplayer(Board)
             makeamove(Board, playerLetter, move)

             if Winner(Board, playerLetter):
                 drawtheboard(Board)
                 print('\nYou have won the game!')
                 gameIsPlaying = False
             else:
                 if istheboardfull(Board):
                     drawtheboard(Board)
                     print('\nIt is a tie!')
                     break
                 else:
                     firstturn = 'computer'

         else:
             
             move = getmoveofcomputer(Board, computerLetter)
             makeamove(Board, computerLetter, move)

             if Winner(Board, computerLetter):
                 drawtheboard(Board)
                 print('\nThe computer has beaten you!')
                 gameIsPlaying = False
             else:
                 if istheboardfull(Board):
                     drawtheboard(Board)
                     print('\nIt is a tie!')
                     break
                 else:
                     firstturn = 'player'

     if not playagain():
		print("\nThankyou for playing!")
		break