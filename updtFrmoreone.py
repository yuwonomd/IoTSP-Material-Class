#update data more one location
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

#update one more one location
#prepare document format
updatedata ={"todolistA/monday/paper":{"detail":"v7"}, "todolistA/tuesday/filmvideo":{"dealine":"10pm"}}
#update data
db.update(updatedata)

#hasil pada tree firebase pada bagian todolistA/monday/paper: {"detail": "1opm"} akan hilang
#firebase memang demikian sehingga terkadang cara ini tidak di rekomendasikan.