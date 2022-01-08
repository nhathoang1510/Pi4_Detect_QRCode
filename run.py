#!/usr/bin/python3
import time
import _thread
import os

def startprgm(i):
    print ("Running thread %d",i)
    if (i == 0):
        time.sleep(0.1)
        print('Running: QR')
        os.system("sudo -H -u pi /usr/bin/python3 /home/pi/qr.py")
    elif (i == 1):
        print('Running: QR2')
        time.sleep(0.1)
        os.system("sudo -H -u pi /usr/bin/python3 /home/pi/qr2.py")
    else:
        i=0
for i in range(2):
    _thread.start_new_thread(startprgm,(i,))