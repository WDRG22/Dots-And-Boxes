from random import *

class Board:
        def __init__(self, x, y):
                self.rows = y * 2 + 1
                self.cols = x * 2 + 1
                self.matrix = self.generateBoard()

        def generateBoard(self): # Initializes new board
            m = []
            for row in range(self.rows):
                tmp = []
                for col in range(self.cols):
                    if row % 2 == 0 and col % 2 == 0: # Dots represented by asterisk char
                        tmp.append('*')
                    elif row % 2 == 1 and col % 2 == 1: # Box values as ints
                        tmp.append(randint(1,5))
                    else: # Lines/Spaces as booleans
                        tmp.append(False)
                m.append(tmp)
            return m
                        
        def display(self): # Displays board state
            for row in range(self.rows):
                for col in range(self.cols):
                    if row % 2 == 0 and isinstance(self.matrix[row][col], bool):
                        if self.matrix[row][col]:
                            print(' --- ', end='')
                        else:
                            print('     ', end='')                            
                    elif row % 2 == 1 and isinstance(self.matrix[row][col], bool):
                        if self.matrix[row][col]:
                            print('|', end='')
                        else:
                            print(' ', end='')                    
                    else:
                        if isinstance(self.matrix[row][col], int):                                          
                            print('  ' + str(self.matrix[row][col]), end='  ')
                        else:
                            print(self.matrix[row][col], end='')
                print()
                        
                        
        def isComplete(self): # Checks if no more moves available                       
            return not any(False in row for row in self.matrix)
        
        # Makes a move on the board. Return value of box if box completed, or 0 
        def move(self, row, col, name):                         
            score = 0
            if row % 2 == 0: # Horizontal line
                self.matrix[row][col] = True
                if row == 0: # First row (Check box below)
                    score += self.checkDown(row, col, name)
                elif row == self.rows - 1: # Last row (Check box above)                
                    score += self.checkUp(row, col, name)
                else: # Intermediate row (Check boxes above and below)                
                    score += self.checkUp(row, col, name)
                    score += self.checkDown(row, col, name)
            else: # Vertical line
                self.matrix[row][col] = True
                if col == 0: # First col (Check right box)                
                    score += self.checkRight(row, col, name)
                elif col == self.rows - 1: # Last col (Check left box)
                    score += self.checkLeft(row, col, name)
                else: # Intermediate col (Check right and left box)                
                    score += self.checkRight(row, col, name)
                    score += self.checkLeft(row, col, name)
            return score 
        
        def checkUp(self, row, col, name): # Checks if box above move is completed
            score = 0
            if (self.matrix[row+-1][col-1] and
                    self.matrix[row-1][col+1] and
                    self.matrix[row-2][col]):            
                
                score += self.matrix[row-1][col]
                self.matrix[row-1][col] = f" {name} {score} "
            return score
            
        def checkDown(self, row, col, name): # Checks if box below move is completed
            score = 0
            if (self.matrix[row+1][col-1] and
                    self.matrix[row+1][col+1] and
                    self.matrix[row+2][col]):
                score += self.matrix[row+1][col]
                self.matrix[row+1][col] = f" {name} {score} "
            return score
        
        def checkRight(self, row, col, name): # Checks if box to right of move is completed
            score = 0
            if (self.matrix[row-1][col+1] and
                    self.matrix[row+1][col+1] and
                    self.matrix[row][col+2]):
                score += self.matrix[row][col+1]
                self.matrix[row][col+1] = f" {name} {score} "
            return score
            
        def checkLeft(self, row, col, name): # Checks if box to left of move is completed
            score = 0
            if (self.matrix[row-1][col-1] and
                    self.matrix[row+1][col-1] and
                    self.matrix[row][col-2]):
                score += self.matrix[row][col-1]
                self.matrix[row][col-1] = f" {name} {score} "
            return score