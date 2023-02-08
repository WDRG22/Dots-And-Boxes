from game import Game


# Dimensions will be doubled then incremented by one, as we will use a 2D Matrix to represent the board,
# where an n-by-n board will have row and column indices representing either:
# 0: dot, 1: space/line, 2: dot, 3: space/line, 4: dot, etc OR
# 0: space/line, 1: box value, 2: space/line, 3: box value, 4: space/line, etc
# e.g. Board[0][0] will be the top left most dot, Board[0][1] and Board[1][0] will be the horizontal and vertical lines placements from that dot
# and Board[1][1] will be the value of the top left most square once completed, and so on
def main():
    print("Welcome to Dots and Boxes!")
    print("Define the board size to begin: ")

    # while True:
    #         x = int(input("Input X-Dimension (2 or greater): "))
    #         y = int(input("Input Y-Dimension (2 or greater): "))
    #         plies = int(input("Now, set the difficult of your AI Competitor by declaring how many plies ahead it will compute: "))
    #         # Write string input validation
    #         if x < 2 or y < 2 or plies < 2:
    #             print("Dimension and ply values must be 2 or greater")
    #         else:
    #             break        
    newGame = Game(2, 2, 0)
    newGame.start()
        

if __name__ == "__main__":
    main()


# Testing
# from player import Player
# from board import Board

# newGame = Game(3, 3)
# newGame.start()