# Salah_times
Reminder of salah(prayes) time for linux
![](https://github.com/mohamedsayed18/Salah_times/blob/master/today.png)
Run the script
```python3 ~/main.py```<br/>
or run by an alias<br/>
* open the .bashrc ```gedit ~/.bashrc```
* put this line ```alias prayer='python3 ~/main.py'```<br/>
make sure that the scripts are on the home directory or you need to change the directory in the alias

#### How to use date_time module
```python
from date_time import SalahTimes
```
create an instance
```python
mycity = SalahTimes()
```
to display the salah times for month
```
month = mycity.month_table()    #get the whole month times
for day in month:
  print (day)
```
for today
```
mycity.today_prayer()   #print today times
```
you can get the url of your city from [this website](https://en.halalguide.me) and click on the salah time the URL should look like this if we choose cairo for example
https://en.halalguide.me/kair/namaz-time
and you can pass it to the constructor like this <br/>
```mycity = SalahTimes(url=https://en.halalguide.me/kair/namaz-time) ```

#### future work and contribution
* a demon that run in the back ground give notifications
* GUI version

#### Useful links
[scraper tutorial](https://hackernoon.com/building-a-web-scraper-from-start-to-finish-bb6b95388184)<br/>
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)<br/>
[requests](https://requests.readthedocs.io/en/master/api/#main-interface)<br/>
[know the date, time of today](https://docs.python.org/3/library/datetime.html)<br/>
