# import libraries
import tkinter as tk
from tkinter import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope of the API access and credentials for authentication
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'credssnakegame.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('snakegame_creds').sheet1

# Setting Login interface with Tkinter
class Login(tk.Frame):
    def __init__(self, master):
        """
        Constructor for Login class, initializes and configures the login window

        Args:
            master: A Tkinter object, which is the parent window
        """
        # Create the main window
        super().__init__(master)
        self.master = master
        self.master.title("SnakeGame Login")
        self.master.geometry("500x500+511+150")
        self.master.wm_resizable(width=False, height=False)
        self.master.iconbitmap(default='snake.ico')

    