import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./ServiceAccountKey.json")
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection(u'sampleData').document(u'sampleDoc')
doc_ref.update({
    u'firstTest': "first test"
})
print("Finished")

try:
    doc = doc_ref.get()
    print(u'Document data: {}'.format(doc.to_dict()))
except google.cloud.exceptions.NotFound:
    print(u'No such document')