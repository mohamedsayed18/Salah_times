import os


WARINING_TIME_BEFORE_PRAYER = float(os.environ.get("WARINING_TIME_BEFORE_PRAYER", "1200"))
SLEEP_INTERVAL = float(os.environ.get("SLEEP_INTERVAL", "660"))