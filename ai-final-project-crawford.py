# ai-final-project-crawford.py
# Jillian Crawford

import requests
from bs4 import BeautifulSoup

# scraping the sudoku puzzle from the internet
url = 'https://nine.websudoku.com/?level=1'
web = requests.get(url)
soup = BeautifulSoup(web.text, 'html.parser')

