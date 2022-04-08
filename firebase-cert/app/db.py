import os

from dotenv import load_dotenv
from firebase_admin import credentials, initialize_app, storage

load_dotenv()

cwd = os.getcwd()
BUCKET_NAME = os.getenv('BUCKET_NAME')


cred = credentials.Certificate(cwd + "/generator-certificate-firebase-adminsdk-b95q7-a5ceaa08f2.json")

app = initialize_app(cred, {
  "storageBucket": "generator-certificate.appspot.com"
})

bucket = storage.bucket(app=app)



# ref: https://medium.com/@abdelhedihlel/upload-files-to-firebase-storage-using-python-782213060064