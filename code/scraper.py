import requests
from bs4 import BeautifulSoup
import datetime

url = 'https://en.halalguide.me/innopolis/namaz-time'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table')
Month = []
for row in table.findAll('tr'):
    list_of_cells=[]

    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    if len(list_of_cells):
        del list_of_cells[0]
        Month.append(list_of_cells)
#print(Month)
salah = ['Fajr','Shuruk','Zuhur','Asr','Maghrib','Isha']
#print today times
today = str(datetime.datetime.now()).split()
date = today[0].split('-')[2]
for day in Month:
    if date == day[0]:
        del day[0:2]
        for i in range(6):
            print(salah[i],'  ',day[i])
        break
