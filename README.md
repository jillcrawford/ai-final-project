# ai-final-project

## Project Description
This project scrapes a live Sudoku puzzle from the internet, analyzes it, and solves it using a two-phase AI agent. First, it fills in cells that have only one valid number based on Sudoku rules (the "duh" phase). Then, it switches to a recursive backtracking algorithm to crack the tougher parts of the puzzle (the "big brain" phase).

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


