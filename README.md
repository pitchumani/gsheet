# What is gsheet
Python scripts to read and write google sheets using gspread (Python API for Google Sheets). Required python libraries are: gspread, oauth2client. Install them before using these scripts.

## How to setup google docs for authorization
Use [Google API Console](https://console.developers.google.com/) to create a service account credential. Refer [google guides](https://developers.google.com/sheets/api/guides/authorizing). Download the credentials json file and pass that to authorze functon.

To enable read/ write access to any google document, share that document with your service account created.

## Modules
* utils
* mf

# utils
## authorize(credentials.json)
This function shall be used to authorize the google docs access using the service account credentials json file (parameter). It returns the gspread client class instance.
Refer [gspread APIs](https://gspread.readthedocs.io/en/latest/index.html).

# Examples
* list-worksheets.py (usage: *python3 credentials.json sheetname*)
* read-mf-transactions.py (usage: *python3 credentials.json sheetname*)

This script uses authorize function from utils.py. Dependent libraries: gspread, oauth2client.
Set PYTHONPATH before executing this script

# License
MIT
