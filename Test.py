
# Kel Lee
import tkinter
import tkinter as tk
from tkinter import simpledialog
import re
import ctypes



ROOT = tk.Tk()
ROOT.withdraw()
i=0
while i < 4:

    if i == 3:
        exec(open('main.py').read())
        break


    USER_INP = simpledialog.askstring(title="Input Key",
                                  prompt="Enter Key")

    i = i + 1
    text_file = open("Key.txt", "r")

    # read whole file to a string
    data = text_file.read()

    # close file
    text_file.close()

    matched = re.match(USER_INP, data)

    is_match = bool(matched)

    if bool(matched):
        break






if bool(matched) :
 ctypes.windll.user32.MessageBoxW(0, "Succesful Login", "Authorization", 1)
else:
    ctypes.windll.user32.MessageBoxW(0, "Failed Login Exceeded Login Attempts. Request New Key from System Administer ", "Authorization", 1)




