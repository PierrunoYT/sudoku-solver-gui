import tkinter as tk
from tkinter import messagebox
import logging
import sys
from sudoku_solver import SudokuSolver

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('sudoku.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

class SudokuGUI:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.root = tk.Tk()
        self.root.title("Sudoku Solver")
        self.solver = SudokuSolver()
        self.cells = {}
        self.logger.info("Initializing Sudoku GUI")
        self.create_board()
        self.create_buttons()
        
    def create_board(self):
        """Create the Sudoku board GUI"""
        for i in range(9):
            for j in range(9):
                cell = tk.Entry(self.root, width=2, font=('Arial', 18), justify='center')
                cell.grid(row=i, column=j, padx=1, pady=1)
                
                # Add thicker borders between 3x3 boxes
                if (i in [0, 3, 6] and j in [0, 1, 2, 3, 4, 5, 6, 7, 8]):
                    cell.grid(pady=(3, 1))
                if (i in [2, 5, 8] and j in [0, 1, 2, 3, 4, 5, 6, 7, 8]):
                    cell.grid(pady=(1, 3))
                if (j in [0, 3, 6] and i in [0, 1, 2, 3, 4, 5, 6, 7, 8]):
                    cell.grid(padx=(3, 1))
                if (j in [2, 5, 8] and i in [0, 1, 2, 3, 4, 5, 6, 7, 8]):
                    cell.grid(padx=(1, 3))
                    
                self.cells[(i, j)] = cell
    
    def create_buttons(self):
        """Create solve and clear buttons"""
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_board)
        solve_button.grid(row=9, column=0, columnspan=4, pady=10)
        
        clear_button = tk.Button(self.root, text="Clear", command=self.clear_board)
        clear_button.grid(row=9, column=5, columnspan=4, pady=10)
    
    def get_board(self):
        """Get the current board state"""
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                value = self.cells[(i, j)].get()
                try:
                    row.append(int(value) if value else 0)
                except ValueError:
                    messagebox.showerror("Error", "Invalid input! Please enter numbers only.")
                    return None
            board.append(row)
        return board
    
    def set_board(self, board):
        """Set the board state in the GUI"""
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                self.cells[(i, j)].delete(0, tk.END)
                if value != 0:
                    self.cells[(i, j)].insert(0, str(value))
    
    def solve_board(self):
        """Solve the current Sudoku puzzle"""
        self.logger.info("Attempting to solve the board")
        board = self.get_board()
        if board:
            self.logger.debug("Current board state: %s", board)
            if self.solver.solve(board):
                self.logger.info("Solution found")
                self.set_board(board)
            else:
                self.logger.warning("No solution exists for the given puzzle")
                messagebox.showinfo("Result", "No solution exists!")
    
    def clear_board(self):
        """Clear all cells in the board"""
        self.logger.info("Clearing the board")
        for cell in self.cells.values():
            cell.delete(0, tk.END)
    
    def run(self):
        """Start the GUI application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = SudokuGUI()
    app.run()
