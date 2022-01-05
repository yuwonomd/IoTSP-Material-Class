import pyrebase

#config Firebase
config ={
  "apiKey": "AIzaSyDYnaNCNrI72-yBBfNMJfQSDbAxPUmOjJ0",
  "authDomain": "test-54007.firebaseapp.com",
  "databaseURL": "https://test-54007-default-rtdb.firebaseio.com",
  "projectId": "test-54007",
  "storageBucket": "test-54007.appspot.com",
  "messagingSenderId": "122202100331",
  "appId": "1:122202100331:web:af05ecc819470ae28d172e",
  "measurementId": "G-NBH1Z82J14"
}

#intialization Firebase
firebase = pyrebase.initialize_app(config)

#intialization database
db = firebase.database()

#Create Own Key
#Create data
data = {"age":24, "addres":["Indonesia", "Los Angeles"]}
#Create Key
db.child("Edwin").set(data) 
