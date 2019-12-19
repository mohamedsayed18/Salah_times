import datetime

today = str(datetime.datetime.now()).split()
day = today[0].split('-')[2]
print(day)
