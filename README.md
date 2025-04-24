# ai-final-project

## Project Description
This project scrapes a live Sudoku puzzle from the internet, analyzes it, and solves it using a two-phase AI agent. First, it fills in cells that have only one valid number based on Sudoku rules. It does this by creating a list for each cell with every possible value for that cell. If there is only one value in the list, then it inserts that value into its respective cell. Then, it switches to a recursive backtracking algorithm to crack the tougher parts of the puzzle. It starts by assuming that a value goes into a cell and then continues to fill in other cells based on that assumption until the puzzle is either solved or it runs into an error. If the puzzle it solves, it returns its solved variation. If it runs into an error, it backtracks and fills the cell in with a different value. It repeats this backtracking algorithm until a valid solved possible is achieved.

The goal: utilize both efficiency and intelligence in solving logic-based puzzles using basic AI strategies.

## How to Install/Run

### Requirements
- Python 3.x
- Required libraries:
  - `requests`
  - `beautifulsoup4`

You can install the necessary packages with:

`pip install requests beautifulsoup4`

### Running It
- You can run this program by typing `python ai-final-project-crawford.py` in your command terminal.
- Once you run it, the program will:
  - Scrape a level 3 (hard) sudoku puzzle from websudoku.com
  - Print the original puzzle
  - Print the puzzle after filling in the pbvious cells
  - Print the fully solved puzzle after using backtracking


