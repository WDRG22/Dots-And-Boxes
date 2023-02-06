from board import Board
from player import Player
import main

class Game:
    def __init__(self, x, y):
        self.board = Board(x, y)
        self.player = Player(self.board)
        self.computer = Player(self.board)

    def start(self):
        self.playerTurn()
        
    def playerTurn(self):
        if self.board.isComplete():
            self.endGame()
                 
        self.board.display()        
        print("Your move! Enter the row and column where you would like to place an edge")        
        while True: # Move validation
            row = input(print(f"Row (0-{self.board.rows}): "))
            col = input(print(f"Column (0-{self.board.cols}): "))                
            if row + col % 2 == 0:
                print("That location denotes either a dot or a box value! Find an blank edge instead")            
            elif self.currentBoard[row, col] is True:
                print("There's already a line there! Find an blank edge instead")
            else:
                break
        self.player.score += self.player.move(row, col)
        
        self.computerTurn()        

    # TODO
    def computerTurn(self):
        # self.playerTurn()
        pass
    
    # TODO improve(?)
    def endGame(self):
        print("Game over! Final scores:")
        print("You: ", self.player.score)
        print("Computer: ", self.computer.score)
        if self.player.score > self.computer.score:
            print("You won!")
        elif self.player.score < self.computer.score:
            print("The computer won!")
        else:
            print("It's a tie!")
        again = input(print("Play again? (y/n)"))
        if again == 'y':
            main.main()
        else:
            exit()
        