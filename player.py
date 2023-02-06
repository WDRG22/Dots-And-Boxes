
# Define a class for both player and AI to track moves and score
# Each player object will possess a reference to the single board object(?)
class Player:
    def __init__(self, currentBoard):
        self.currentBoard = currentBoard
        self.score = 0
        
    # Can only make moves on even row and odd col (horizontal lines) or odd row and even col (vertical lines)
    # i.e. sum of row and col must be odd number for valid move, and val at row,col must be False
    # Return value of box if box completed, or 0 
    def move(self, row, col):                        
        score = 0
        if row % 2 == 0: # Horizontal line
            if row == 0: # First row (Check below box)
                score += self.checkDown()
            elif row == self.currentBoard.y - 1: # Last row (Check above box)                
                score += self.checkUp()
            else: # Intermediate row (Check above and below box)                
                score += self.checkUp()
                score += self.checkDown()
        else: # Vertical line
            if col == 0: # First col (Check right box)                
                score += self.checkRight()
            elif col == self.currentBoard.y - 1: # Last col (Check left box)
                score += self.checkLeft()
            else: # Intermediate col (Check right and left box)                
                score += self.checkRight()
                score += self.checkLeft()
        return score 
    
    def checkUp(self, row, col):
        score = 0
        if (self.currentBoard.matrix[row+-1][col-1] and
                self.currentBoard.matrix[row-1][col+1] and
                self.currentBoard.matrix[row-2][col]):
            score += self.currentBoard.matrix[row-1][col] 
        return score
        
    def checkDown(self, row, col):
        score = 0
        if (self.currentBoard.matrix[row+1][col-1] and
                self.currentBoard.matrix[row+1][col+1] and
                self.currentBoard.matrix[row+2][col]):
            score += self.currentBoard.matrix[row+1][col] 
        return score
    
    def checkRight(self, row, col):
        score = 0
        if (self.currentBoard.matrix[row-1][col+1] and
                self.currentBoard.matrix[row+1][col+1] and
                self.currentBoard.matrix[row][col+2]):
            score += self.currentBoard.matrix[row][col+1] 
        return score
        
    def checkLeft(self, row, col):
        score = 0
        if (self.currentBoard.matrix[row-1][col-1] and
                self.currentBoard.matrix[row+1][col-1] and
                self.currentBoard.matrix[row][col-2]):
            score += self.currentBoard.matrix[row][col-1] 
        return score
    
        