from random import *

class Board:
        def __init__(self, x, y):
                self.rows = y * 2 + 1
                self.cols = x * 2 + 1
                self.matrix = self.generateBoard()

        def generateBoard(self):
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
                        
        def display(self):
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
                        
                        
        def isComplete(self):                            
            return not any(False in row for row in self.matrix)