import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def authorize(creds_json):
    """ Uses gspread and oauth2client.service_account to authenticate google
    docs access using the credentials specified by creds.
    Returns the gspread client class instance.

    Refs: https://gspread.readthedocs.io/en/latest/index.html"""
    
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]

    secret_file = os.path.join(os.getcwd(), creds_json)
    
    creds = ServiceAccountCredentials.from_json_keyfile_name(secret_file, scope)
    
    return gspread.authorize(creds)
