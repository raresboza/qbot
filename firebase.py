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

db = firebase.database()
# auth = firebase.auth()
# storage = firebase.storage()

dummyMovie = {
    'Movie_id': 0,
    'Title': 'Test movie',
    'Rating': 10.0,
    'Rating_count': 85
}

dummyMu = {
    'Discord_id': -1,
    'Votes': [{
        'Vote': 10.0,
        'Movie_id': 0
    }]
}


def vote(Discord_id, Movie_id):
    # caz in care nu exista filmul -> inseram film (apel de functie)

    # caz in care nu exista discord_id

    # caz in care exista discord_id

    return 0


def init():
    db.child("Movies").child("Movie").push(dummyMovie)
    db.child("Movies").child("MovieUsers").push(dummyMu)


if __name__ == "__main__":
    init()
