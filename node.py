
# Initialize node with copy of board in order to avoid making moves on game board when generating children
class Node:
    def __init__(self, board, accruedScore):
        self.board = board
        self.accruedScore = accruedScore
        self.children = {}
        self.isTerminal = self.board.isComplete()
        self.heuristicScore = self.getHeuristicScore()
      
    # Children as arr of key, vals, where keys are (row, col) tuple of move 
    # to create value Node  
    def getChildren(self):
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                self.board
        
    def getHeuristicScore():
        pass
        # heuristic where value of current state is equal to current computer's total score plus
        # the average of the remaining unclaimed values?
        
        # or current score plus number of boxes with even number of open edges left,
        # where those with 2 remaining edges are weighted twice as heavily as those with 4?
        
        # If boxes w/ 1 remaining open edge are created, prefers lower values 
    