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
       
#write some code here

#-------------------------------------------------------------
 
    
    def assignMove(self, cell,ch):
        if self.cellIsEmpty(cell):
            self.board[cell] = ch        
            
        
    # assigns the cell of the board to the character ch
    

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

#write some code here
def main():
    myboard = TicTacToe()
    gameOver = False
    ch = 'x'
    cell = 0
    while gameOver == False:
        while not myboard.cellIsEmpty(cell):
            cell = 0
            while cell < 1 or cell > 9:
                try:
                    myboard.drawBoard()
                    cell = int(input('It is the turn for ' + ch +'  . What is your move?'))
                except ValueError:
                    print('input a number from 1-9!')
                    None
        myboard.assignMove(cell,ch)
        if myboard.isWinner(ch):
            myboard.drawBoard()
            print(ch +' is winner')
            gameOver =True
            break
        if myboard.boardFull() == True:
            myboard.drawBoard()
            print('its a tie')
            break
        if ch == 'x':
            ch = 'o'
        else:
            ch = 'x'                 
main()