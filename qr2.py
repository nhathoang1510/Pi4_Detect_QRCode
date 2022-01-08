import numpy as np
import serial
import pyrebase

ser = serial.Serial(
         port = '/dev/ttyUSB0',
         baudrate = 115200,
         parity = serial.PARITY_NONE,
         stopbits = serial.STOPBITS_ONE,
         bytesize = serial.EIGHTBITS,
         timeout=1
)

config = {
  "apiKey": "AIzaSyAULD_5XOVsrub8anXNRIQkPdOEX8Z1Qjw",
  "authDomain": "project2-b7d1e.firebaseapp.com",
  "databaseURL": "https://project2-b7d1e-default-rtdb.firebaseio.com",
  "storageBucket": "project2-b7d1e.appspot.com"
};
firebase = pyrebase.initialize_app(config)

while True:
      database = firebase.database()
      rb_tar=database.child("User").child("user").get().val()
      btn_home=database.child("Button").child("home").get().val()
      btn_start=database.child("Button").child("start").get().val()
      btn_stop=database.child("Button").child("stop").get().val()
      print("rb_tar: "+rb_tar)
      send="E"+btn_home+btn_start+btn_stop+"000"+rb_tar+"E"
      print("send: "+send)
      ser.write(send.encode('utf-8'))
