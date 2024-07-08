from itertools import count
from multiprocessing import connection
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import admin_login

class My_bookings():
    
    def __init__(self,root,frame,customer_id):
        self.root = root
        self.frame = frame
        self.customer_id = customer_id
        self.user = "Customer"
    
    def check_bookings(self):
        if (self.user == "Customer"):
            connection = sqlite3.connect('hotelmanagement.db')
            cursor = connection.cursor()
            cursor.execute(f'select Booking_No from bookings where Customer_ID="{self.customer_id}"')
            bookings = cursor.fetchall()
            connection.close()
            if (len(bookings) == 0):
                self.root.destroy()
                messagebox.showerror("Customer tasks","No Bookings to show")
            else:
                self.get_bookings()
        else:
           self.get_bookings() 
    
    def get_bookings(self):
        connection = sqlite3.connect('hotelmanagement.db')
        cursor = connection.cursor()
        if (self.user == "Customer"):
            cursor.execute(f'select Booking_No,Booking_date,Check_In,Check_Out,NOA,NOC_1,NOC_2,NOC_3,Mealplan,Room_ID,Total_Price,Discount,Advance,\
            Balance from bookings where Customer_ID="{self.customer_id}"')
            bookings = cursor.fetchall()
        else:
            bookings = []
        
        connection.close()
        self.show_bookings(bookings)
    
    def show_bookings(self,bookings):
        self.root.title("Royal Hotel")
        self.root.iconbitmap("hotel.ico")

        if (self.user == "Customer"):
            x = int((1520-1020)/2)
            y = int((810-460)/2)
            self.root.geometry(f'1020x460+{x}+{y}')
            self.root.minsize(1020,460)
            self.root.maxsize(1020,460)
        else:
            x = int((1520-940)/2)
            y = int((810-540)/2)
            self.root.geometry(f'940x540+{x}+{y}')
            self.root.minsize(940,540)
            self.root.maxsize(940,540)

        self.root.configure(bg="#3A5FCD")
        self.frame.configure(bg="#3A5FCD")
        self.make_header()
        frame1 = Frame(self.frame,padx=10,pady=10,bg="darkturquoise")
        frame1.grid(row=1,column=0,padx=10,pady=10)
        ##################################
        def close():
            if (self.user == "Customer"):
                self.root.destroy()
            else:
                response = messagebox.askyesno("Admin tasks","Do you want to close Reports?")
                if (response==True):
                    for w in self.frame.winfo_children():
                        w.destroy()
                    alogin = admin_login.Admin_login(self.root,self.frame,self.username,self.password,self.name)
                    alogin.login()
        ##################################
        #adding style
        my_style = ttk.Style()
        my_style.theme_use("default")
        my_style.configure("Treeview",background="silver",foreground="black",rowheight=30,fieldbackground="silver")
        my_style.map("Treeview",background=[("selected","blue")])
        # add a scrollbutton
        my_scroll = Scrollbar(frame1)
        my_scroll.grid(row=0,column=1,sticky=NS)
        #creating treeview
        global my_tree
        my_tree = ttk.Treeview(frame1,yscrollcommand=my_scroll.set)
        my_tree.grid(row=0,column=0)
        #configure tags
        my_tree.tag_configure("eventag",background="white")
        my_tree.tag_configure("oddtag",background="lightblue")
        # config scrollbar
        my_scroll.config(command=my_tree.yview)
        #define columns
        if (self.user == "Customer"):
            columns = ("Booking No","Booking date","Check In","Check Out","No of Adults","No of Childs","Mealplan","Room ID","Total Price","Discount",
            "Advance","Balance")
        else:
            columns = ("Booking No","Check In","Check Out","No of Adults","No of Childs","Mealplan","Room ID","Total Price","Discount",
            "Advance","Balance")
        my_tree["columns"] = columns
        #format columns
        my_tree.column("#0",width=0,minwidth=0,stretch=NO)
        for x in columns:
            my_tree.column(x,anchor=CENTER,width=80)
        #create headings
        my_tree.heading("#0",text="")
        for x in columns:
            my_tree.heading(x,text=x,anchor=CENTER)
        
        self.insert_data(bookings)

        button2 = Button(self.frame, text="Close", padx=15, pady=0,
                        font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                        relief=RAISED, activebackground="crimson", bd=3,command=close)
        button2.grid(row=2, column=0,padx=10)
        
        self.root.mainloop()
    
    def make_header(self):
        label1 = Label(self.frame, text="Customer Bookings", font=(
            "Cooper Black", 25), padx=30, pady=5, bg="#3A5FCD", bd=0)
        label1.grid(row=0, column=0, pady=5, padx=5, columnspan=2)

    def insert_data(self,bookings):
        global my_tree
        new_bookings = []
        for record in bookings:
            record = list(record)
            if (self.user == "Customer"):
                noc = int(record[5])+int(record[6])+int(record[7])
                record.pop(5);record.pop(5);record.pop(5)
                record.insert(5,noc)
            else:
                noc = int(record[4])+int(record[5])+int(record[6])
                record.pop(4);record.pop(4);record.pop(4)
                record.insert(4,noc)
            record = tuple(record)
            new_bookings.append(record)
        #####################
        def enable_buttons(e):
            if (self.user == "Admin"):self.active_buttons()
        #####################
        #insert data
        count = 0
        for record in new_bookings:
            if (count%2 == 0):
                my_tree.insert(parent="",index="end",iid=count,text="",values=record,tags="eventag")
            else:
                my_tree.insert(parent="",index="end",iid=count,text="",values=record,tags="oddtag")
            count += 1
            my_tree.bind("<ButtonRelease-1>",enable_buttons)
    
    def clear_rows(self):
        for item in my_tree.get_children():
            my_tree.delete(item)
    
    def delete_details(self):
        global my_tree
        x = my_tree.focus()
        if (len(x) > 0): 
            row_detail = my_tree.item(x,"values")
            connection = sqlite3.connect('hotelmanagement.db')
            cursor = connection.cursor()
            cursor.execute(f'delete from checkout where Booking_No="{row_detail[0]}"')
            connection.commit()
            connection.close()
            my_tree.delete(x)
        else:
            messagebox.showerror("Admin tasks","Please select a record")

    def print_report(self):
        global my_tree
        selected = my_tree.selection()
        booking_details = [];selections = len(selected)
        for i in range(selections):
            row = selected[i]
            details = list(my_tree.item(row,"values"))
            booking_details.append(details)
        top = Toplevel()
        self.show_printed_report(top,booking_details,selections)
    
    def show_printed_report(self,root,booking_details,selections):
        root.iconbitmap("hotel.ico")
        frame1 = LabelFrame(root)
        frame1.pack(side=TOP,fill=BOTH)

        label1 = Label(frame1,text="Booking No",font=("Times New Roman",12),padx=0,pady=5,bg="darkturquoise",highlightthickness=2)
        label1.grid(row=0,column=0,pady=5)
        label1.config(highlightbackground="#00868B",highlightcolor="#00868B",width=10)

        label3 = Label(frame1,text="Check In",font=("Times New Roman",12),pady=5,bg="darkturquoise",highlightthickness=2)
        label3.grid(row=0,column=1,pady=5)
        label3.config(highlightbackground="#00868B",highlightcolor="#00868B",width=10)

        label4 = Label(frame1,text="Check Out",font=("Times New Roman",12),pady=5,bg="darkturquoise",highlightthickness=2)
        label4.grid(row=0,column=2,pady=5)
        label4.config(highlightbackground="#00868B",highlightcolor="#00868B",width=10)

        label5 = Label(frame1,text="No of Adults",font=("Times New Roman",12),pady=5,bg="darkturquoise",highlightthickness=2)
        label5.grid(row=0,column=3,pady=5)
        label5.config(highlightbackground="#00868B",highlightcolor="#00868B",width=10)

        label6 = Label(frame1,text="No of Childs",font=("Times New Roman",12),pady=5,bg="darkturquoise",highlightthickness=2)
        label6.grid(row=0,column=4,pady=5)
        label6.config(highlightbackground="#00868B",highlightcolor="#00868B",width=10)

        label7 = Label(frame1,text="Meal Plan",font=("Times New Roman",12),pady=5,bg="darkturquoise",highlightthickness=2)
        label7.grid(row=0,column=5,pady=5)
        label7.config(highlightbackground="#00868B",highlightcolor="#00868B",width=10)

        label8 = Label(frame1,text="Room ID",font=("Times New Roman",12),pady=5,bg="darkturquoise",highlightthickness=2)
        label8.grid(row=0,column=6,pady=5)
        label8.config(highlightbackground="#00868B",highlightcolor="#00868B",width=10)

        label9 = Label(frame1,text="Total Price",font=("Times New Roman",12),pady=5,bg="darkturquoise",highlightthickness=2)
        label9.grid(row=0,column=7,pady=5)
        label9.config(highlightbackground="#00868B",highlightcolor="#00868B",width=10)

        label12 = Label(frame1,text="Discount",font=("Times New Roman",12),pady=5,bg="darkturquoise",highlightthickness=2)
        label12.grid(row=0,column=8,pady=5)
        label12.config(highlightbackground="#00868B",highlightcolor="#00868B",width=10)

        label10 = Label(frame1,text="Advance",font=("Times New Roman",12),pady=5,bg="darkturquoise",highlightthickness=2)
        label10.grid(row=0,column=9,pady=5)
        label10.config(highlightbackground="#00868B",highlightcolor="#00868B",width=10)

        label11 = Label(frame1,text="Balance",font=("Times New Roman",12),pady=5,bg="darkturquoise",highlightthickness=2)
        label11.grid(row=0,column=10,pady=5)
        label11.config(highlightbackground="#00868B",highlightcolor="#00868B",width=10)

        for i in range(selections):
            for j in range(11):
                label = Label(frame1,text=booking_details[i][j],font=("Times New Roman",12),pady=5,bg="darkturquoise",highlightthickness=2)
                label.grid(row=i+1,column=j,pady=5)
                label.config(highlightbackground="#00868B",highlightcolor="#00868B",width=10)     

        root.mainloop()
        



        


    
