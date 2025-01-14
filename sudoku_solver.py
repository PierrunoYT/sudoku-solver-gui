class SudokuSolver:
    def __init__(self):
        self.size = 9
        self.box_size = 3
        
    def find_empty(self, board):
        """Find an empty cell in the board"""
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] == 0:
                    return i, j
        return None
    
    def is_valid(self, board, num, pos):
        """Check if the number is valid in the given position"""
        # Check row
        for j in range(self.size):
            if board[pos[0]][j] == num and pos[1] != j:
                return False
                
        # Check column
        for i in range(self.size):
            if board[i][pos[1]] == num and pos[0] != i:
                return False
        
        # Check box
        box_x = pos[1] // self.box_size
        box_y = pos[0] // self.box_size
        
        for i in range(box_y * self.box_size, box_y * self.box_size + self.box_size):
            for j in range(box_x * self.box_size, box_x * self.box_size + self.box_size):
                if board[i][j] == num and (i, j) != pos:
                    return False
        
        return True
    
    def solve(self, board):
        """Solve the Sudoku puzzle using backtracking"""
        empty = self.find_empty(board)
        if not empty:
            return True
            
        row, col = empty
        
        for num in range(1, 10):
            if self.is_valid(board, num, (row, col)):
                board[row][col] = num
                
                if self.solve(board):
                    return True
                    
                board[row][col] = 0
                
        return False
