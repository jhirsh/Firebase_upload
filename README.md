# Firebase_upload
Goal: upload .txt files to Firebase Cloud Firestore in a Python script.
Scope:
* Must define the type being uploaded
* Input is of form `key: value` in .txt file

## Environment setup
Navigate to your working directory.
* `python3 -m venv env` sets up your virtual environment
* `pip3 install --upgrade pip` to make update pip version
* `pip install firebase-admin` to install Firebase credentials

Download `.json` certificate from Firebase Project
![alt text](https://github.com/jhirsh/firebase_upload/firebase_download_key.png "Logo Title Text 1")

## Notes on Firebase uploading
* `db.collection('<collection id>').document('<document id>').set(data)`
* `data` must be a python dict. Fill it exactly how you'd like your document to be structured.

## Running upload script
`python3 upload_file.py [filename]`
`[filename]` doesn't need extension, and will automatically `.txt`

## Further iterations
* While this method works well for uploading a single file, if you have collected a lot of data, it might make more sense to be able to upload multiple files at once. Could implement it with bash scripting or in the python script itself.
* Dynamically create the `data` dictionary to properly type all variables instead of changing it on case-by-case basis for script.


