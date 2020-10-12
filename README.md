# LogicAnalyzer
Some python scripts for playing around on different bus lines and GPIO pins.

This project started with experimentation related to a ten dollar Saleae clone logic analyzer, hence the name.

1) Install dependencies (eg "pip install pyserial")

  pyserial  
  smbus2
  
1) you can just run python one_channel.py to do a loop over GPIO 29 (BCM 21), which is the bottom right pin on the pi