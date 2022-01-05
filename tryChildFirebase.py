import pyrebase

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

#initialisaziton Firebase
firebase = pyrebase.initialize_app(config)

#database initialization
db = firebase.database()

#prepare data
data = {"name": "Jesslyn", "age": 23, "addres" : "bukit palma"}

#send data to Firebase
#make child = make path for data
db.child("branch").child("Employes").child("male employes").push(data)
#set for Own Key
#db.child("branch").child("Employes").child("male employes").child("JC").set(data)