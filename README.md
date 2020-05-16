# raspberry-monitor
Simple temperature monitor script for the Raspberry Pi

Displays temperature data and a color-coded status message of the Raspberry Pi's current CPU temperature for monitoring. It can be run through ssh while the Raspberry Pi is doing another tasks such as running RetroPie.

## Requirements
- Python 3.6 or higher
- [termcolor](https://pypi.org/project/termcolor/)

## Usage
``` bash  
$ python3 raspberry-monitor.py
```

## Example output
``` bash
[OK] 37.8ºC at Sat May 16 2020 12:01:00 GMT+0200
[OK] 38.1ºC at Sat May 16 2020 12:01:01 GMT+0200
[HOT] 87.4ºC at Sat May 16 2020 12:01:02 GMT+0200
```
