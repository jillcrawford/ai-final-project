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
        cellnum = (row)(col)
        cell = soup.find('input', id=cellnum)
        value = cell.get('value') if cell else 0
        cur_row.append(int(value))
    puzzle.append(cur_row)

# printing puzzle out
for row in puzzle:
    print(row)