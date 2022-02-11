import tkinter as tk
from tkinter import ttk
from tkinter import *



class ItemEntry:
    def __init__(self, root):
        self.root = root
        self.root.title("Purchase Entry")
        self.root.geometry("1350x700")

        #item_id=[]

        # Purchase Entry Details

        p_entry = Label(self.root, text="Item Purchase Entry:", font=("times new roman", 15, "bold"), bg="white",
                         fg="black").place(x=60, y=30)

        # Item ID number

        item_id = Label(self.root, text="ITEM ID :", font=("times new roman", 13), bg="white",
                        fg="black").place(x=60, y=80)
        self.txt_itemId = Entry(self.root, font=("Times new roman", 13), bg="white")
        self.txt_itemId.place(x=310, y=80, width=280)

        # Item Type

        item_type = Label(self.root, text="ITEM TYPE :", font=("times new roman", 13), bg="white", fg="black").place(
            x=60, y=120)
        self.txt_itemType = Entry(self.root, font=("Times new roman", 15), bg="white")
        self.txt_itemType.place(x=310, y=120, width=280)

        # Item Purchase Year

        item_pyear = Label(self.root, text="PURCHASE YEAR :", font=("times new roman", 13), bg="white", fg="black").place(
            x=60, y=160)
        self.txt_itemPYear = Entry(self.root, font=("Times new roman", 13), bg="white")
        self.txt_itemPYear.place(x=310, y=160, width=80)

        # Purchase authority
        authority = Label(self.root, text="PURCHASE AUTHORITY :", font=("times new roman", 13), bg="white", fg="black").place(
            x=60, y=200)
        self.txt_authority = Entry(self.root, font=("Times new roman", 13), bg="white")
        self.txt_authority.place(x=310, y=160, width=80)

        # Quantity

        item_qty = Label(self.root, text="QUANTITY :", font=("times new roman", 13), bg="white", fg="black").place(
            x=60, y=240)
        self.txt_qty = Entry(self.root, font=("Times new roman", 13), bg="white")
        self.txt_qty.place(x=310, y=240, width=80)

        # Rate per Item

        rate_pit = Label(self.root, text="RATE PER ITEM(IN RUPEES) :", font=("times new roman", 13), bg="white", fg="black").place(
            x=60, y=280)
        self.txt_ratePIt = Entry(self.root, font=("Times new roman", 13), bg="white")
        self.txt_ratePIt.place(x=310, y=280, width=80)

        # Total Amount
        total_amt = Label(self.root, text="TOTAL AMOUNT(IN RUPEES) :", font=("times new roman", 13), bg="white", fg="black").place(
            x=60, y=320)
        self.txt_totalAmt = Entry(self.root, font=("Times new roman", 13), bg="white")
        self.txt_totalAmt.place(x=310, y=320, width=280)

        # Name of Department Head
        name_ofDHead = Label(self.root, text="NAME OF DEPARTMENT HEAD :", font=("times new roman", 13), bg="white", fg="black").place(
            x=750, y=80)
        deptHead = ["SELECT", "ABC", "XYZ", "PQR", "LMN"]
        self.cmb_duration = ttk.Combobox(self.root, value=deptHead, width=15, height=15, state="readonly")
        self.cmb_duration.place(x=310, y=370)
        self.cmb_duration.current(0)

        # Depriciation percentile(%)
        depri_Per = Label(self.root, text="DEPRICIATION PERCENTILE(%) :", font=("times new roman", 13), bg="white",
                          fg="black", justify='left').place(x=60, y=360)
        self.txt_depriPerc = Entry(self.root, font=("Times new roman", 13), bg="white")
        self.txt_depriPerc.place(x=310, y=370, width=280)

        # Voucher PDF Upload
        voucher = Label(self.root, text="UPLOAD VOUCHER\n(JPEG,JPG,PDF) :", font=("times new roman", 13), bg="white", fg="black").place(x=60, y=410)
        self.txt_voucher = Entry(self.root, font=("Times new roman", 13), bg="white")
        self.txt_voucher.place(x=310, y=410, width=280)

        # Amount & date
        amt_date = Label(self.root, text="AMOUNT AND DATE :", font=("times new roman", 13), bg="white", fg="black").place(x=60, y=450)
        self.txt_amtDate = Entry(self.root, font=("Times new roman", 13), bg="white")
        self.txt_amtDate.place(x=310, y=450, width=280, height=50)

        # Depriciation amount
        depri_amt = Label(self.root, text="DEPRICIATION AMOUNT(IN RUPEES) :", font=("times new roman", 13), bg="white",
                             fg="black").place(x=750, y=30)
        self.txt_depriAmt = Entry(self.root, font=("Times new roman", 13), bg="white")
        self.txt_depriAmt.place(x=310, y=450, width=280, height=50)


        # SUBMIT BUTTON
        self.subm = Button(root, text="SUBMIT", bd='5')#, command=self.setData)
        self.subm.place(x=590, y=620, width=100)

        # RESET BUTTON
        self.rest = Button(root, text="RESET", bd='5')#, command=self.clear)
        self.rest.place(x=740, y=620, width=100)




root = Tk()
obj = ItemEntry(root)
root.mainloop()