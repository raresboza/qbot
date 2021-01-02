import pyrebase
firebase_credentials = open("firebase.config", "r")

apiKey = firebase_credentials.readline().rstrip('\n')
authDomain = firebase_credentials.readline().rstrip('\n')
projectId = firebase_credentials.readline().rstrip('\n')
storageBucket = firebase_credentials.readline().rstrip('\n')
messagingSenderId = firebase_credentials.readline().rstrip('\n')
appId = firebase_credentials.readline().rstrip('\n')
measurementId = firebase_credentials.readline().rstrip('\n')
databaseURL = firebase_credentials.readline().rstrip('\n')

firebaseConfig = {
    'apiKey': apiKey,
    'authDomain': authDomain,
    'projectId': projectId,
    'storageBucket': storageBucket,
    'messagingSenderId': messagingSenderId,
    'appId': appId,
    'measurementId': measurementId,
    'databaseURL': databaseURL
    }

firebase = pyrebase.initialize_app(firebaseConfig)

#db = firebase.database()
#auth = firebase.auth()
#storage = firebase.storage()