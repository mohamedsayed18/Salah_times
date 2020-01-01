# Salah_times
Reminder of salah(prayes) time for linux

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
you can get the url of your city from [this website](https://en.halalguide.me) and click on the salah time the URL should look like this if we choose cairo for example
https://en.halalguide.me/kair/namaz-time
and you can pass it to the constructor like this <br/>
```mycity = SalahTimes(url=https://en.halalguide.me/kair/namaz-time) ```

#### future work and contribution 
* a demon that run in the back ground give notifications
* GUI version