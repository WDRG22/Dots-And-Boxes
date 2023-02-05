from random import *

class Board:
        def __init__(self, matrix, x, y):
                self.matrix = matrix
                self.x = x
                self.y = y
                
#       New 3x3 board looks like:
#      *      F      *      F      *
#
#      F      5      F      7      F
#
#      *      F      *      F      *
#
#      F      9      F      2      F
#
#      *      F      *      F      *
#
#      F      1      F      4      F
#   
#      *      F      *      F      *

        def generateBoard(self):
            for i in range(x):
                for j in range(y):
                    if i % 2 == 0 and j % 2 == 1: # Dots represented by asterisk char
                        self.matrix[i][j] = '*'
                    elif i % 2 == 1 and j % 2 == 1: # Box values as ints
                        self.matrix[i][j] = randint(0,9)
                    else: # Lines/Spaces as booleans
                        self.matrix[i][j] = False