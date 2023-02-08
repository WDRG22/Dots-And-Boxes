from board import Board
from algorithm import miniMaxSearch

class Game:
    def __init__(self, x, y, plies):
        self.board = Board(x, y)
        self.playerName = 'P'
        self.playerScore = 0
        self.computerName = 'C'
        self.computerScore = 0
        self.plies = plies

    def start(self): # Starts game with player's turn
        self.playerTurn()
        
    def playerTurn(self): # Checks if game complete, gets and makes player move, adjusts score, then computer's turn
        if self.board.isComplete():
            self.endGame()                  
        row, col = self.getPlayerMove()        
        self.playerScore += self.board.move(row, col, self.playerName)
        self.computerTurn()        

    # TODO
    def computerTurn(self):
        # move = miniMaxSearch(self.board, self.plies, self.computer.totalScore)
        if self.board.isComplete():
            self.endGame()
        row, col = self.getPlayerMove()        
        self.computerScore += self.board.move(row, col, self.computerName)
        self.playerTurn()
    
    def getPlayerMove(self): # Gets and validates user input for move, returns row and col of move
        print(f"\nPLAYER'S TURN (Score: {self.playerScore})")        
        print("Your move! Enter the row and column where you would like to place an edge")
        self.board.display()
        while True: # Move validation
            print(f"Row (0-{self.board.rows - 1}): ", end='')
            row = int(input())
            print(f"Column (0-{self.board.cols - 1}): ", end='')
            col = int(input())
            if row >= self.board.rows or col >= self.board.cols:
                print("Index out of range. Try again")
            elif (row + col) % 2 == 0:
                print("That location denotes either a dot or a box value! Find an blank edge instead")            
            elif self.board.matrix[row][col] is True:
                print("There's already a line there! Find an blank edge instead")
            else:
                break
        return row, col
    
    def endGame(self):
        print("\n\nGAME OVER!\n")
        self.board.display()
        print("You: ", self.playerScore)
        print("Computer: ", self.computerScore)
        if self.playerScore > self.computerScore:
            print("YOU WIN!")
        elif self.playerScore < self.computerScore:
            print("THE COMPUTER WINS!")
        else:
            print("IT'S A TIE!")
        exit()
        

        