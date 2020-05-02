import urllib
import requests

from bs4 import BeautifulSoup
import webbrowser

page = requests.get("https://covidtracking.com/data/us-daily")
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

# Get table of covid data:

headers = []
table = soup.find(class_="table-module--table--1HfxU")


## headers
head = table.find('thead')
head2 = head.find('tr')
print(head2)
for header in head2.find_all('th'):
    headers.append(header.get_text())


## output table 
for row in table:
    for row in soup.find_all('tr'):
        i = 0
        for column in row.find_all('td'): 
            print(headers[i] + ": " + column.get_text())
            i += 1