#update data one location
import pyrebase

#config Firebase
#Project ID: pythonfirebasetest-e8a27
#Project Name: pythonfirebasetest
config ={
  "apiKey": "AIzaSyAKVopmLwZlZ9aKqtgy05m2vcEYlIDFKCM",
  "authDomain": "pythonfirebasetest-e8a27.firebaseapp.com",
  "databaseURL": "https://pythonfirebasetest-e8a27-default-rtdb.firebaseio.com",
  "projectId": "pythonfirebasetest-e8a27",
  "storageBucket": "pythonfirebasetest-e8a27.appspot.com",
  "messagingSenderId": "932117064911",
  "appId": "1:932117064911:web:207788c953360f0bef9bba",
  "measurementId": "${config.measurementId}"
}

#intialization Firebase
firebase = pyrebase.initialize_app(config)

#intialization database
db = firebase.database()

#prepare data
datamonday = {"deadline": "12pm"}
datamonday2 = {"deadline": "13pm"}

datatuesday = {"deadline": "13pm"}

datawednesday = {"deadline": "13pm"}
datawednesday2 = {"deadline": "13pm"}

#send data to Firebase
#make child = make path for data
#set data for Monday
db.child("todolistA").child("monday").child("paper").set(datamonday)
db.child("todolistA").child("monday").child("pull-request").set(datamonday2)

#set data for Tuesday
db.child("todolistA").child("tuesday").child("filmvideo").set(datatuesday)

#set data for Wednesday
db.child("todolistA").child("wednesday").child("project").set(datawednesday)
db.child("todolistA").child("wednesday").child("voulenter").set(datawednesday2)

#prepare update data
updatedatamonday ={"deadline": "07pm"}
#update data monday
db.child("todolistA").child("monday").child("paper").update(updatedatamonday)

#prepapare update data
updatatuesday = {"deadline": "2am"}
#update data tuesday
db.child("todolistA").child("tuesday").child("filmvideo").update(updatatuesday)
