import sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def upload_txt():
    # set up the firebase conection using your downloaded .json file
    cred = credentials.Certificate('./hockey-11fc7-firebase-adminsdk-kq13h-7700bd4fb9.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    # open the file
    filename = sys.argv[1] + ".txt"
    file = open(filename, "r")

    # Firebase data must be uploaded as a python dict
    data = { }
    for line in file:
        title = line.split(": ")
        data[title[0]] = float(title[1])
    print(data)
    db.collection('D1_09_1').document('01_10_2010_weights').set(data)

# define correct usage
if len(sys.argv) == 2:
    try:
        upload_txt()
    except FileNotFoundError:
        print("ERROR: file not found")
    except TypeError:
        print("ERROR: Firebase dict needs 'str' keys")
else:
    print("ERROR: incorrect number of arguments")
    print("usage: python3 upload_file.py [filename]")
