# Sure! Here is a simple model for a Connect 4 game in Python:

class Connect4:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.current_player = 1
    
    def place_piece(self, col):
        if col < 0 or col >= self.cols:
            raise ValueError("Invalid column")
        row = self.rows - 1
        while row >= 0 and self.board[row][col] != 0:
            row -= 1
        if row < 0:
            raise ValueError("Column is full")
        self.board[row][col] = self.current_player
        self.current_player = -self.current_player
        return row, col
    
    def check_win(self, row, col):
        # check for horizontal win
        count = 0
        for c in range(col, self.cols):
            if self.board[row][c] != self.current_player:
                break
            count += 1
        for c in range(col - 1, -1, -1):
            if self.board[row][c] != self.current_player:
                break
            count += 1
        if count >= 4:
            return True
        
        # check for vertical win
        count = 0
        for r in range(row, self.rows):
            if self.board[r][col] != self.current_player:
                break
            count += 1
        if count >= 4:
            return True
        
        # check for diagonal win
        count = 0
        r, c = row, col
        while r < self.rows and c < self.cols:
            if self.board[r][c] != self.current_player:
                break
            count += 1
            r += 1
            c += 1
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if self.board[r][c] != self.current_player:
                break
            count += 1
            r -= 1
            c -= 1
        if count >= 4:
            return True
        
        count = 0
        r, c = row, col
        while r < self.rows and c >= 0:
            if self.board[r][c] != self.current_player:
                break
            count += 1
            r += 1
            c -= 1
        r, c = row - 1, col + 1
        while r >= 0 and c < self.cols:
            if self.board[r][c] != self.current_player:
                break
            count += 1
            r -= 1
            c += 1
        if count >= 4:
            return True
        
        return False
    
    def check_full(self):
        for col in range(self.cols):
            if self.board[0][col] == 0:
                return False
        return True
