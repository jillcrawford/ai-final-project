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

# search through cells and see which spaces only have one valid number
def fill_obvious(board):
    progress = True
    while progress:
        progress = False
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    possible = [num for num in range(1,10) if is_valid(board, row, col, num)]
                    if len(possible) == 1:
                        board[row][col] = possible[0]
                        progress = True


# backtracking function to solve more complex puzzles
def backtracking(board):
    for row in range(9):
        for col in range(9):
        if board[row][col] == 0:
            for num in range(1, 10):
                if is_valid(board, row, col, num):
                    board[row][col] = num
                    if backtracking(board):
                        return True
                    board[row][col] = 0
                return False
    return True

# call the function to fill every cell with only one possible solution
fill_obvious(puzzle)
print("-----------")
for r in puzzle:
    print(r)