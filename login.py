# import libraries
import tkinter as tk
from tkinter import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope of the API access and credentials for authentication
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'service_account.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('snakegame_creds').sheet1