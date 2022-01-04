"""Time of the prayes to day"""
import requests
from bs4 import BeautifulSoup
import datetime

class SalahTimes:
    """salah time for your city"""
    def __init__(self,url='https://en.halalguide.me/innopolis/namaz-time'):
        """scrap the web for times"""
        self.url = url
        self.month = []
        self.salah = ['Fajr','Shuruk','Zuhur','Asr','Maghrib','Isha']
        #get the prayer times table
        response = requests.get(self.url)   #get the response from website
        html = response.content #html of the page
        soup = BeautifulSoup(html, 'html.parser')
        self.table = soup.find('table')
        self.salah = ['Fajr','Shuruk','Zuhur','Asr','Maghrib','Isha']

    def month_table(self):
        """get the days's prayer times in the list Month"""
        #print("yes")
        for row in self.table.findAll('tr'):
            #print(row)
            list_of_cells=[]
            for cell in row.findAll('td'):
                #print(cell)
                text = cell.text.replace('&nbsp;', '') #in case of HTML format
                #print(text)
                list_of_cells.append(text)
                #print(len(list_of_cells))
            if len(list_of_cells):  #avoid empty lists
                del list_of_cells[0]
                self.month.append(list_of_cells)
        return self.month

    def today_prayer(self, return_ok=False):
        """print the today salahs"""
        self.month_table()  # get the table for the month
        today = str(datetime.datetime.now()).split()    #[date, time]
        date = int(today[0].split('-')[2])   #date
        for day in self.month: # search for today in the month
            if date == int(day[0]):
                del day[0:2]
                if return_ok:
                    return dict(zip(self.salah, day))
                for i in range(6):  # print salah and it's time
                    print(self.salah[i],day[i])
                break
    
    def today_info(self):
        return self.today_prayer(return_ok=True)
