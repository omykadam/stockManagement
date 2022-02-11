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

#import pymysql

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
                      width=13, border=0, cursor="hand2").place(x=775, y=0)

        users = Button(frame2, text="USERS", font=("Times new roman", 12, "bold"), bg="#0096FF", fg="white", height=3,
                     width=13, border=0, cursor="hand2").place(x=895, y=0)

        vendors = Button(frame2, text="VENDORS", font=("Times new roman", 12, "bold"), bg="#0096FF", fg="white", height=3,
                        width=13, border=0, cursor="hand2").place(x=1015, y=0)
        item = Button(frame2, text="ITEMS", font=("Times new roman", 12, "bold"), bg="#0096FF", fg="white", height=3,
                        width=13, border=0, cursor="hand2").place(x=1135, y=0)
        search = Button(frame2, text="SEARCH", font=("Times new roman", 12, "bold"), bg="#0096FF", fg="white", height=3,
                        width=13, border=0, cursor="hand2").place(x=1255, y=0)

        logout = Button(frame2, text="EXIT", font=("Times new roman", 12, "bold"), bg="#0096FF", fg="white", height=3,
                        width=13, border=0, cursor="hand2").place(x=1375, y=0)

        self.frame3 = Frame(frame1, bg="white")
        self.frame3.place(x=0, y=0, width=350, height=700)

        self.frame4 = Frame(frame1, bg="cyan")
        self.frame4.place(x=350, y=0, width=1150, height=700)

        #in frame 4

        self.user_reg = Label(self.frame4 , text="User Registration",bg="cyan" ,font=('Helvetica 15 bold'), ).place(x=430, y=100)

        self.User_id = Label(self.frame4, text="User Id :", font=('Times new roman', 14,),bg="cyan", justify='left').place(x=300,
                                                                                                                 y=190)
        self.user_label_entry = Entry(self.frame4, font=('boldface', 14,)).place(x=600, y=190)

        self.User_name = Label(self.frame4, text="User Name :", font=('Times new roman', 14,),bg="cyan", justify='left').place(
            x=300, y=240)
        self.user_name_entry = Entry(self.frame4, font=('boldface', 14,)).place(x=600, y=240)

        self.User_id = Label(self.frame4, text="Designation :", font=('Times new roman', 14,),bg="cyan", justify='left').place(
            x=300, y=360)
        self.user_label_entry = Entry(self.frame4, font=('boldface', 14,)).place(x=600, y=300)

        self.User_id = Label(self.frame4, text="Department :", font=('Times new roman', 14,),bg="cyan", justify='left').place(
            x=300, y=300)
        self.user_label_entry = Entry(self.frame4, font=('boldface', 14,)).place(x=600, y=360)

        self.User_id = Label(self.frame4, text="User Id :", font=('Times new roman', 14,),bg="cyan", justify='left').place(x=300,
                                                                                                                 y=420)
        self.user_label_entry = Entry(self.frame4, font=('boldface', 14,)).place(x=600, y=420)

        self.User_id = Label(self.frame4, text="Password :", font=('Times new roman', 14,),bg="cyan", justify='left').place(x=300,
                                                                                                                  y=480)
        self.user_label_entry = Entry(self.frame4, font=('boldface', 14,)).place(x=600, y=480)

        self.User_id = Label(self.frame4, text="Confirm Password :", font=('Times new roman', 14,),bg="cyan",
                             justify='left').place(x=300, y=540)
        self.user_label_entry = Entry(self.frame4, font=('boldface', 14,)).place(x=600, y=540)

        self.clear_btn = Button(self.frame4, text="Clear", font=('boldface', 14)).place(x=450, y=600)
        self.submit_btn = Button(self.frame4, text="Submit", font=('boldface', 14)).place(x=550, y=600)

        # IN frame 3






#def callAdd(self):
root = Tk()
obj = MainPage(root)
root.mainloop()