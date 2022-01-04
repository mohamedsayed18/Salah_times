from subprocess import run as run_bash
import sys
import time
from datetime import date, datetime
from datetime import timedelta


sys.path.append("..")

from ubuntu_automatic_updater.constants import WARINING_TIME_BEFORE_PRAYER as WP
from ubuntu_automatic_updater.constants import SLEEP_INTERVAL as SI
from base.date_time import SalahTimes

def notify(message):
    process = run_bash(["notify-send", message])
    


def run():
    
    prayer_time_manager = SalahTimes()
    today_info = prayer_time_manager.today_info()
    time_now = datetime.now().time()
    time_now = datetime.combine(date.today(), time_now) - timedelta(seconds=5000)
    for k,v in today_info.items():
        prayer_time = datetime.strptime(v, "%H:%M")
        prayer_time = prayer_time.time()
        prayer_time = datetime.combine(date.today(), prayer_time)

        time2p = prayer_time-time_now 
        
        if prayer_time < time_now:
            continue
        time2p = time2p.seconds
        
        if  0 <= time2p <= WP or True:
            notify(f"Prayer {k} is at {v}, {time2p // 60} minutes left")
    
    time.sleep(SI)


if __name__ == "__main__":
    run()