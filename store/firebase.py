import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('credentials/bajukawenstore-firebase-adminsdk-fbsvc-2e8a4486ea.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
