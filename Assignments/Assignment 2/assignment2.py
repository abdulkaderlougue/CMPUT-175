import random
class TicTacToe:
    def __init__(self):
        # "board" is a list of 10 strings representing the board (ignore index 0)
        self.board = [" "]*10
        self.board[0]="#"
        
#------------------------------------------------------------- 
    def drawBoard(self):
    # This method prints out the board with current plays adjacent to a board with index.
        line1 = '\t 7 '+'|'+' 8 '+'|'+' 9 '
        line2 = '\t 4 '+'|'+' 5 '+'|'+' 6 '
        line3 = '\t 1 '+'|'+' 2 '+'|'+' 3 '
        print(' ' + self.board[7]+' | '+self.board[8]+' | '+self.board[9]+ line1)
        print('-----------\t-----------')
        print(' ' + self.board[4]+' | '+self.board[5]+' | '+self.board[6]+ line2)
        print('-----------\t-----------')
        print(' ' + self.board[1]+' | '+self.board[2]+' | '+self.board[3]+ line3)

#------------------------------------------------------------- 
    def boardFull(self):
        if ' ' in self.board:
            return False
        else:
            return True
    # This method checks if the board is already full and returns True. Returns false otherwise

#write some code here

#------------------------------------------------------------- 
    def cellIsEmpty(self, cell):
        if self.board[cell] == ' ':
            return True
        else:
            return False

#-------------------------------------------------------------
    def deAssignMove(self,cell):
        self.board[cell] = ' '
        
#-------------------------------------------------------------
    def assignMove(self, cell,ch):
        if self.cellIsEmpty(cell):
            self.board[cell] = ch        
            
        
    # assigns the cell of the board to the character ch
#------------------------------------------------------------- 

    def whoWon(self):
        # returns the symbol of the player who won if there is a winner, otherwise it returns an empty string. 
        if self.isWinner("x"):
            return "x"
        elif self.isWinner("o"):
            return "o"
        else:
            return ""
#-------------------------------------------------------------   
    def isWinner(self, ch):
        while ch != ' ':
            return ((self.board[7]==ch and self.board[8]==ch and self.board[9]==ch) or
                    (self.board[4]==ch and self.board[5]==ch and self.board[6]==ch) or
                    (self.board[1]==ch and self.board[2]==ch and self.board[3]==ch) or
                    (self.board[7]==ch and self.board[4]==ch and self.board[1]==ch) or
                    (self.board[8]==ch and self.board[5]==ch and self.board[2]==ch) or
                    (self.board[9]==ch and self.board[6]==ch and self.board[3]==ch) or
                    (self.board[7]==ch and self.board[5]==ch and self.board[3]==ch) or
                    (self.board[1]==ch and self.board[5]==ch and self.board[9]==ch))
    # Given a player's letter, this method returns True if that player has won.
#-------------------------------------------------------------
    def changeCh(self,ch):
        if ch == 'x':
            ch='o'
            return ch
        else:
            ch='x'
            return ch 
    # change the sign
#-------------------------------------------------------------

    def checkCenter(self):
        if self.board[5]== ' ':
            return True
    #check whether the center of board is empty
#-------------------------------------------------------------
    def checkCorner(self):
        if self.board[1]== ' ' or self.board[3] == ' ' or self.board[7] == ' ' or self.board[9] == ' ':
            return True
    #check whether the corner of board is empty
#-------------------------------------------------------------
    def checkSide(self):
        if self.board[2]== ' ' or self.board[4] == ' ' or self.board[6] == ' ' or self.board[8] == ' ':
            return True        
    #check whether the side of board is empty
#-------------------------------------------------------------

def main():
    gameOver = False
    while gameOver == False:
        myboard = TicTacToe()
        print('Welcome to Tic Tac Toe Series')
        name1 = input('What is your name?')           # name of player
        cell = 0                                      #cell is index of board
        
        while gameOver == False:
            print(name1 + ', There are 4 modes for playing, please choose a number from 1 to 6 to choose mode')
            print('User against user ...............1')
            print('User against dumb computer ......2')
            print('User against random computer ....3')
            print('User against smart computer......4')
            print('Randomly selected game...........5')
            print('Quit ............................6')
            mode = '0'                               # set mode as 0 at first 
            #user chooses mode
            while mode not in '1 2 3 4 5 6'.split() and gameOver == False:
                try:
                    mode = input('Enter your choice: ')
                    assert mode in  '1 2 3 4 5 6'.split(),'choose a number in 1,2,3,4,5,6'
                except Exception:
                    print('choose a number in 1,2,3,4,5,6')
                
                if mode == '5':
                    mode = random.choice(['2','3','4'])  # randomly choose a mode from Dumb Computer, Random Computer or Smart Computer strategy
            #code for end the game         
            if mode == '6':
                gameOver = True
                break
                    
            #code for user against user
            if mode == '1':
                print('you are playing User against user game')
                name2 = input("what is player2's name?")  #name of player 2
                whoFirst = 'name' 
                while whoFirst not in (name1,name2):
                    try:
                        whoFirst = input('enter a name to choose who goes first')  #choose who goes first
                    except Exception:
                        print('Please choose a name between two players')
                #initialize ch(the sign) and name(refer as turn in mode 1) 
                if whoFirst == name1:
                    ch = 'x'
                    name = name1
                elif whoFirst == name2:
                    ch = 'x'
                    name = name2  
                while not myboard.cellIsEmpty(cell):
                    cell = 0
                    # a while loop to get a cell number to assign move 
                    while cell < 1 or cell > 9:
                        while cell not in  [1,2,3,4,5,6,7,8,9]:
                            try:
                                myboard.drawBoard()
                                cell1 = int(input('It is the turn for ' + name +' . What is your move? ')) # user decides which tile to go
                                try:
                                    if myboard.cellIsEmpty(cell1) ==True:
                                        cell = cell1
                                    else:
                                        cell = 0
                                except Exception:
                                    print('input a number from 1-9!')
                            except ValueError:
                                print('input a number from 1-9!')
                                None
                    myboard.assignMove(cell,ch)       #assign move after getting the cell
                    #check if someone have won
                    if myboard.isWinner(ch):
                        myboard.drawBoard()
                        print(name +' is winner')
                        answer='x'
                        while answer.upper() not in "YN":
                            try:
                                answer=input("Do you want to play another game? (Y/N)")
                            except Exception:
                                print('Please choose a character from Y or N')
                        if answer.upper() == "N":
                            gameOver = True
                        else:
                            gameOver = False
                        break
                    #check if it is a tie
                    if myboard.boardFull() == True:
                        myboard.drawBoard()
                        print('its a tie')
                        while answer.upper() not in "YN":
                            try:
                                answer=input("Do you want to play another game? (Y/N)")
                            except Exception:
                                print('Please choose a character from Y or N')
                        if answer.upper() == "N":
                            gameOver = True
                        else:
                            gameOver = False                
                        break
                    #change sign to chaneg turn
                    if ch == 'x' and name == name1:
                        ch = 'o'
                        name = name2
                    elif ch =='x' and name == name2:
                        ch ='o'
                        name = name1
                    elif ch =='o' and name == name1:
                        ch='x'
                        name = name2
                    else:
                        ch = 'x'
                        name = name1
               
            #code for mode 2 which is user against dumb computer
            if mode == '2':
                print('you are playing User against dumb computer game')
                turn = 0          
                numberList = [9,8,7,6,5,4,3,2,1]            #List contain possible move for user
                #user's input
                choose = 'n'
                while choose not in 'x o r'.split():
                    try:
                        choose = input(name1+ ' , do you want to play x or o? Type r if you want me to chose for you.')
                        choose.lower()
                        assert choose in ["x","o","r"], 'please choose from x , o or r'
                    except Exception:
                        print('please choose from x , o or r')

                #initialize ch(the sign) and name(refer as turn in mode 1)
                if choose == 'x':
                    ch='x'
                    turn = 1
                elif choose == 'o':
                    turn = 2
                    ch='o'
                else:
                    #random choose from x and o
                    index = random.randint(1,3)
                    if index == 1:
                        ch = 'x'
                        turn = 1
                    else:
                        ch = 'o'
                        turn = 2
                while not myboard.cellIsEmpty(cell):
                    cell = 0
                    #code for getting the cell's number
                    while cell < 1 or cell > 9:            
                        if turn == 1:
                            while cell not in  [1,2,3,4,5,6,7,8,9]:
                                try:
                                    myboard.drawBoard()
                                    cell1 = int(input('It is the turn for ' + name1 +' . What is your move? '))  #user's input
                                    try:
                                        #check if the tile has been token
                                        if myboard.cellIsEmpty(int(cell1)):
                                            cell = cell1
                                            turn = 2
                                        else:
                                            cell = 0
                                    except Exception:
                                        print('input a number from 1-9!')
                                    
                                except ValueError:
                                    print('input a number from 1-9!')
                                    None    
                        else:
                            if choose == 'o':           #change the sign to ensure x goes first
                                ch='x'
                            while not myboard.cellIsEmpty(cell):
                                cell = numberList.pop(0)
                                turn = 1
                            
                    myboard.assignMove(cell,ch)   #assign move after getting the cell
                    #check if there is someone who have won
                    if myboard.isWinner(ch):
                        myboard.drawBoard()
                        print(ch +' is winner')
                        gameOver = True
                        break
                    #check if it is a tie
                    if myboard.boardFull() == True:
                        myboard.drawBoard()
                        print('its a tie')
                        gameOver = True
                        break
                    # change the sign to  change turn
                    elif ch == 'x':
                        ch = 'o'
                    else:
                        ch = 'x'
                # game loop for letting player to choose whether to play again
                if gameOver == True:    
                    answer='x'
                    while answer.upper() not in "YN":
                        try:
                            answer=input("Do you want to play another game? (Y/N)")
                        except Exception:
                            print('Please choose a character from Y or N')
                    if answer.upper() == "N":
                        gameOver = True
                    else:
                        gameOver = False
                        break                
            #code for mode3 which is user against random computer
            if mode == '3':
                print('you are playing User against random computer')
                turn = 0
                numberList = [9,8,7,6,5,4,3,2,1]          #List contain possible move for user
                #user's input
                choose = 'n'
                while choose not in 'x o r'.split():
                    try:
                        choose = input(name1+ ' , do you want to play x or o? Type r if you want me to chose for you.')
                        choose.lower()
                        assert choose in ["x","o","r"], 'please choose from x , o or r'
                    except Exception:
                        print('please choose from x , o or r')
                #initialize ch(the sign) and name(refer as turn in mode 1)
                if choose == 'x':
                    ch = 'x'
                    turn = 1
                elif choose == 'o':
                    ch = 'o'
                    turn = 2
                else:
                    #random choose from x and o
                    index = random.randint(1,3)
                    if index == 1:
                        ch = 'x'
                        turn = 1
                    else:
                        ch = 'o'
                        turn = 2
                while not myboard.cellIsEmpty(cell):
                    cell = 0
                    #code for getting the cell's number
                    while cell < 1 or cell > 9:            
                        if turn == 1 :
                            try:
                                myboard.drawBoard()
                                cell = int(input('It is the turn for ' + name1 +' . What is your move? '))
                                try:
                                    #check if the tile has been token
                                    if myboard.cellIsEmpty(int(cell)):
                                        turn = 2
                                    else:
                                        cell = 0     
                                except Exception:
                                    print('input a number from 1-9!')
                            except ValueError:
                                print('input a number from 1-9!')
                                None    
                        else:
                            if choose == 'o':            #change the sign to ensure x goes first
                                ch='x'                            
                            while not myboard.cellIsEmpty(cell):
                                cell = int(random.choice(numberList))
                                turn = 1
                                
                            
                    myboard.assignMove(cell,ch)     #assign move after getting the cell
                    #check if there is someone who have won
                    if myboard.isWinner(ch):
                        myboard.drawBoard()
                        print(ch +' is winner')
                        gameOver = True
                        break
                    #check if it is a tie
                    if myboard.boardFull() == True:
                        myboard.drawBoard()
                        print('its a tie')
                        gameOver = True
                        break
                    # change the sign to  change turn
                    elif ch == 'x':
                        ch = 'o'
                    else:
                        ch = 'x'  
                # game loop for letting player to choose whether to play again
                if gameOver == True:    
                    answer='x'
                    while answer.upper() not in "YN":
                        try:
                            answer=input("Do you want to play another game? (Y/N)")
                        except Exception:
                            print('Please choose a character from Y or N')
                    if answer.upper() == "N":
                        gameOver = True
                    else:
                        gameOver = False
                        break                     
            #code for mode4 which is user against smart computer
            if mode == '4':
                print('you are playing User against smart computer')
                turn = 0
                numberList = [9,8,7,6,5,4,3,2,1]      #List contain possible move for user
                tileFix = [False]*10                   # Create a list to record if a tile is already taken
                                                      # so the computer would not replace the tile during checking the potential winning
                #user's input
                choose = 'n'
                while choose not in 'x o r'.split():
                    try:
                        choose = input(name1+ ' , do you want to play x or o? Type r if you want me to chose for you.')
                        choose.lower()
                        assert choose in ["x","o","r"], 'please choose from x , o or r'
                    except Exception:
                        print('please choose from x , o or r')
                #initialize ch(the sign) and name(refer as turn in mode 1)
                if choose == 'x':
                    ch = 'x'
                    turn = 1
                elif choose == 'o':
                    ch = 'o'
                    turn = 2
                else:
                    #random choose from x and o
                    index = random.randint(1,2)
                    if index == 1:
                        ch = 'x'
                        turn = 1
                    else:
                        ch = 'o'
                        turn = 2
                while not myboard.cellIsEmpty(cell):
                    cell = 0
                    #code for getting the cell's number
                    while cell < 1 or cell > 9: 
                        if turn == 1 :
                            try:
                                myboard.drawBoard()
                                cell = int(input('It is the turn for ' + name1 +' . What is your move? '))
                                if tileFix[cell]== False:
                                    turn = 2
                                else:
                                    cell=0
                                
                            except Exception:
                                print('input a number from 1-9!')
                                None    
                        else:
                            if choose == 'o':
                                ch = 'x'
                            moved = False     #moved =false means computer has not moved yet
                            for i in numberList:
                                if tileFix[i] == False:    
                                    myboard.assignMove(i,ch) #assume computer makes a move 
                                else:
                                    continue
                                winner = myboard.whoWon()    #check this point who won
                                if winner == ch :            #if computer win 
                                    myboard.deAssignMove(i)  #remove this move
                                    cell = i                 #record the cell number 
                                    moved = True             #computer has made its move
                                    break
                                else:
                                    #check if player will win at next move
                                    myboard.deAssignMove(i)   #remove last move
                                    ch = myboard.changeCh(ch) #change the sign to assume that computer as player
                                    #a for loop to check each cell
                                    for i2 in numberList:     
                                        if tileFix[i2] == False:  # if the tile is not been taken
                                            myboard.assignMove(i2, ch) #assume player's next move
                                            winner = myboard.whoWon()  #check if player will win at this move
                                            if winner == ch:
                                                myboard.deAssignMove(i2) # if win, remove the move
                                                cell = i2                # record the cell number to assign move so that player will be blocked
                                                # change the sign back
                                                moved = True             # computer has made his move
                                                break
                                            else:
                                                myboard.deAssignMove(i2) # if not win remove the move
                                    ch = myboard.changeCh(ch)
                                   
                            #if computer have not made its move yet
                            if moved == False :
                                #check whether the center of board is empty
                                if myboard.checkCenter():
                                    cell = 5
                                #check whether the corner of board is empty
                                elif myboard.checkCorner():
                                    while not myboard.cellIsEmpty(cell):
                                        cell = int(random.choice(['1','3','7','9']))
                                #check whether the side of board is empty
                                elif myboard.checkSide():
                                    while not myboard.cellIsEmpty(cell):
                                        cell = int(random.choice(['2','4','6','8']))
                                    
                            turn = 1  #change the turn
                            
                    myboard.assignMove(cell,ch) #assign move
                    tileFix[cell] = True      # Record that this tile has been taken.
                    #check if there is a winner
                    if myboard.isWinner(ch):
                        myboard.drawBoard()
                        print(ch +' is winner')
                        gameOver = True
                        break
                    #check if it is a tie
                    if myboard.boardFull() == True:
                        gameOver = True
                        myboard.drawBoard()
                        print('its a tie')                     
                        break        
                    #change the sign to change the turn
                    elif ch == 'x':
                        ch = 'o'
                    else:
                        ch = 'x'
                # game loop for letting player to choose whether to play again
                if gameOver == True:    
                    answer='x'
                    while answer.upper() not in "YN":
                        try:
                            answer=input("Do you want to play another game? (Y/N)")
                        except Exception:
                            print('Please choose a character from Y or N')
                    if answer.upper() == "N":
                        gameOver = True
                    else:
                        gameOver = False
                        break      
main()