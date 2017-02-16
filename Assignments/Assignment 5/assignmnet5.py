import random
# -----------------------------------------------------------------------------
# Battleship Game - Assignment 5 - CMPUT 175 - Winter 2015
# Name:        Yaozhi Lu
# Student No.: 1433993
# -----------------------------------------------------------------------------

class BattleshipGame:
    def __init__(self):
        self.computerShips = {"A":5,"B":4,"S":3,"D":3,"P":2}
        self.userShips = {"A":5,"B":4,"S":3,"D":3,"P":2}
        #setup blank 10x10 board
        self.userBoard=[[" " for i in range(10)] for j in range(10)]
        self.computerBoard=[[" " for i in range(10)] for j in range(10)]
        self.shipDictLetterR = {'A':'Aircraft Carrier','B':'Battleship','S':'Submarine','D':'Destroyer','P':'Patrol Boat'}
        self.rounds = 0
# --------------------------------------------------------------------------- 
    def incrementRounds(self):
        self.rounds+=1
# ---------------------------------------------------------------------------
    def getHits(self,computer):
        count = 0
        if computer == True:
            for i in self.userBoard:
                for j in i:
                    if j == '#':
                        count+=1    #check each element in list
        else:
            for i in self.computerBoard:
                for j in i:
                    if j == '#':
                        count+=1    #check each element in list         
        return count
# ---------------------------------------------------------------------------
    def findTheList(self,theSign):
        #to find the potential position of user's ship
        #return a list
        theList=[]
        board = self.userBoard
        try:
            for i in range(0,10):
                for j in range(0,10):
                    if self.userBoard[i][j]==theSign:
                        theList.append([i,j])
        except:
            pass
        
        return theList
                        
                    
# ---------------------------------------------------------------------------
    def getMisses(self,computer):
        count = 0
        if computer == True:
            for i in self.userBoard:
                for j in i:
                    if j == '*':
                        count+=1
        else:
            for i in self.computerBoard:
                for j in i:
                    if j == '*':
                        count+=1 
        return count
# ---------------------------------------------------------------------------
    def drawBoards(self,hide):
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
                if hide == False:
                    if grid1 in theLetterList:
                        grid1 = ' '
                grid1+='|'                             #add | after each grid
                line1+=grid1
            line1= line1 +'\t'+ letterList[index] + '|'# add prefix for user's board
            for grid2 in self.userBoard[index] :
                grid2+='|'
                line1+=grid2
            if index == 0:
                line1+='  Nbr. of hits  :   '+("%02d"%(BattleshipGame.getHits(self,True)))+' '*15+("%02d"%(BattleshipGame.getHits(self,False)))
            elif index == 1:
                line1+='  Nbr. of misses:   '+("%02d"%(BattleshipGame.getMisses(self,True)))+' '*15+("%02d"%(BattleshipGame.getMisses(self,False)))
            elif index == 2:
                line1+='  Ships sunk    :   '+"%02d"%len(BattleshipGame.getEnemyFleet(self,False)[1])+' '*15+"%02d"%len(BattleshipGame.getEnemyFleet(self,True)[1])
            elif index >2 and index < 9:
                if len(BattleshipGame.getEnemyFleet(self,False)[1])>0:
                    try:
                        line1+=' '*19+self.shipDictLetterR[BattleshipGame.getEnemyFleet(self,False)[1][index-3]]
                    except:
                        pass
                elif len(BattleshipGame.getEnemyFleet(self,True)[1])>0:
                    try:
                        line1+='  '+self.shipDictLetterR[BattleshipGame.getEnemyFleet(self,True)[1][index-3]]
                    except:
                        pass
            print(line1)
            line1 = ''
            index += 1

# ---------------------------------------------------------------------------       
    def validatePlacement(self,computer,ship,size,x,y,ori):

        #validate the ship can be placed at the given coordinates
        # and places it if acceptable
        if ori == "v" and x+size > 10:
            return False
        elif ori == "h" and y+size > 10:
            return False
        else:
            if computer:
                board=self.computerBoard
            else:
                board=self.userBoard
            if ori == "v":
                for i in range(size):
                    if board[x+i][y] != " ":
                        return False
            elif ori == "h":
                for i in range(size):
                    if board[x][y+i] != " ":
                        return False
            # announce the ship to be placed
            if computer:
                print ("Computer placing a " + ship)
            else: 
                print ("You placed a " + ship)                
            #place the ship based on valid orientation and coordinates
            if ori == "v":
                for i in range(size):
                    board[x+i][y] = ship[0]
            else: # ori=="h"
                for i in range(size):
                    board[x][y+i] = ship[0]
        return True

# ---------------------------------------------------------------------------       
    def getEnemyFleet(self, computer):
        # returns a list of two lists. The first one has the sunken ships and the second the ships to sink
        if computer:
            fleet=self.userShips
        else:
            fleet=self.computerShips
        toSink=[]
        sunk=[]
        # check all ships in the armada of ennemy in the game instance        
        for ship in fleet.keys():
            if fleet[ship]==0:
                sunk.append(ship)
            else:
                toSink.append(ship)
        return [toSink,sunk]

# ---------------------------------------------------------------------------       
    def checkWinning(self, computer):
        # Check if there are still any pieces of ships left to hit on the board
        # board refers to either the board of the computer (if user is playing) or the user (if computer is playing)
        if computer:
            board=self.userBoard
        else:
            board=self.computerBoard
        # Loop to check all cells in the board
        # if any cell contains a char that is not empty, a miss or a hit return false        
        for i in range(10):
            for j in range(10):
                if board[i][j] != ' ' and board[i][j] != '*' and board[i][j] != '#':
                    return False
        return True

# ---------------------------------------------------------------------------       
    
    def makeA_Move(self, computer, x,y):
        if computer:
            board=self.userBoard
        else:
            board=self.computerBoard
        old=board[x][y]
        if old==" ":
            board[x][y]="*"
        elif old=="*" or old=="#":
            return old
        else:
            board[x][y]="#"
        return old
# ---------------------------------------------------------------------------       

    def checkIfSunk(self, computer,symbol):
        if computer:
            armada=self.userShips
        else:
            armada=self.computerShips
        
        # reduce size left of hit ship and check if sunk
        armada[symbol] -= 1
        if armada[symbol] == 0:
            return True
        return False
    
        
# ---------------------------------------------------------------------------

#user define function
def computerPlaceShips(game,ships):
    # Placing the computer ships in random positions
    for ship in ships.keys():
        #generate random coordinates and validate the postion
        valid = False
        while(not valid):
            x = random.randint(1,10)-1
            y = random.randint(1,10)-1
            o = random.randint(0,1)
            if o == 0: 
                ori = "v"
            else:
                ori = "h"
            valid = game.validatePlacement(True,ship,ships[ship],x,y,ori)
    
# ---------------------------------------------------------------------------       
def userPlaceShips(game,ships):
    #Placing the user ships after asking the coordinates and the orientation of each
    #Coordinates are for the bow
    for ship in ships.keys():
        #get coordinates from user and vlidate the postion
        valid = False
        while(not valid):
            game.drawBoards(False)
            print ("Placing a", ship, "of size", ships[ship])
            # reading coordinates x y of new ship
            shipCoordinates=readCoordinates()
            x=shipCoordinates[0]
            y=shipCoordinates[1]
            # reading orientation of new ship
            validOrientation=False
            while not validOrientation:
                orientation=input("This ship is vertical or horizontal (v,h)? ").lower()
                if orientation == "v" or orientation == "h":
                    validOrientation=True                
            valid = game.validatePlacement(False,ship,ships[ship],x,y,orientation)
            if not valid:
                print ("Cannot place a", ship, "there. Stern is out of the board or collides with other ship.\nPlease take a look at the board and try again.")
                input("Hit ENTER to continue")

    game.drawBoards(False)         # DEBUGGING: Cheating to see where the computer ships are
    input("Done placing user ships. Hit ENTER to continue")

# ---------------------------------------------------------------------------       
def readCoordinates():
    # read coordinates x y on board from user and validate
    validCoordinates=False
    while not validCoordinates:
        cell=input("Enter coordinates x y (x in [A..J] and y in [1..10]):")
        cell=cell.split()
        if len(cell)==2:
            if cell[0].upper() in ['A','B','C','D','E','F','G','H','I','J'] and cell[1].isdigit():
                x=['A','B','C','D','E','F','G','H','I','J'].index(cell[0].upper())
                y=int(cell[1])-1
                if x>=0 and x<=9 and y>=0 and y<=9:
                    validCoordinates=True    
    return [x,y]
# ---------------------------------------------------------------------------       
def userMakesMove(game):
    # ask for coordinates for a move by user and try to make move
    # if move is a hit, check ship sunk and win condition 
    # return if user won    
    moveLigit=False
    while(not moveLigit):
        move=readCoordinates()
        x=move[0]
        y=move[1]
        beforeDropped = game.makeA_Move(False,x,y)
        #displaying current boards
        labels=['A','B','C','D','E','F','G','H','I','J']
        if beforeDropped=="*" or beforeDropped == "#":
            print ("Sorry, " + labels[x] + " " + str(y+1) + " was already played. Try again.")
        elif beforeDropped == " ":
            print ("Sorry, " + labels[x] + " " + str(y+1) + " is a miss.")
            moveLigit=True
            
        else:
            print ("Hit at " + labels[x] + " " + str(y+1))
            if game.checkIfSunk(False,beforeDropped): 
                print (whatShip(beforeDropped) + " sunk")
            moveLigit=True
            
    input("Press RETURN to continue")        
    return game.checkWinning(False)        
        
# ----------------------------------------------------------------------
#get the attack list for hunt by considering the size of smallest ship
def attackList(size):
    attackList = []
    if size == 2:
        for i in range(0,10):
            if i%2 == 0:   #if its even
                for j in range(0,10,2):
                    attackList.append([i,j]) # append the coord
            else:          #if its odd
                for j in range(1,10,2):
                    attackList.append([i,j])
                    
    ##do the same thing below
    elif size == 3:
        for i in range(0,10):
            if i%3 ==0:
                for j in range(0,10,3):
                    attackList.append([i,j])
            elif i%3 ==1:
                for j in range(1,10,3):
                    attackList.append([i,j])
            else:
                for j in range(2,10,3):
                    attackList.append([i,j])          
    elif size ==4:
        for i in range(0,10):
            if i%4 == 0:
                for j in range(0,10,4):
                    attackList.append([i,j])
            elif i%4 == 1:
                for j in range(1,10,4):
                    attackList.append([i,j])
            elif i%4 ==2:
                for j in range(2,10,4):
                    attackList.append([i,j])
            elif i%4 ==3:
                for j in range(3,10,4):
                    attackList.append([i,j])
    elif size == 5:
        for i in range(0,10):
            if i%5==0:
                for j in range (0,10,5):
                    attackList.append([i,j])
                    
            elif i%5==0:
                for j in range(1,10,5):
                    attackList.append([i,j])
            elif i%5 == 1:
                for j in range(2,10,5):
                    attackList.append([i,j])
            elif i%5 == 2:
                for j in range(3,10,5):
                    attackList.append([i,j])
            elif i%5 == 3:
                for j in range(4,10,5):
                    attackList.append([i,j])
            elif i%5 == 4:
                for j in range(5,10,5):
                    attackList.append([i,j])
    return attackList
                
                

# ----------------------------------------------------------------------
def whatShip(symbol):
    # converting the symbol of a ship to the full name and returning it
    if symbol == "A":
        ship = "Aircraft Carrier"
    elif symbol == "B":
        ship = "Battleship"
    elif symbol == "S":
        ship = "Submarine" 
    elif symbol == "D":
        ship = "Destroyer"
    elif symbol == "P": 
        ship = "Patrol Boat"
    return ship    
    
# #############################################################################
def main():
    ships = {"Aircraft Carrier":5,"Battleship":4,"Submarine":3,"Destroyer":3,"Patrol Boat":2}    
    game=BattleshipGame()                   # create instance of the game
    computerPlaceShips(game,ships)          # Computer places its armada
    userPlaceShips(game,ships)              # User places the armada
    gameOver=False
    tryList= []
    checkMove = []
    explore = False
    attack = False
    ori = None
    huntPhase = True
    lastBeforeDropped = 0
    # game main loop
    while(not gameOver): 
       
        #user move
        winning=userMakesMove(game)

        #check if user won
        if winning:
            print ("Congratulations! User WON!")
            gameOver=True
        else:
            # display what remains of the fleet
            armada=game.getEnemyFleet(False)
            print ("Ships to sink:[", end="")
            for ship in armada[0]:
                print (whatShip(ship), " ", end="")
            print ("]  Ships sunk:[",end="")
            for ship in armada[1]:
                print (whatShip(ship), " ", end="")
            print("]")            
            
            #computer move
            moveLigit=False
            
            
            while(not moveLigit):
                if huntPhase == True:
                    #get the size smallest ship
                    toSunk = game.getEnemyFleet(True)[0]
                    size = 6
                    for i in toSunk:
                        fullName = whatShip(i)
                        if ships[fullName] < size:
                            size = ships[fullName]
                    #use the function to get the attack list
                    theList = attackList(size)
                    beforeDropped = '#'
                    #if the cell has been occupied, keep puting bombs
                    while beforeDropped == '#' or beforeDropped == '*':
                        coord = random.choice(theList)
                        x = coord[1]
                        y = coord[0]
                        beforeDropped = game.makeA_Move(True,x,y)
                    #if hit something
                    if beforeDropped not in [' ','#','*']:
                        if game.checkIfSunk(True,beforeDropped):
                            print (whatShip(beforeDropped) + " sunk")                       
                        checkMove.append([coord[1],coord[0]])
                        centerCoord = checkMove[0]      #the hitted position to be checked. check the direction of ship
                        #append around qualified position into list
                        if centerCoord[0]+1 < 10:
                            tryList.append([centerCoord[0]+1,centerCoord[1]])
                        if centerCoord[0]-1 > -1:
                            tryList.append([centerCoord[0]-1,centerCoord[1]])
                        if centerCoord[1]+1 < 10:
                            tryList.append([centerCoord[0],centerCoord[1]+1])
                        if centerCoord[1]-1> -1:
                            tryList.append([centerCoord[0],centerCoord[1]-1])
                        lastBeforeDropped = beforeDropped  #record last move in case hit other ship
                        explore = True
                        huntPhase = False
                    moveLigit = True
                elif explore == True:   
                    checked = False
                    labels=['A','B','C','D','E','F','G','H','I','J']
                    while not checked:
                        theTry = random.choice(tryList)     #choose a position to hit
                        beforeDropped = game.makeA_Move(True,theTry[0],theTry[1])
                        if beforeDropped=="*" or beforeDropped == "#":   #if it has been occupied
                            tryList.remove(theTry)                       #remove the position
                            checked = False
                        elif beforeDropped == ' ':     #if not hit the ship
                            print ("Sorry computer, " + labels[theTry[0]] + " " + str(theTry[1]+1) + " is a miss.")
                            tryList.remove(theTry)     #remove the position
                            checked = True
                            moveLigit=True
                        elif beforeDropped not in [' ','#','*']:   #if hit
                            print ("Computer did a Hit at " + labels[theTry[0]] + " " + str(theTry[1]+1))
                            if game.checkIfSunk(True,beforeDropped):     #decrease the size 
                                print (whatShip(beforeDropped) + " sunk")
                            elif theTry[0]-centerCoord[0] == 1 or theTry[0]-centerCoord[0] == -1:
                                if lastBeforeDropped == beforeDropped:     #if hit the same ship
                                    theMove = theTry
                                    theSign = beforeDropped
                                    ori = 'v'                               #return the direction
                                    toAttack = game.findTheList(theSign)
                                else:
                                    theSign = lastBeforeDropped
                                    theMove = theTry
                                    ori = 'h'                                #return the direction
                                    toAttack = game.findTheList(theSign)
                                
                            elif theTry[1]-centerCoord[1] == 1 or theTry[1]-centerCoord[1] == -1:
                                if lastBeforeDropped == beforeDropped:
                                    theMove = theTry
                                    ori = 'h'                                #return the direction
                                    theSign = beforeDropped
                                    toAttack = game.findTheList(theSign)
                                else:
                                    theSign = lastBeforeDropped
                                    theMove = theTry
                                    ori = 'v'                                #return the direction
                                    toAttack = game.findTheList(theSign)     
                            lastBeforeDropped = 0
                            checked = True
                            moveLigit=True
                            explore = False
                            attack = True
                            
                            
                elif attack == True:
                    if len(toAttack)>0:
                        attackCoord = toAttack.pop(0)       #give a position from potential attack positon list to attack 
                        preDropped = game.makeA_Move(True,attackCoord[0],attackCoord[1])
                        if game.checkIfSunk(True,preDropped):           #check if sunk
                            print (whatShip(preDropped) + " sunk")
                            checkMove = []
                            huntPhase = True
                            attack = False
                            tryList = []         #clear the try list
                        moveLigit=True
                    else:
                        moveLigit= False

                    
            game.incrementRounds()
            game.drawBoards(False)
            winning = game.checkWinning(True)
            
        
            #check if computer won
            if winning:
                print ("Sorry! Computer WON! Here is what the board looked like:")
                # display boards without hiding the computer ships
                game.drawBoards(True)
                input("Press ENTER to continue")
                gameOver=True
# ############################################################################# 
    
if __name__=="__main__":
    main()