from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from my_bookings import My_bookings

class Reports(My_bookings):

    def __init__(self,root,frame,customer_id,username,password,name):
        super().__init__(root,frame,customer_id)
        self.username = username
        self.password = password
        self.name = name
        self.user = "Admin"
    
    def make_header(self):
        frame2 = Frame(self.frame,padx=10,pady=0,bg="#3A5FCD")
        frame2.grid(row=0,column=0,padx=10,pady=0)
        ############# button commands ##################
        def search():
            if (len(txt1.get()) > 0):
                customer_id = txt1.get()
                connection = sqlite3.connect('hotelmanagement.db')
                cursor = connection.cursor()
                cursor.execute(f'select First_Name from customers where Customer_ID="{customer_id}"')
                cdetails = cursor.fetchall()
                if (len(cdetails) > 0):
                    try:
                        cursor.execute(f'select Booking_No,Check_In,Check_Out,NOA,NOC_1,NOC_2,NOC_3,Mealplan,Room_ID,Total_Price,Discount,Advance,\
                            Balance from checkout where Customer_ID="{customer_id}"')
                        bookings = cursor.fetchall()
                        self.insert_data(bookings)
                        button5.configure(state=NORMAL)
                    except:
                        messagebox.showerror("Admin tasks","There are no reports for this customer")
                else:
                    messagebox.showerror("Admin tasks","Please enter valid Customer ID")
            else:
                messagebox.showerror("Admin tasks","Please enter Customer ID")
        def Print():
            self.print_report()
        def delete():
            self.delete_details()
            button4.configure(state=DISABLED)
        def clear():
            txt1.delete(0,END)
            self.clear_rows()
            button5.configure(state=DISABLED)
        ################################################
        global button2;global button4
        label1 = Label(frame2, text="Customer Reports", font=("Cooper Black", 22), padx=30, pady=5, bg="#3A5FCD", bd=0)
        label1.grid(row=0, column=0, pady=0, padx=3, columnspan=2)

        frame3 = Frame(frame2,padx=10,pady=10,bg="darkturquoise")
        frame3.grid(row=1,column=0)

        label2 = Label(frame3,text="Customer ID",font=("Times New Roman",13),padx=15,pady=5,bg="darkturquoise",highlightthickness=2)
        label2.grid(row=0,column=0,pady=5,padx=5)
        label2.config(highlightbackground="#00868B",highlightcolor="#00868B")

        txt1 = Entry(frame3, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt1.grid(row=0, column=1, padx=5)

        button1 = Button(frame3, text="Search", padx=10, pady=1,
                        font=("Berlin Sans FB Demi", 13), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=search)
        button1.grid(row=0, column=2)

        button2 = Button(frame3, text="Print", padx=15, pady=1,
                        font=("Berlin Sans FB Demi", 13), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=Print,state=DISABLED)
        button2.grid(row=0, column=3,padx=5)

        button4 = Button(frame3, text="Delete", padx=10, pady=1,
                        font=("Berlin Sans FB Demi", 13), bg="#87CEFA",
                        relief=RAISED, activebackground="crimson", bd=3,command=delete,state=DISABLED)
        button4.grid(row=0, column=4,padx=5)

        button5 = Button(frame3, text="Clear", padx=10, pady=1,
                        font=("Berlin Sans FB Demi", 13), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=clear,state=DISABLED)
        button5.grid(row=0, column=5,padx=5)
    
    def active_buttons(self):
        button2.configure(state=NORMAL)
        button4.configure(state=NORMAL)

