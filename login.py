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
        # Set the login screen background image
        self.login_img = PhotoImage(file='./login_screen.png')
        self.label_login = Label(self.master, image=self.login_img)
        self.label_login.place(x=0, y=0)
         # Create the GUI widgets
        self.username_entry = tk.Entry(self.master, borderwidth=0, highlightthickness=0)
        self.username_entry.pack()
        self.password_entry = tk.Entry(self.master, borderwidth=0, highlightthickness=0, show="*")
        self.password_entry.pack()
        self.login_btn = tk.Button(self.master,
                                       text="Log-in",
                                       font='Arial 12',
                                       bg='#0099FF',
                                       fg='white',
                                       borderwidth=0,
                                       highlightthickness=0,
                                       )
        self.login_btn.pack()
        self.signin_btn = tk.Button(self.master,
                                       text="Sign-in",
                                       font='Arial 12',
                                       bg='#ECFFDD',
                                       borderwidth=0,
                                       highlightthickness=0,
                                       )
        self.signin_btn.pack()
        self.login_label = Label(master, text="", background='#A4C58C', justify='center')
        self.signin_label = Label(master, text="", background='#A4C58C', justify='center')

        # Position the widgets on the window
        self.username_entry.place(width=220, height=20, x=130, y=198)
        self.password_entry.place(width=220, height=20, x=130, y=270)
        # Log-in and Sign-in button position 
        self.login_btn.place(width=120, height=42, x=118, y=314)
        self.signin_btn.place(width=120, height=42, x=247, y=314)
        self.login_label.place(width=220, height=20, x=137, y=374)
        self.signin_label.place(width=220, height=20, x=137, y=406)

        self.login_success = False

if __name__ == "__main__":
    root = tk.Tk()
    login_window = Login(root)
    login_window.mainloop()