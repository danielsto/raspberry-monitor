from datetime import datetime
from termcolor import colored

import os
import re
import time


def measure_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return (re.search("\d+\.\d", temp).group())

while True:
    temp = measure_temp()
    status = 'OK' if float(temp) < 85.0 else 'HOT'
    color = 'green' if status == 'OK' else 'red'
    print(f'[{colored(status, color)}] {temp}ºC at {datetime.now()}')
    time.sleep(1)
