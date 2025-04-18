# ai-final-project-crawford.py
# Jillian Crawford

import requests
from bs4 import BeautifulSoup

# scraping the sudoku puzzle from the internet
url = 'https://nine.websudoku.com/?level=1'
web = requests.get(url)
soup = BeautifulSoup(web.text, 'html.parser')

# filling in the puzzle with the info from the web
puzzle = []
# 9 x 9 grid
for row in range(9):
    cur_row = []
    for col in range(9):
        cellnum = f'f{row}{col}'
        cell = soup.find('input', id=cellnum)
        value = cell.get('value') if cell and cell.get('value') else 0
        cur_row.append(int(value))
    puzzle.append(cur_row)

# printing puzzle out
for row in puzzle:
    print(row)

# agent to solve puzzle
# first by checking if there are any cells with only one possible number
# then through backtracking 

# function to determine if a move is valid
def is_valid(board, row, col, num):

    # checking rows and columns
    if num in board[row]:
        return False
    if num in [board[r][col] for r in range(9)]:
        return False
    
    # checking 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    box = [board[r][c] for r in range(start_row, start_row + 3)
           for c in range(start_col, start_col + 3)]
    if num in box:
        return False
    
    return True

