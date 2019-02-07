# Firebase_upload
<b>Goal:</b> upload .txt files to Firebase Cloud Firestore in a Python script. <br />
<img src="https://github.com/jhirsh/firebase_upload/blob/master/images/firebase_uploaded_data.png" alt="Firebase .json certificate"  display=block margin-left=atuo margin-right=auto width=75%>

<b>Files:</b>
* `2010_01_10_weights.txt` - input for the script that will be uploaded to Firebase
* `upload_file.py` - script that performs upload

## Environment setup
Navigate to your working directory.
* `python3 -m venv env` sets up your virtual environment
* `pip3 install --upgrade pip` to make update pip version
* `pip install firebase-admin` to install Firebase credentials

Download `.json` certificate from Firebase Project and put it in `wd`
<img src="https://github.com/jhirsh/firebase_upload/blob/master/images/firebase_download_key.png" alt="Firebase .json certificate"  display=block margin-left=atuo margin-right=auto width=75%>

## Notes on Firebase uploading
* `db.collection('<collection id>').document('<document id>').set(data)`
* `data` must be a python dict. Fill it exactly how you'd like your document to be structured.

## Running upload script
`python3 upload_file.py [filename]` <br />
`[filename]` doesn't need extension, and will automatically add `.txt`

## Further iterations
* While this method works well for uploading a single file, if you have collected a lot of data, it might make more sense to be able to upload multiple files at once. Could implement it with bash scripting or in the python script itself.
* Dynamically create the `data` dictionary to properly type all variables instead of changing it on case-by-case basis for script.


