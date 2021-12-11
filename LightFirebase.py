#import library
from pyfirmata import util, Arduino
import pyfirmata
import pyrebase
import time

#setup Config
config = {
  "apiKey": "AIzaSyDYnaNCNrI72-yBBfNMJfQSDbAxPUmOjJ0",
  "authDomain": "test-54007.firebaseapp.com",
  "databaseURL": "https://test-54007-default-rtdb.firebaseio.com",
  "projectId": "test-54007",
  "storageBucket": "test-54007.appspot.com",
  "messagingSenderId": "122202100331",
  "appId": "1:122202100331:web:af05ecc819470ae28d172e",
  "measurementId": "G-NBH1Z82J14"
}

#firebase configuration using library pyrebase
firebase = pyrebase.initialize_app(config)

#create database
db = firebase.database()

#setting port Arduino
port = "/dev/cu.usbmodem1101" #--> look through Arduino IDE for port
#setting Board Arduino
board = Arduino(port)
#setting pin Arduino
pin = board.get_pin('a:3:i')

#setting continue reading
it = pyfirmata.util.Iterator(board)
it.start()

#main program
while True:
    analog_value = pin.read() #start reading value
    
    if analog_value == None:  #if value None
      print(analog_value)
    else:                     #if value not None
      #data push to Firebase
      db.child("iot").push(analog_value) 
    #string_value = str(analog_value)

    #data = {"intensitas": string_value}
#push data to realtime database
#create data variable
    #db.child("iot").child("ligt").update(data)

#config = {
 # "apiKey": "AIzaSyDYnaNCNrI72-yBBfNMJfQSDbAxPUmOjJ0",
 # "authDomain": "test-54007.firebaseapp.com",
 # "projectId": "test-54007",
 # "storageBucket": "test-54007.appspot.com",
 # "messagingSenderId": "122202100331",
 # "appId": "1:122202100331:web:74f7b0d1870bf65b8d172e",
 # "measurementId": "G-0XM0F61H9P"
#}

#firebase configuration using library pyrebase
#firebase = pyrebase.initialize_app(config)

#create database
#db = firebase.database()

#data = {"intensitas":"123"}

#push data to realtime database
#db.child("iot").push(data)
#create data variable
#db.child("iot").child("ligt").set(data)
