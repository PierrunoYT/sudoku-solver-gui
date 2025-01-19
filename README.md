# Sudoku Solver

A web-based Sudoku solver that uses a backtracking algorithm to solve any valid Sudoku puzzle.

## Features

- Clean, modern web interface
- Real-time input validation
- Solves any valid Sudoku puzzle
- Clear and intuitive controls

## Installation

### Windows
1. Install Python 3.x from [python.org](https://python.org)
2. Clone this repository:
```bash
git clone https://github.com/yourusername/sudoku-solver.git
cd sudoku-solver
```
3. Install dependencies:
```bash
python -m pip install -r requirements.txt
```

### macOS
1. Install Python if not already installed:
```bash
brew install python3
```
2. Clone this repository:
```bash
git clone https://github.com/yourusername/sudoku-solver.git
cd sudoku-solver
```
3. Install dependencies:
```bash
pip3 install -r requirements.txt
```

### Linux
1. Install Python if not already installed:
```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip

# Arch Linux
sudo pacman -S python python-pip
```
2. Clone this repository:
```bash
git clone https://github.com/yourusername/sudoku-solver.git
cd sudoku-solver
```
3. Install dependencies:
```bash
pip3 install -r requirements.txt
```

## Usage

### Windows
1. Start the web server:
```bash
python app.py
```

### macOS/Linux
1. Start the web server:
```bash
python3 app.py
```

### Using the Web Interface
1. Open your web browser and navigate to:
```
http://localhost:5000
```

2. Enter the numbers in the Sudoku grid:
   - Use numbers 1-9
   - Leave empty cells for unknown values
   - The Solve button will be enabled once you enter at least one number

3. Click "Solve" to find the solution
   - If a solution exists, it will be displayed in the grid
   - If no solution exists, you'll see an error message

4. Click "Clear" to reset the grid and start over

## Technical Details

- Backend: Python Flask server with a backtracking algorithm
- Frontend: HTML5, CSS3, and vanilla JavaScript
- Styling: Bootstrap 5 for modern UI components

## Files

- `app.py` - Flask web server and API endpoints
- `sudoku_solver.py` - Core solving algorithm
- `templates/index.html` - Web interface
- `requirements.txt` - Python dependencies
