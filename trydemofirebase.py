import pyrebase #import library

#config firebase
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

#initialization firebase
firebase = pyrebase.initialize_app(config)

#database initialization
db = firebase.database()

#prepare data
data = {"name": "John", "age": 33, "addres" : "bukit Rejeki"}
#send data to Firebase
db.push(data) 
