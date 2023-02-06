#TODO

class Node:
    def __init__(self, board):
        self.board = board
        self.score = 0
        self.children = {}
        self.isTerminal = False
        
        