from flask import Flask, render_template, request, jsonify
from sudoku_solver import SudokuSolver
import json

app = Flask(__name__)
solver = SudokuSolver()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json()
    board = data['board']
    
    if solver.solve(board):
        return jsonify({'success': True, 'solution': board})
    return jsonify({'success': False, 'message': 'No solution exists'})

if __name__ == '__main__':
    app.run(debug=True) 