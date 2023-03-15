# import libraries
import tkinter as tk
from tkinter import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

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

    def register(self):
        """
        Register a new user by adding their login credentials to the Google Sheet.

        If either the username or password field is empty, a message is displayed to the user.
        """

        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            # Verify if both fields were filled
            self.signin_label.config(fg="red", text="Please fill in both fields.")
            return

        # Add the new user's credentials to the Google Sheet
        row = [username, password,]
        index = 2  # Index of the row to add the login information to
        wks.insert_row(row, index)
        

        # Display a message to the user indicating that registration was successful
        self.signin_label.config(fg="green", text="You are registered!")

    def check_login(self):
        """
        Authenticate the user's login credentials.

        If the user's username and password match those stored in the Google Sheet, display a
        message indicating successful login. Otherwise, display a message indicating that the
        username or password is incorrect.
        """
        username = self.username_entry.get()
        password = self.password_entry.get()

        row_index = None
        
        # Obtain information form googlesheets
        login_info = wks.get_all_values()
        # Check information to validate login
        for index, row in enumerate(login_info):
            if username == row[0] and password == row[1]:
                row_index = index + 1
                # Update the last login column for the user
                wks.update_cell(row_index, 5, str(datetime.now()))
                # Move the user login to the top of the worksheet once it logged in
                login_row = wks.row_values(row_index)
                wks.delete_row(row_index)
                wks.insert_row(login_row, 2)
                # Display a message indicating successful login
                self.login_label.config(text="Login Successful!", fg="green")
                self.login_label.update()
                # If Login successful, close the login screen and start the game
                self.master.after(500, self.master.destroy)
        else:
            # If Login goes wrong, display an error mesage
            self.login_label.config(fg="red",
                                        text="Sorry! Username or password isn't right.")

if __name__ == "__main__":
    root = tk.Tk()
    login_window = Login(root)
    login_window.mainloop()