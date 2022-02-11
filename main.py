from tkinter import *
from tkinter import ttk
#from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime
'''import Delete
import MainFrame
import SearchMe
import Update
import Payment
from MainFrame import *
from Delete import *
from Update import *
from SearchMe import *
from Payment import *'''

import pymysql

class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.title("DeadStock Management System")
        self.root.geometry("1500x800+0+0")



        # Input Frame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=0, y=100, width=1500, height=700)
        frame2 = Frame(self.root, bg="sky blue")
        frame2.place(x=0, y=0, width=1500, height=100)
        title = Label(frame2, text="WELCOME ADMIN", font=("Sans-serif", 26, "bold"), bg="sky blue",
                      fg="White").place(x=50, y=30)

        home = Button(frame2, text="HOME", font=("Times new roman", 12, "bold"), bg="#0096FF", fg="white", height=3,
                      width=13, border=0, cursor="hand2").place(x=795, y=0)

        users = Button(frame2, text="USERS", font=("Times new roman", 12, "bold"), bg="#0096FF", fg="white", height=3,
                     width=13, border=0, cursor="hand2").place(x=920, y=0)

        vendors = Button(frame2, text="VENDORS", font=("Times new roman", 12, "bold"), bg="#0096FF", fg="white", height=3,
                        width=13, border=0, cursor="hand2").place(x=1045, y=0)
        item = Button(frame2, text="ITEMS", font=("Times new roman", 12, "bold"), bg="#0096FF", fg="white", height=3,
                        width=13, border=0, cursor="hand2").place(x=1170, y=0)
        view = Button(frame2, text="VIEW", font=("Times new roman", 12, "bold"), bg="#0096FF", fg="white", height=3,
                        width=13, border=0, cursor="hand2").place(x=1295, y=0)

        logout = Button(frame2, text="EXIT", font=("Times new roman", 12, "bold"), bg="#0096FF", fg="white", height=3,
                        width=13, border=0, cursor="hand2").place(x=1420, y=0)

        frame3 = Frame(frame1, bg="black")
        frame3.place(x=0, y=0, width=350, height=500)

        frame4 = Frame(frame1, bg="red")
        frame4.place(x=350, y=0, width=10, height=500)



#def callAdd(self):
root = Tk()
obj = MainPage(root)
root.mainloop()


