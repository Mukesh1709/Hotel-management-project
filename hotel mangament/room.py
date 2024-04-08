from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #============================varible===============================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomvailble=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        

        



        # Title
        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        self.img2 = Image.open(r"logo.jpg")
        self.img2 = self.img2.resize((100, 40))
        self.photoimg2 = ImageTk.PhotoImage(self.img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        # LabelFrame
        LabelFrameleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking  Details", font=("times new roman", 18, "bold"), padx=2)
        LabelFrameleft.place(x=5, y=50, width=425, height=490)

        # Customer Contact
        lbl_cust_contact = tk.Label(LabelFrameleft, text="Customer Contact:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky="w")
        self.var_contact = tk.StringVar()
        enty_contact = tk.Entry(LabelFrameleft, textvariable=self.var_contact, font=("arial", 13, "bold"), width=20)
        enty_contact.grid(row=0, column=1, sticky="w")

         # Create Fetch Data button
        btnFetchData = tk.Button(LabelFrameleft, command=self.Fetch_contact, text="Fetch Data", font=("arial", 8, "bold"), bg="black", fg="gold", width=10)
        btnFetchData.place(x=347,y=4)
        
        # Check in Date
        Label_check_date = Label(LabelFrameleft, text="Check in Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        Label_check_date.grid(row=1, column=0, sticky=W)
        textcheck_in_date = Entry(LabelFrameleft,textvariable=self.var_checkin ,font=("arial", 13, "bold"), width=29)
        textcheck_in_date.grid(row=1, column=1)

        # Check out Date
        Label_check_out = Label(LabelFrameleft, text="Check_out Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        Label_check_out.grid(row=2, column=0, sticky=W)
        textcheck_in_out = Entry(LabelFrameleft,textvariable=self.var_checkout, font=("arial", 13, "bold"), width=29)
        textcheck_in_out.grid(row=2, column=1)

        # Room Type
        Label_RoomType = Label(LabelFrameleft, text="Room Type:", font=("arial", 12, "bold"), padx=2, pady=6)
        Label_RoomType.grid(row=3, column=0, sticky=W)

        combo_RoomType = ttk.Combobox(LabelFrameleft,textvariable=self.var_roomtype, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_RoomType['values'] = ("Single", "Double", "Luxury")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Avilabel Room
        lblRoomAvailable = ttk.Label(LabelFrameleft, font=("arial", 12, "bold"), text="Available Room: ")
        lblRoomAvailable.grid(row=4, column=0, sticky="w", padx=2, pady=6)
        txtRoomAvailable = ttk.Entry(LabelFrameleft,textvariable=self.var_roomvailble, font=("arial", 13, "bold"), width=29)
        txtRoomAvailable.grid(row=4, column=1)

        # Meal
        lblMeal = ttk.Label(LabelFrameleft, font=("arial", 12, "bold"), text="Meal: ")
        lblMeal.grid(row=5, column=0, sticky="w", padx=2, pady=6)
        txtMeal = ttk.Entry(LabelFrameleft,textvariable=self.var_meal, font=("arial", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1)

        # No Of Days
        lblNoOfDays = ttk.Label(LabelFrameleft, font=("arial", 12, "bold"), text="No Of Days: ")
        lblNoOfDays.grid(row=6, column=0, sticky="w", padx=2, pady=6)
        txtNoOfDays = ttk.Entry(LabelFrameleft,textvariable=self.var_noofdays, font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=6, column=1)

        # Paid Tax
        lblPaidTax = ttk.Label(LabelFrameleft, font=("arial", 12, "bold"), text="Paid Tax: ")
        lblPaidTax.grid(row=7, column=0, sticky="w", padx=2, pady=6)
        txtPaidTax = ttk.Entry(LabelFrameleft,textvariable=self.var_paidtax, font=("arial", 13, "bold"), width=29)
        txtPaidTax.grid(row=7, column=1)

        # Sub Total
        lblSubTotal = ttk.Label(LabelFrameleft, font=("arial", 12, "bold"), text="Sub Total: ")
        lblSubTotal.grid(row=8, column=0, sticky="w", padx=2, pady=6)
        txtSubTotal = ttk.Entry(LabelFrameleft,textvariable=self.var_actualtotal, font=("arial", 13, "bold"), width=29)
        txtSubTotal.grid(row=8, column=1)

        # Total Cost  
        lblTotalCost = ttk.Label(LabelFrameleft, font=("arial", 12, "bold"), text="Total Cost: ")
        lblTotalCost.grid(row=9, column=0, sticky="w", padx=2, pady=6)
        txtTotalCost = ttk.Entry(LabelFrameleft,textvariable=self.var_total, font=("arial", 13, "bold"), width=29)
        txtTotalCost.grid(row=9, column=1)

        #===============Bill Button==================================================
        btnBill=Button(LabelFrameleft,text="Bill",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

        # ===================================btns========================================
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        #===========================Rightside image===================================
        self.img3 = Image.open(r"bed.jpg")
        self.img3 = self.img3.resize((500, 300))
        self.photoimg3 = ImageTk.PhotoImage(self.img3)
        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=55, width=500, height=300)


        #============================table Frame search system==========================================
        
        Table_Frame=Frameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Deatils And Search System",font=("times new roman",18,"bold"),padx=2,)
        Table_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        combo_Search = ttk.Combobox(Table_Frame, font=("arial" ,12, "bold"),width=24,state="readonly")  
        combo_Search["values"] = ("Contact", "Room")  
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1,padx=2)

        txtSearch=Entry(Table_Frame,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSerach=Button(Table_Frame,text="Search",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSerach.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

         # ==============================show data Table=====================================
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_Table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomvailable",
                                                                     "meal","noofdays"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.room_Table.xview)
        Scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("contact",text="contact")
        self.room_Table.heading("checkin",text="Check-in")
        self.room_Table.heading("checkout",text="Check-out")
        self.room_Table.heading("roomtype",text="Room Type")
        self.room_Table.heading("roomvailable",text="Room No")
        self.room_Table.heading("meal",text="Meal")
        self.room_Table.heading("noofdays",text="NoOfDay")

        self.room_Table["show"]="headings"

        self.room_Table.column("contact",width=100)
        self.room_Table.column("checkin",width=100)
        self.room_Table.column("checkout",width=100)
        self.room_Table.column("roomtype",width=100)
        self.room_Table.column("roomvailable",width=100)
        self.room_Table.column("meal",width=100)
        self.room_Table.column("noofdays",width=100)
        

        self.room_Table.pack(fill=BOTH,expand=1)

#=================================All Data Fetch========================================================
    def Fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter contact Number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="trile1")
            my_cursor = conn.cursor()
            query = ("SELECT customer_name FROM customer WHERE mobile = %s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "This number  not Found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=450, y=55, width=300, height=180)

                label_name = Label(root, text="customer_name:", font=("Arial", 12, "bold"))
                label_name.place(x=0, y=0)
                
                # Create a label to display the customer name
                label_customer = Label(root, text=row, font=("Arial", 12, "bold"))
                label_customer.place(x=90, y=0)

                #==============================Gender===============================================
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="trile1")
                my_cursor = conn.cursor()
                query = ("SELECT gender FROM customer WHERE mobile = %s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                Labelgender=Label(showDataframe,Text="gender",font=("arial",12,"bold"))
                Labelgender.place(x=0,y=30)

                Label2=Label(showDataframe,Text=row,font=("arial",12,"bold"))
                Label2.place(x=90,y=30)

                #=================================email====================================
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="trile1")
                my_cursor = conn.cursor()
                query = ("SELECT email FROM  customer WHERE mobile = %s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                Labelemail=Label(showDataframe,Text="email",font=("arial",12,"bold"))
                Labelemail.place(x=0,y=60)

                Label3=Label(showDataframe,Text=row,font=("arial",12,"bold"))
                Label3.place(x=90,y=60)

                #======================================Nationality==========================================
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="trile1")
                my_cursor = conn.cursor()
                query = ("select nationality from customer whare mobile = %s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                Labelnationality=Label(showDataframe,Text="nationality",font=("arial",12,"bold"))
                Labelnationality.place(x=0,y=90)

                Label4=Label(showDataframe,Text=row,font=("arial",12,"bold"))
                Label4.place(x=90,y=90)

                #=============================Address=================================
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="trile1")
                my_cursor = conn.cursor()
                query = ("SELECT address FROM customer WHERE mobile = %s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                Labeladdress=Label(showDataframe,text="address:",font=("arial",12,"bold"))
                Labeladdress.place(x=0,y=90)

                Label4=Label(showDataframe,Text=row,font=("arial",12,"bold"))
                Label4.place(x=90,y=90)







if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
