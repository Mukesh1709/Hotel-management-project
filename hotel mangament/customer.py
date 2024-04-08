from tkinter import*
from PIL import Image
from PIL import ImageTk  #pip install pillow
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox





class Cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

     #======================================Variable=================================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()

       


      




        #=======================title==============================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #=====================logo======================================
        self.img2 = Image.open(r"logo.jpg")
        self.img2 = self.img2.resize((100, 40))
        self.photoimg2 =ImageTk.PhotoImage(self.img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #=======================labelFrame============================
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Deatils",font=("times new roman",18,"bold"),padx=2,)
        LabelFrameleft.place(x=5,y=50,width=425,height=490)

        #============================labels and entrys======================
        #custRef
        lbl_cust_ref=Label(LabelFrameleft,text="Customer Ref:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        enty_ref=Entry(LabelFrameleft,textvariable=self.var_ref,width=29,font=("times new romen",13,"bold"))
        enty_ref.grid(row=0,column=1)
        

         # cust name
        cname=Label(LabelFrameleft,font=("arial",12,"bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        Textmname=Entry(LabelFrameleft,textvariable=self.var_cust_name,font=("arial",13,"bold"),width=29,state="readonly")
        enty_ref.grid(row=1,column=1)

         #mother name
        lblmname=Label(LabelFrameleft,font=("arial",12,"bold"),text="Mother Name:",padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=Entry(LabelFrameleft,textvariable=self.var_mother,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=2,column=1)

        # gender combobox
        Label_gender = Label(LabelFrameleft, font=("arial", 12, "bold"), text="Gender:", padx=2, pady=6)
        Label_gender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(LabelFrameleft,textvariable=self.var_gender, font=("arial" ,12, "bold"),width=27,state="readonly")  # Corrected 'width' parameter
        combo_gender["values"] = ("Male", "Female", "Other")  # Corrected 'values' parameter
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1) 
       

        #postcode
        lblpostcode=Label(LabelFrameleft,font=("arial",12,"bold"),text="Post Code:",padx=2,pady=6)
        lblpostcode.grid(row=4,column=0,sticky=W)
        lblpostcode=Entry(LabelFrameleft,textvariable=self.var_post,font=("arial",13,"bold"),width=29)
        lblpostcode.grid(row=4,column=1)

        #===================Email====================================
        lblEmail=Label(LabelFrameleft,font=("arial",12,"bold"),text="Email:",padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        lblEmail=Entry(LabelFrameleft,textvariable=self.var_email,font=("arial",13,"bold"),width=29)
        lblEmail.grid(row=6,column=1)

        #Mobilenumber
        lblMobile=Label(LabelFrameleft,font=("arial",12,"bold"),text="Mobile:",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        lblMobile=Entry(LabelFrameleft,textvariable=self.var_mobile,font=("arial",13,"bold"),width=29)
        lblMobile.grid(row=5,column=1)

        #nationality
        lblNationality=Label(LabelFrameleft,font=("arial",12,"bold"),text="Nationality:",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality = ttk.Combobox(LabelFrameleft,textvariable=self.var_nationality, font=("arial" ,12, "bold"),width=27,state="readonly")  # Corrected 'width' parameter
        combo_Nationality["values"] = ("Indian", "American", "Britist")  # Corrected 'values' parameter
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1)
        

        #Idproof type combobox
        lblIdproof=Label(LabelFrameleft,font=("arial",12,"bold"),text="Id Proof Type:",padx=2,pady=6)
        lblIdproof.grid(row=8,column=0,sticky=W)

        combo_id = ttk.Combobox(LabelFrameleft,textvariable=self.var_id_proof , font=("arial" ,12, "bold"),width=27,state="readonly")  # Corrected 'width' parameter
        combo_id["values"] = ("AdharCard", "DrivingLicence", "Passport")  # Corrected 'values' parameter
        combo_id.current(0)
        combo_id.grid(row=8, column=1)
        

        #id number
        lblIdNumber=Label(LabelFrameleft,font=("arial",12,"bold"),text="Id Number:",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        lblIdNumber=Entry(LabelFrameleft,textvariable=self.var_id_number,font=("arial",13,"bold"),width=29)
        lblIdNumber.grid(row=9,column=1)

        # address
        lblAddress=Label(LabelFrameleft,font=("arial",12,"bold"),text="Address:",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=Entry(LabelFrameleft,textvariable=self.var_address,font=("arial",13,"bold"),width=29)
        txtAddress.grid(row=10,column=1)

        # ===================================btns========================================
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

       #============================table Frame==========================================
        
        Table_Frame=Frameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Deatils And Search System",font=("times new roman",18,"bold"),padx=2,)
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        combo_Search = ttk.Combobox(Table_Frame, font=("arial" ,12, "bold"),width=24,state="readonly")  
        combo_Search["values"] = ("Mobile", "Ref")  
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
        details_table.place(x=0,y=50,width=860,height=350)

        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile",
                                                                     "email","nationality","idproof","idnumber","address"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.Cust_Details_Table.xview)
        Scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")



        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)
        

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",
                                     self.get_cuersor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are requaired",parent=self.root)
        else:
            try:
               conn=mysql.connector.connect(host="localhost",user="root",password="root",database="trile1")
               my_cyrsor=conn.cursor()
               my_cyrsor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_ref.get(),
                                                                            self.var_cust_name.get(),
                                                                            self.var_mother.get(),
                                                                            self.var_gender.get(),
                                                                            self.var_post.get(),
                                                                            self.var_mobile.get(),
                                                                            self.var_email.get(),
                                                                            self.var_nationality.get(),
                                                                            self.var_id_proof.get(),
                                                                            self.var_id_number.get(),
                                                                            self.var_address.get(),   
                                                                         ))
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("waring",f"Some went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="trile1")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
               self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
               for i in rows:
                 self.Cust_Details_Table.insert("",END,values=i)
               conn.commit()
        conn.close()

    def get_cuersor(self,event=""):
        cusrsor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cusrsor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10]),

    def update(self):
        if self.var_mobile.get() == "":
           messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
           conn = mysql.connector.connect(host="localhost", user="root", password="root", database="trile1")
           my_cursor = conn.cursor()
           my_cursor.execute("UPDATE customer SET customer_name=%s, mother_name=%s, gender=%s, post_code=%s, email=%s, nationality=%s, id_proof=%s, id_number=%s, address=%s, customer_ref=%s "
                          "WHERE mobile=%s",
                                                                                                                                                                                       (self.var_cust_name.get(),
                                                                                                                                                                                        self.var_mother.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_post.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_nationality.get(),
                                                                                                                                                                                        self.var_id_proof.get(),
                                                                                                                                                                                        self.var_id_number.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_ref.get(),
                                                                                                                                                                                        self.var_mobile.get()
                                                                                                                                                                                    ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update", "Customer details have been updated successfully", parent=self.root)

        

            
            




        


if __name__ =="__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()

