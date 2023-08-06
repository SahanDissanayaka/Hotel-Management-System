from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import admin_login
from dbcreatefile import idcreater

class Customer_details():

    def __init__(self,root,frame,username,password,name):
        self.root = root
        self.frame = frame
        self.username = username
        self.password = password
        self.name = name
        self.user = "Admin"
    
    def show(self):
        self.root.title("Royal Hotel")
        self.root.iconbitmap("hotel.ico")
        x = int((1520-1110)/2)
        y = int((810-750)/2)
        self.root.geometry(f'1110x750+{x}+{y}')
        self.root.minsize(1110,750)
        self.root.maxsize(1110,750)
        self.root.configure(bg="#3A5FCD")
        ########## Button Commands ###########
        def search():
            if (len(txt1.get()) > 0 and selection.get() != "Select"):
                txt = txt1.get();mode = str(selection.get())
                self.search_customer(txt,mode)
            else:
                messagebox.showerror("Admin tasks","Please fill required fields")

        def add():
            self.add_customer()
        
        def select():
            self.select_customer()
        
        def update():
            self.update_customer()

        def delete():
            self.delete_customer()

        def clear():
            self.clear_details()
        
        def enable_buttons(e):
            button6.configure(state=NORMAL);button4.configure(state=NORMAL)
        
        def close():
            for widject in self.frame.winfo_children():
                widject.destroy()
            alogin = admin_login.Admin_login(self.root,self.frame,self.username,self.password,self.name)
            alogin.login()
        #####################################
        global my_tree;global txt1;global txt2;global txt3;global txt4;global txt5;global txt6;global txt7;global txt8;global txt9
        global gender;global txtbox;global count;global button3;global button4;global button6
        label1 = Label(self.frame, text="Manage Customer Details",
                    font=("Cooper Black", 20), padx=30, pady=5, bg="#3A5FCD", bd=0)
        label1.grid(row=0, column=0, pady=0, padx=3, columnspan=2)

        frame1 = Frame(self.frame, bg="darkturquoise", padx=10, pady=5)
        frame1.grid(row=1, column=0, pady=10, padx=10)

        frame2 = LabelFrame(frame1,text="Search Customer", bg="darkturquoise", padx=5, pady=5)
        frame2.grid(row=0,column=0,columnspan=6)
        selection = StringVar()
        selection.set("Select")
        menubox1 = OptionMenu(frame2,selection,"Customer ID","First Name","Contact No")
        menubox1.grid(row=0,column=0)
        menubox1.config(width=15, bg="#79CDCD", activebackground="#79CDCD")
        txt1 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt1.grid(row=0, column=1, padx=5)
        button1 = Button(frame2, text="Search", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 13), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=search)
        button1.grid(row=0, column=2)

        label2 = Label(frame1,text="Customer ID",font=("Times New Roman",12),padx=15,pady=5,bg="darkturquoise",highlightthickness=2)
        label2.grid(row=1,column=0,pady=5,padx=5)
        label2.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt2 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt2.grid(row=1,column=1)

        label3 = Label(frame1,text="Gender",font=("Times New Roman",12),padx=32,pady=5,bg="darkturquoise",highlightthickness=2)
        label3.grid(row=2,column=0,pady=5,padx=5)
        label3.config(highlightbackground="#00868B",highlightcolor="#00868B")
        gender = StringVar()
        gender.set("Select ")
        menubox2 = OptionMenu(frame1,gender,"Male","Female")
        menubox2.grid(row=2,column=1)
        menubox2.config(width=20,bg="#79CDCD",activebackground="#79CDCD")

        label4 = Label(frame1,text="Contact No",font=("Times New Roman",12),padx=21,pady=5,bg="darkturquoise",highlightthickness=2)
        label4.grid(row=2,column=2,pady=5,padx=5)
        label4.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt3 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt3.grid(row=2,column=3)

        label5 = Label(frame1,text="First Name",font=("Times New Roman",12),padx=23,pady=5,bg="darkturquoise",highlightthickness=2)
        label5.grid(row=1,column=2,pady=5)
        label5.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt4 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt4.grid(row=1,column=3)

        label6 = Label(frame1,text="Last Name",font=("Times New Roman",12),padx=21,pady=5,bg="darkturquoise",highlightthickness=2)
        label6.grid(row=1,column=4,pady=5,padx=7)
        label6.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt5 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt5.grid(row=1,column=5)

        label7 = Label(frame1,text="Date of Birth",font=("Times New Roman",12),padx=15,pady=5,bg="darkturquoise",highlightthickness=2)
        label7.grid(row=2,column=4,pady=5)
        label7.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt6 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt6.grid(row=2,column=5)

        label8 = Label(frame1,text="Email Address",font=("Times New Roman",12),padx=10,pady=5,bg="darkturquoise",highlightthickness=2)
        label8.grid(row=3,column=0,pady=5)
        label8.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt7 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt7.grid(row=3,column=1)

        label9 = Label(frame1,text="Nationality",font=("Times New Roman",12),padx=25,pady=5,bg="darkturquoise",highlightthickness=2)
        label9.grid(row=3,column=2,pady=5)
        label9.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt8 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt8.grid(row=3,column=3)

        label10 = Label(frame1,text="ID No",font=("Times New Roman",12),padx=35,pady=5,bg="darkturquoise",highlightthickness=2)
        label10.grid(row=3,column=4,pady=5)
        label10.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt9 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt9.grid(row=3,column=5)

        label11 = Label(frame1,text="Address",font=("Times New Roman",12),padx=29,pady=5,bg="darkturquoise",highlightthickness=2)
        label11.grid(row=4,column=0,pady=5,sticky=N)
        label11.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txtbox = Text(frame1,width=21,height=4,bg="#79CDCD",font=("Times New Roman", 13))
        txtbox.grid(row=4,column=1)

        frame3 = Frame(self.frame,padx=3,pady=3,bg="darkturquoise")
        frame3.grid(row=2,column=0,padx=20)

        # adding style
        my_style = ttk.Style()
        my_style.theme_use("default")
        my_style.configure("Treeview",background="silver",foreground="black",rowheight=25,fieldbackground="silver")
        my_style.map("Treeview",background=[("selected","blue")])
        # add a scrollbutton
        my_scroll = Scrollbar(frame3)
        my_scroll.grid(row=0,column=1,sticky=NS)
        #creating treeview
        my_tree = ttk.Treeview(frame3,yscrollcommand=my_scroll.set)
        my_tree.grid(row=0,column=0)
        #configure tags
        my_tree.tag_configure("eventag",background="white")
        my_tree.tag_configure("oddtag",background="lightblue")
        # config scrollbar
        my_scroll.config(command=my_tree.yview)
        #define columns
        my_tree["columns"] = ("Customer ID","First Name","Last Name","Gender","Contact No","Date of Birth","Email Address","Nationality","ID No","Address")
        #format columns
        my_tree.column("#0",width=0,minwidth=0,stretch=NO)
        my_tree.column("Customer ID",anchor=CENTER,width=80)
        my_tree.column("First Name",anchor=CENTER,width=80)
        my_tree.column("Last Name",anchor=CENTER,width=80)
        my_tree.column("Gender",anchor=CENTER,width=60)
        my_tree.column("Contact No",anchor=CENTER,width=100)
        my_tree.column("Date of Birth",anchor=CENTER,width=100)
        my_tree.column("Email Address",anchor=CENTER,width=150)
        my_tree.column("Nationality",anchor=CENTER,width=80)
        my_tree.column("ID No",anchor=CENTER,width=100)
        my_tree.column("Address",anchor=CENTER,width=220)
        #create headings
        my_tree.heading("#0",text="")
        my_tree.heading("Customer ID",text="Customer ID",anchor=CENTER)
        my_tree.heading("First Name",text="First Name",anchor=CENTER)
        my_tree.heading("Last Name",text="Last Name",anchor=CENTER)
        my_tree.heading("Gender",text="Gender",anchor=CENTER)
        my_tree.heading("Contact No",text="Contact No",anchor=CENTER)
        my_tree.heading("Date of Birth",text="Date of Birth",anchor=CENTER)
        my_tree.heading("Email Address",text="Email Address",anchor=CENTER)
        my_tree.heading("Nationality",text="Nationality",anchor=CENTER)
        my_tree.heading("ID No",text="ID No",anchor=CENTER)
        my_tree.heading("Address",text="Address",anchor=CENTER)
        #adding data
        connection = sqlite3.connect("hotelmanagement.db")
        cursor = connection.cursor()
        cursor.execute('select Customer_ID,First_Name,Last_Name,Gender,Contact_No,DOB,Email_Address,Nationality,ID_No,Address from customers')
        data = cursor.fetchall()
        connection.close()
        count = 0
        for record in data:
            if (count%2 == 0):
                my_tree.insert(parent='',index='end',iid=count,text='',values=record,tags="eventag")
            else:
                my_tree.insert(parent='',index='end',iid=count,text='',values=record,tags="oddtag")
            count += 1
        #binding
        my_tree.bind("<ButtonRelease-1>",enable_buttons)
        #creating buttons
        frame4 = Frame(self.frame,bg="#3A5FCD",pady=10)
        frame4.grid(row=3,column=0,pady=10)
        button2 = Button(frame4, text="Add", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=add)
        button2.grid(row=0, column=0,padx=50)
        button6 = Button(frame4, text="Select", padx=10, pady=0,
                 font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                 relief=RAISED, activebackground="mediumspringgreen", bd=3,command=select,state=DISABLED)
        button6.grid(row=0, column=1,padx=50)
        button3 = Button(frame4, text="Update", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=update,state=DISABLED)
        button3.grid(row=0, column=2,padx=50)
        button4 = Button(frame4, text="Delete", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="crimson", bd=3,command=delete,state=DISABLED)
        button4.grid(row=0, column=3,padx=50)
        button5 = Button(frame4, text="Clear", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=clear)
        button5.grid(row=0, column=4,padx=50)
        button7 = Button(frame4, text="Close", padx=15, pady=0,
                 font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                 relief=RAISED, activebackground="crimson", bd=3,command=close)
        button7.grid(row=1, column=2,padx=50,pady=10)

        self.root.mainloop()
    
    def search_customer(self,txt,mode):
        connection = sqlite3.connect("hotelmanagement.db")
        cursor = connection.cursor()
        if (mode == "Customer ID"):
            cursor.execute(f'select Customer_ID,First_Name,Last_Name,Gender,Contact_No,DOB,Email_Address,Nationality,ID_No,Address from customers where Customer_ID="{txt}"')
        elif (mode == "Contact No"):
            cursor.execute(f'select Customer_ID,First_Name,Last_Name,Gender,Contact_No,DOB,Email_Address,Nationality,ID_No,Address from customers where Contact_No="{txt}"')
        else:
            cursor.execute(f'select Customer_ID,First_Name,Last_Name,Gender,Contact_No,DOB,Email_Address,Nationality,ID_No,Address from customers where First_Name="{txt}"')
        data = cursor.fetchall()
        if (len(data) == 0):
            messagebox.showerror("Admin tasks","Please Enter valid Details")
        else:
            for row in my_tree.get_children():
                my_tree.delete(row)
            global count
            count = 0
            for record in data:
                if (count%2 == 0):
                    my_tree.insert(parent='', index='end', iid=count, text="", values=record,tag="eventag")
                else:
                    my_tree.insert(parent='',index='end',iid=count,text="",values=record,tag="oddtag")
                count += 1
        connection.close()
    
    def is_text_full(self,List):# can know whether entry boxes are full or not by giving there variable in a list as a parameter
        for entry in List:
            x = len(entry.get())
            if (x==0):
                return False
        else:
            return True
            
    def add_customer(self):
        global my_tree;global txt1;global txt2;global txt3;global txt4;global txt5;global txt6;global txt7;global txt8;global txt9
        global gender;global txtbox;global count
        txtareas = [txt3,txt4,txt5,txt6,txt7,txt8,txt9]
        customer_id = idcreater("customerid")
        if (self.is_text_full(txtareas) and gender.get() != "Select"):
            lines = txtbox.get("1.0","end-1c").split("\n");address = ""
            for line in lines:
                address += line + " "
            details = (customer_id,txt4.get(),txt5.get(),gender.get(),txt3.get(),txt6.get(),txt7.get(),txt8.get(),txt9.get(),address)#datagrid
            if (count%2 == 0):
                my_tree.insert(parent="",index="end",iid=count,text="",values=details,tags="eventag")
                count += 1
            else:
                my_tree.insert(parent="",index="end",iid=count,text="",values=details,tags="oddtag")
                count += 1
            adding_details = [(customer_id,"Title",txt4.get(),txt5.get(),address,gender.get(),txt6.get(),txt9.get(),txt8.get(),
            txt7.get(),customer_id,customer_id,txt3.get())]
            connection = sqlite3.connect("hotelmanagement.db")
            cursor = connection.cursor()
            cursor.execute('insert into customers values (?,?,?,?,?,?,?,?,?,?,?,?,?)',*adding_details)
            connection.commit()
            connection.close()
            txt3.delete(0,END);txt4.delete(0,END,);txt5.delete(0,END);txt6.delete(0,END);txt7.delete(0,END);txt8.delete(0,END)
            txt9.delete(0,END);gender.set("Select");txtbox.delete("1.0","end");txt2.delete(0,END)
        else:
            messagebox.showerror("Customer Adding failed","Please fill all the text areas")
    
    def select_customer(self):
        global my_tree;global txt1;global txt2;global txt3;global txt4;global txt5;global txt6;global txt7;global txt8;global txt9
        global gender;global txtbox;global button3;global button6
        txt2.delete(0,END)
        selected_row = my_tree.focus()
        details = my_tree.item(selected_row,"values")
        lines = details[9].split(" ")
        if ("" in lines):lines.remove("")
        address=""
        for line in lines:
            address += line + "\n"
        txt2.insert(0,details[0]);txt4.insert(0,details[1]);txt5.insert(0,details[2]);gender.set(details[3]);txt3.insert(0,details[4])
        txt6.insert(0,details[5]);txt7.insert(0,details[6]);txt8.insert(0,details[7]);txt9.insert(0,details[8]);txtbox.insert("1.0",address)
        button6.configure(state=DISABLED);button3.configure(state=NORMAL)

    def update_customer(self):
        global my_tree;global txt1;global txt2;global txt3;global txt4;global txt5;global txt6;global txt7;global txt8;global txt9
        global gender;global txtbox;global button3
        selected_row = my_tree.focus()
        details = my_tree.item(selected_row,"values")
        txtareas = [txt3,txt4,txt5,txt6,txt7,txt8,txt9]
        if (self.is_text_full(txtareas) and gender.get() != "Select"):
            lines = txtbox.get("1.0","end-1c").split("\n");address = ""
            for line in lines:
                address += line + " "
            while ("" in lines):
                lines.remove("")
            updated_details = (txt2.get(),txt4.get(),txt5.get(),gender.get(),txt3.get(),txt6.get(),txt7.get(),txt8.get(),txt9.get(),address)
            my_tree.item(selected_row,text="",values=updated_details)
            connection = sqlite3.connect("hotelmanagement.db")
            cursor = connection.cursor()
            cursor.execute(f'update customers set First_Name="{updated_details[1]}",Last_Name="{updated_details[2]}",Gender="{updated_details[3]}",Address="{updated_details[9]}",\
                DOB="{updated_details[5]}",Nationality="{updated_details[7]}",Email_Address="{updated_details[6]}",Contact_No="{updated_details[4]}",ID_No="{updated_details[8]}"\
                    where Customer_ID="{details[0]}"')
            connection.commit()
            connection.close()
            txt3.delete(0,END);txt4.delete(0,END,);txt5.delete(0,END);txt6.delete(0,END);txt7.delete(0,END);txt8.delete(0,END)
            txt9.delete(0,END);gender.set("Select");txtbox.delete("1.0","end");txt2.delete(0,END)
            button3.configure(state=DISABLED)
        else:
            messagebox.showerror("Customer Adding failed","Please fill all the text areas")
    
    def delete_customer(self):
        global button4
        select_row = my_tree.focus()
        details = my_tree.item(select_row,"values")
        x = my_tree.selection()
        for record in x:
            my_tree.delete(record)
        connection = sqlite3.connect("hotelmanagement.db")
        cursor = connection.cursor()
        cursor.execute(f'delete from customers where Customer_ID="{details[0]}"')
        connection.commit()
        connection.close()
        button4.configure(state=DISABLED)
    
    def clear_details(self):
        global my_tree;global txt1;global txt2;global txt3;global txt4;global txt5;global txt6;global txt7;global txt8;global txt9
        global gender;global txtbox
        txt3.delete(0,END);txt4.delete(0,END,);txt5.delete(0,END);txt6.delete(0,END);txt7.delete(0,END);txt8.delete(0,END)
        txt9.delete(0,END);gender.set("Select");txtbox.delete("1.0","end")