import random
class BattleshipGame:
    def __init__(self):
        self.userBoard = [[' ']*10 for row in range(10)]
        self.computerBoard = [[' ']*10 for row in range(10)]
        self.comShips = {'A':5,'B':4,'S':3,'D':3,'P':2}
        self.userShips = {'A':5,'B':4,'S':3,'D':3,'P':2}
        self.rounds = 0
        
    def drawBoards(self, hide):
        #draws the grid of the computer next to the grid of the user as illustrated above. The user grid should have the user placed ships as well as the hit and misses
        #of the compputer. The computer grid should have the hit and misses of the user and if the hide parameter is True, the grid should NOT show the ships of the computer. 
        #The ships on the grid are represented by the first letter of their type. For example a Submarine (size 3) would be SSS. An Aircraft Carrier (size 5) would be AAAAA.
        title = '1 2 3 4 5 6 7 8 9 10'
        letterList = ['A ','B ','C ','D ','E ','F ','G ','H ','I ','J ']
        theLetterList =['A','B','D','S','P']
        print("   Computer's board:   \t   User's board   \t  at round: "+str(self.rounds))
        print(' '*3 + title + ' '*4 + title+' '*19+'Computer Status:  User Status:')
        index = 0
        line1 = ''
        for lines1 in self.computerBoard:
            line1 = line1 + letterList[index]+ '|'     #add prefix
            for grid1 in lines1:                       #hide computer's boat
                if hide == True:
                    if grid1 in theLetterList:
                        grid1 = ' '
                grid1+='|'                             #add | after each grid
                line1+=grid1
            line1= line1 +'\t'+ letterList[index] + '|'# add prefix for user's board
            for grid2 in self.userBoard[index] :
                grid2+='|'
                line1+=grid2
            if index == 0:
                line1+='  Nbr. of hits  :   '+("%02d"%(self.userBoard.count('#')))+' '*15+("%02d"%(self.computerBoard.count('#')))
            elif index == 1:
                line1+='  Nbr. of misses:   '+("%02d"%(self.userBoard.count('*')))+' '*15+("%02d"%(self.computerBoard.count('*')))
            elif index == 2:
                line1+='  Ships sunk    :   '+"%02d"%len(BattleshipGame.getEnemyFleet(self,False)[1])+' '*15+"%02d"%len(BattleshipGame.getEnemyFleet(self,True)[1])
                #print(BattleshipGame.getEnemyFleet(self,False)[1]+BattleshipGame.getEnemyFleet(self,True)[1])            
            print(line1)
            line1 = ''
            index += 1
                 
            

    def validatePlacement(self, computer, ship, size, x, y, orientation):
        #attempts to place a ship of type ship of size size at a given coordinates x and y. ship is the first letter of the type of ship.  It returns True if a ship is well 
        #placed and False if the stern of a ship is out of bounds or crosses another ship. x and y are the coordinates of the indicated position for the bow of the ship to place. 
        #In other words, the bow of the ship is at location (x,y). orientation is either h or v indicating horizontal of vertical positioning for the ship on the grid. computer is
        #True if the computer is placing a ship on its grid. It is False if it is the user placing the ship on the player's grid. 
        placed = False
        canBePlaced = ''                                    # to check if grid can be placed
        if orientation == 'h':
            if y+size-1 > 9:                                #check if over size
                placed = False
            else:
                for i in range(0,size):
                    if computer == False:
                        if self.userBoard[x][y+i] == ' ':   #return true if can be placed 
                            canBePlaced = True
                            pass
                        else:                               #if one of grid cannot be placed return False and break
                            canBePlaced = False
                            break
                    else:
                        if self.computerBoard[x][y+i] == ' ':  #return true if can be placed 
                            canBePlaced = True
                            pass
                        else:
                            canBePlaced = False
                            break                            
                if canBePlaced == True:                        #if all grid can be placed
                    for i in range(0,size):
                        if computer == False:
                            self.userBoard[x][y+i] = ship      #change character
                            
                        else:
                            self.computerBoard[x][y+i] = ship    #change character
                    placed = True
                else:
                    placed = False
            
        if orientation == 'v':
            if x + size-1 > 9:                              # to check if grid can be placed
                placed = False
            else:
                for i in range(0,size):
                    if computer == False:
                        if self.userBoard[x+i][y] == ' ':   #return true if can be placed 
                            canBePlaced = True
                            pass
                        else:
                            canBePlaced = False               #if one of grid cannot be placed return False and break
                            break
                    else:
                        if self.computerBoard[x+i][y] == ' ':   #return true if can be placed 
                            canBePlaced = True
                            pass
                        else:
                            canBePlaced = False
                            break                            
                if canBePlaced == True:                          #if all grid can be placed
                    for i in range(0,size):
                        if computer == False:
                            self.userBoard[x+i][y] = ship        #change character
                            
                        else:
                            self.computerBoard[x+i][y] = ship    #change character
                    placed = True
                else:
                    placed = False
        return placed
            
    def getEnemyFleet(self, computer):
        #returns a list containing two lists, one with the ships still to sink and one with the ships already sunk. The ships are coded by the first letter of their type 
        #(A, D, B, P, and S). computer is True if the computer is requesting list. It is False if it is the user requesting the list.
        toSink = []
        beSunk = []
        theList = []
        if computer == True:
            for items in self.userShips:
                if self.userShips[items] == 0:   #check if all grid of boat have been hit
                    beSunk.append(items)
                else:
                    toSink.append(items)
        if computer == False:
            for items in self.comShips:
                if self.comShips[items] == 0:   #check if all grid of boat have been hit
                    beSunk.append(items)
                else:
                    toSink.append(items) 
                    
        theList.append(toSink)
        theList.append(beSunk)
        return theList
        
        
    def checkWinning(self, computer):
        #returns True if all ships are sunk and False if there are still ships in the fleet. computer is True if the computer is requesting the information. 
        #It is False if it is the user requesting the information.
        result = BattleshipGame.getEnemyFleet(self,computer)
        if computer == True:
            if len(result[1]) == 5:        #check if win
                return True
            else:
                return False
            
        if computer == False:
            if len(result[1]) == 5:       #check if win
                return True
            else:
                return False            
        
    def makeA_Move(self,computer, x, y):
        #computer is True if the computer is making the move, and False if it is the user making the move. It returns the old content as a character of grid cell
        #at x and y after replacing this content with either "*" (miss) if it was empty and "#" (hit) if it contained part of a ship. If the content of the cell was 
        #already a hit or a miss, it simply returns it.
        content = ''
        if computer == True:
            if self.userBoard[x][y] == ' ':
                symbol = '*'
                self.userBoard[x][y]=symbol        #change the content
                
            elif self.userBoard[x][y] == '*':      #check if grid has been hit
                symbol = '*'
            elif self.userBoard[x][y] == '#':
                symbol = '#'
            else:
                content = self.userBoard[x][y]
                self.userShips[content] -= 1
                symbol = '#'
                self.userBoard[x][y] = symbol    #change the content
                
        if computer == False:
            if self.computerBoard[x][y] == ' ':
                content = self.computerBoard[x][y]
                symbol = '*'
                self.computerBoard[x][y]=symbol     #change the content
                
            elif self.computerBoard[x][y] == '*':    #check if grid has been hit
                symbol = '*'  
            elif self.computerBoard[x][y] == '#':
                symbol = '#'
            else:
                content = self.computerBoard[x][y]
                self.comShips[content] -= 1
                symbol = '#'
                self.computerBoard[x][y] = symbol     #change the content
    
        return content
                
    
    def checkIfSunk(self, computer, ship):
        #Updates the count for the parts of the ship symbolized by ship, the first letter of the ship type, and returns True if the ship is sunk and False if the ship
        #is not sunk yet. computer is True if the computer is requesting the information. It is False if it is the user requesting the information.
        if computer == True:
            count = self.userShips[ship]
            if count == 0:                     #check if sunk
                return True
            else:
                return False
            
        if computer == False:
            count = self.comShips[ship]        #check if sunk
            if count == 0:
                return True
            else:
                return False
            
def main():
    game = BattleshipGame()
    gameOver = False
    hide = True
    letterIndex = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10}                         #letter dictionary key is character and value is int
    shipList = ['Aircraft Carrier','Battleship','Submarine','Destroyer','Patrol Boat']                   #ship name list
    shipDictInt = {'Aircraft Carrier':5,'Battleship':4,'Submarine':3,'Destroyer':3,'Patrol Boat':2}      #ship dictionary, key is ship nume and value is size
    shipDictLetter = {'Aircraft Carrier':'A','Battleship':'B','Submarine':'S','Destroyer':'D','Patrol Boat':'P'}   #ship dictionary, key is ship nume and value is letter
    shipDictLetterR = {'A':'Aircraft Carrier','B':'Battleship','S':'Submarine','D':'Destroyer','P':'Patrol Boat'}  #reverse of shipDictLetter
    letterList =['A','B','D','S','P']            #letter list
    
    userShips= []
    userShipsSunk = []
    
    computerShips = []
    computerShipsSunk = []
    
    game.drawBoards(hide)
    index = 0
    
    
    while index < 5:
        reroll = False
        while not reroll:
            haveInput = False
            print('placing a '+shipList[index]+' of size '+str(shipDictInt[shipList[index]]))
            while not haveInput:
                try:
                    userInputCoord =input('Enter coordinates x y (x in [A..J] and y in [1..10]): ')     #put a ship in map
                    inputCoord = userInputCoord.split(' ')
                    coord = [int(letterIndex[inputCoord[0].upper()])-1,int(inputCoord[1])-1]
                    haveInput = True
                    assert (0<=coord[0]<10 and 0<=coord[1]<10)
                except Exception as exce:
                    haveInput = False
                    print(exce)
                    
            orientation = ''                                                                            #get orientation
            while orientation not in ['h','v']: 
                orientation = input('This ship is vertical or horizontal (v,h)? ')

            haveInput = False
            while not haveInput:
                try:
                    if game.validatePlacement(False,shipDictLetter[shipList[index]],shipDictInt[shipList[index]],coord[0],coord[1],orientation) == True:  #change letter and add ship into list
                        userShips.append(shipList[index])
                        game.drawBoards(hide)
                        index += 1
                        haveInput = True
                        reroll = True
                    
                    assert(haveInput == True)
                except Exception:
                    print('Cannot place a Submarine there. Stern is out of the board or collides with other ship.\nPlease take a look at the board and try again.')
                    input('Hit ENTER to continue')
                    haveInput = True
                    reroll = False
                    
    
    index = 0
    while index < 5:                                               #put computer's ship
        comCoord=[random.randint(0,9),random.randint(0,9)]
        orientation = random.choice(['h','v'])
        if game.validatePlacement(True,shipDictLetter[shipList[index]],shipDictInt[shipList[index]],comCoord[0],comCoord[1],orientation) == True:
            computerShips.append(shipList[index])
            index += 1
        else:
            None
    game.drawBoards(hide)
    input('Done placing user ships. Hit ENTER to continue')
    
    while not gameOver:
        haveInput =False
        reroll = False
        turn = 'user'
        if turn == 'user':                              #user's turn
            game.drawBoards(hide)
            while not reroll:                           #while not need to re-enter the coord
                haveInput =False
                while not haveInput:
                    try:
                        location = input('Enter coordinates x y (x in [A..J] and y in [1..10]): ')         #record coord to hit
                        userHit = location.split(' ')
                        userHitCoord = [letterIndex[userHit[0].upper()]-1,int(userHit[1])-1]
                        haveInput = True
                        assert (0<= userHitCoord[0] <10 and 0<= userHitCoord[1] <10)
                    except Exception:
                        haveInput = False
                        print('You have to enter coordinates x y (x in [A..J] and y in [1..10])')
                        
                print('Hit at '+location)
                haveInput = False
                while not haveInput:
                    letter = game.makeA_Move(False,userHitCoord[0],userHitCoord[1])    #make move
                    if letter in letterList:
                        if game.checkIfSunk(False,letter) == True:                     #check if sunk
                            computerShips.remove(shipDictLetterR[str(letter)])
                            computerShipsSunk.append(shipDictLetterR[str(letter)])
                            print(shipDictLetterR[str(letter)]+ ' sunk')
                            haveInput = True
                            reroll = True
                            if game.checkWinning(False) == True:                      #check if win
                                print('Congratulations! User WON!')
                                gameOver = True
                                break
                        else:
                            haveInput = True
                            reroll = True
                    elif letter == ' ':
                        haveInput = True
                        reroll = True
                    else:
                        print('Sorry, '+location+' was already played. Try again.')
                        haveInput = True
                        reroll = False
                
            turn = 'computer'
            
        if turn == 'computer':
            moved = False
            game.drawBoards(hide)
            comHitCoord = [-1, -1]
            while not moved:
                comHitCoord = [random.randint(0,9),random.randint(0,9)]                   #coord to hit
                letter = game.makeA_Move(True,comHitCoord[0],comHitCoord[1])              #make computer's move 
                if letter not in ['*','#']:
                    moved = True
                    if game.checkIfSunk(False,letter) == True:                            #check if sunk
                        userShips.remove(shipDictLetterR[str(letter)])
                        userShipsSunk.append(shipDictLetterR[str(letter)])
                        if game.checkWinning(True) == True:                              #check if win
                            print('Sorry, you lose')
                            gameOver = True
                            game.drawBoards(False)
                            break
                else:
                    moved = False
            turn = 'user'
            
        print('Ships to sink:[ '+ ' '.join(computerShips) +' ] Ships sunk:[' + ' '.join(computerShipsSunk) + ' ]')  #print infomation
        
        
main()