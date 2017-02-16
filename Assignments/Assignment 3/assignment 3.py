import random
class OceanTreasure:
    def __init__(self):
        #__chests a list of 3 different pairs representing the randomly selected coordinates of the chests in the ocean
        #__board is a matrix 60 by 15 implemented by a list of 15 lists of 60 positions all initialized by the character '~'
        self.__board = [['~']*60 for row in range(15)]    
        self.__chests=[]
        #choice the location of chest randomly, use a while loop in case same location
        while len(self.__chests) <3 :
            coord = [str(random.randint(0,60)),str(random.randint(0,15))]
            if coord not in self.__chests:
                self.__chests.append(coord)
                
    def getChests(self):
        #returns the list of coordinates of the chests still to be found.
        return self.__chests
    
    def getTreasuresLeft(self):
        #returns the number of treasure chests still to be found.
        return len(self.__chests)
        
    def dropSonar(self,x, y, sonar): 
        #receives two integers x and y and a character sonar and changes the matrix __board by putting the character sonar in 
        #the specified coordinates. x should be between 0 and 59 while y between 0 and 14.
        distance = self.checkDistance(x,y)   #distence from checkDistance method
        if distance == None:                 #if sonar is too far from chest, return O
            sonar = 'O'   
        elif distance == 0:                  #if sonar is on chest, return X and remove the chest from self.__chests
            self.__chests.remove([x,y])
            sonar = 'X'
        elif distance > 0:                   #return the range form checkDistance method if chest is closer on x
            sonar = str(distance)
        elif distance < 0:                   #return the range form checkDistance method if chest is closer on y
            if distance == -1:
                sonar = 'a'
            elif distance == -2:
                sonar = 'b'
            elif distance == -3:
                sonar = 'c'
            elif distance == -4:
                sonar = 'd'
            elif distance == -5:
                sonar = 'e'
                
        self.__board[int(y)][int(x)] = sonar  #change the character

        
        
    def checkDistance(self,x ,y):
        #receives two integers x and y representing the coordinates of a sonar device and returns 0 if the coordinates 
        #correspond to the exact position of a treasure chest. In that case the found chest is removed from the __chest list. 
        #The method returns a positive distance if the closest hidden chest is on the x axis and a negative distance if the closest
        #hidden chest is on the y axis and still in the range.   
        
        location = [x,y]                            #location of sonar
        if location in self.__chests:               #return 0 if sonar is on chest
            return 0
        distanceList = []                           #to store distances between chest and soanr
        coordList = []                              #to store chests' location
        coordDict= {}                               #to make location of chest and distance as pairs
        for chest in self.__chests:                  
            distance = ((int(chest[0])-int(float(x)))**2+(int(chest[1])-int(float(y)))**2)**0.5    #calculate distance
            distanceList.append(distance)                                                #store chest's distence
            coordList.append(chest)                                                      #store chest's location
        for i in range(0,3): 
            coordDict[distanceList[i]]=coordList[i]                                      #make them paired in the dictionary
        
        closedChest = coordDict[min(distanceList)]           # check the minimum distance and its corresponding location
        xRange = abs(int(closedChest[0])-int(x))                  # get the absolute value of x range 
        yRange = abs(int(closedChest[1])-int(y))                  # get the absolute value of x range 
        if xRange < 10 and yRange < 6:                      # check if chest is in the range of sonar
            if xRange < 2 * yRange and xRange != 0 or yRange == 0:
                return xRange                               #return positive x range 
            else:
                return -yRange                              #return negative y range 
 
        
    def drawBoard(self):
        #draws the ocean with the sonar devices by drawing the content of __board.  The board should be drawn as illustrated 
        #above with the indices above, bellow and on the sides of the ocean to allow determination or coordinates.
        print(" " * 4,"1","2","3","4","5",sep = " " * 9)
        print(" " * 3 + "0123456789" * 6)
        index = 0
        for line in self.__board:
            leftIndex = "%2d"%(index)
            row = ""
            for grid in line:
                row += grid
            print(leftIndex,row,str(index),sep = " ")
            index += 1
        print(" " * 4,"1","2","3","4","5",sep = " " * 9)
        print(" " * 3 + "0123456789" * 6)        
        
        
        
        
def main():
    ocean = OceanTreasure()
    chestLocation = ocean.getChests()
    gameOver = False
    droppedSpot = []                        #to store where sonar dropped
    position = ['','']
    usedSonar = 0                           #store how many sonars have been used
    haveInput = False
    print(chestLocation)
    while not gameOver:
        ocean.drawBoard() 
        print("You have " + str(20-usedSonar) + " sonar devices available. Treasures found: " + \
              str(3-ocean.getTreasuresLeft()) + ". Still to be found: " + \
              str(ocean.getTreasuresLeft()) + ".")
        print('Where do you want to drop your sonar?')
        while not haveInput:
            userInput = input('Enter coordinates x y (x in [0..59] and y in [0..14]) (or Q to quit and H for help): ')   #location of sonar user put
            try:
                if userInput.lower() in ['q','h']:        #check if user input can be lower, and if in Q and H
                    try:
                        if userInput.lower() == 'q':      #quit game 
                            haveInput = True              #quit the loop
                            break
                        elif userInput.lower() == 'h':   #get help
                            print('your input must be a pair of x y which sepreted by a space (x in [0..59] and y in [0..14])')
                            haveInput = False
                    except Exception as exce:
                        print(exce)
                            
                else:
                    try:                                # if not in h and q, try to split input to get the location 
                        position=userInput.split(' ')   
                        assert (len(position) == 2 and isinstance(int(position[0]),int) and isinstance(int(position[1]),int)  and int(position[0]) in range(0,60) and int(position[1]) in range(0,14)),"You must enter a pair of coordinates separated by a space (or Q to quit and H for help).\n"          #assert input is in right form    
                        
                        if position not in droppedSpot:    #check if this location has been used
                            droppedSpot.append(position)   # store the position of used soanr
                        else:
                            print('You already dropped a sonar there. You lost another sonar device.\n')                        
                        haveInput = True
                        
                    except :
                        haveInput= False
                        print('your input must be a pair of x y which sepreted by a space (x in [0..59] and y in [0..14])')
                    
                        
            except :
                haveInput= False
        try:                                             #try if input is right form and not in q and h
            ocean.dropSonar(position[0],position[1],'')  #drop the sonar
            usedSonar += 1                               #add 1 used sonar
            haveInput = False                            #refresh the record of 
        except:
            print('Thank you for playing')               #end the game
            gameOver = True
            
        if usedSonar == 20 and ocean.getTreasuresLeft() > 0:   #check if all the sonars have been used
            gameOver = True
            print('You lost all your 20 sonar devises.\nThe remaining chests were in: ' + str(ocean.getChests()))
            
        elif ocean.getTreasuresLeft() == 0:         #check if there is no chest left 
            gameOver = True
            print('Well done! You found all the 3 treasure Chests using ',usedSonar,' out of 20 sonar devices.')
            
       
main()        