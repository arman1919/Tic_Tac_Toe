

class Board:
    def __init__(self) -> None:
        self.board = [ ["","",""]
                      ,["","",""]
                      ,["","",""]]
        
    def restart(self):
        self.board =  [ ["","",""]
                      ,["","",""]
                      ,["","",""]]
        
    def  press_symbol(self,position,sybol):
        row = (position - 1) // 3  
        col = (position - 1) % 3
   
        self.board[row][col] = sybol
    
    
    
    def check_winner(self):
        board = self.board
        
        for row in board:
            if all(cell == 'X' for cell in row):
                return 'X'
            elif all(cell == 'O' for cell in row):
                return 'O'

        for col in range(3):
            if all(board[row][col] == 'X' for row in range(3)):
                return 'X'
            elif all(board[row][col] == 'O' for row in range(3)):
                return 'O'

        if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
            return 'X'
        elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
            return 'O'
            
        return None
    
    
            


class Player:
    def __init__(self,name,sybol):
        self.name = name
        self.sybol = sybol
        
    
        