
# Define a class for both player and AI to track moves and score
# Each player object will possess a reference to the single board object(?)
class Player:
    def __init__(self, currentBoard):
        self.score = 0
        self.currentBoard = currentBoard
        
    
        