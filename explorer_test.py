#! /usr/bin/python3

import explorerhat
import random
import time
#import PiCamera

#kamera = PiCamera()

explorerhat.light[0].fade(0, 100, 0.5)

# Slår på alle lysene
for x in range(0,4):
    explorerhat.light[x].on()        

# Sover i 2 sek. (dvs. lysene er på i 2 sek.
time.sleep(2)

# Slår av alle lysene
for x in range(0,4):
    explorerhat.light[x].off()
    
# Motortest
explorerhat.motor.forwards(50)
time.sleep(1)
explorerhat.motor.backwards(0)

try:
    while True:
        explorerhat.motor.forwards(50)
except KeyboardInterrupt:
    explorerhat.motor.stop()
    print("Programmet avsluttar.")    