#!/usr/bin/python
import time
from gpiozero import MCP3008
 
divider = MCP3008(0)
 
while True:
    print(divider.value)
    time.sleep(2.0)
