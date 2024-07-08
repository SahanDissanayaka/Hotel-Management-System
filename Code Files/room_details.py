from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import sqlite3
from dbcreatefile import idcreater
import admin_login

class Room_details():

    def __init__(self,root,frame,username,password,name):
        self.root = root
        self.frame = frame
        self.username = username
        self.password = password
        self.name = name
    
    def show(self):
        x = int((1520-1035)/2)
        y = int((810-550)/2)
        self.root.geometry(f'1035x550+{x}+{y}')
        self.root.minsize(1035,550)
        self.root.maxsize(1035,550)
        ####### Button Commands ##########
        def search():
            if (len(txt4.get()) > 0):
                txt = txt4.get()
                self.search_room(txt)
            else:
                messagebox.showerror("Admin tasks","Please enter Room ID")
        def add():
            self.add_room()
        def select():
            self.select_room()
        def update():
            self.update_room()
        def delete():
            self.delete_room()
        def clear():
            self.clear_details()
        def enable_buttons(e):
            button4.configure(state=NORMAL);button6.configure(state=NORMAL)
        def close():
            response = messagebox.askyesno("Admin tasks","Do you want to close Room Details?")
            if (response==True):
                for widject in self.frame.winfo_children():
                    widject.destroy()
                alogin = admin_login.Admin_login(self.root,self.frame,self.username,self.password,self.name)
                alogin.login()
        ##################################
        global txt1;global txt2;global txt3;global state;global category;global floor_no;global my_tree
        global count;global button3;global button6;global button4
        label1 = Label(self.frame, text="Manage Room Details", font=(
            "Cooper Black", 20), padx=30, pady=5, bg="#3A5FCD", bd=0)
        label1.grid(row=0, column=0, pady=0, padx=3, columnspan=2)

        frame1 = Frame(self.frame, bg="darkturquoise", padx=10, pady=19)
        frame1.grid(row=1, column=0, pady=20, padx=20)

        label2 = Label(frame1, text="Room No", font=("Times New Roman", 12),
                    padx=20, pady=5, bg="darkturquoise", highlightthickness=2)
        label2.grid(row=1, column=0, pady=8)
        label2.config(highlightbackground="#00868B", highlightcolor="#00868B")
        txt1 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt1.grid(row=1, column=1, padx=5)

        label3 = Label(frame1, text="Catergory", font=("Times New Roman", 12),
                    padx=20, pady=5, bg="darkturquoise", highlightthickness=2)
        label3.grid(row=2, column=0, pady=8)
        label3.config(highlightbackground="#00868B", highlightcolor="#00868B")
        categories = ["Single", "Double", "Triple",
                    "Quad", "Queen", "King", "Twin", "Suite"]
        category = StringVar()
        category.set('Select')
        menubox1 = OptionMenu(frame1, category, *categories)
        menubox1.grid(row=2, column=1)
        menubox1.config(width=20, bg="#79CDCD", activebackground="#79CDCD")

        label4 = Label(frame1, text="Floor No", font=("Times New Roman", 12),
                    padx=22, pady=5, bg="darkturquoise", highlightthickness=2)
        label4.grid(row=3, column=0, pady=8)
        label4.config(highlightbackground="#00868B", highlightcolor="#00868B")
        floor_no = IntVar()
        floor_no.set("Select")
        menubox2 = OptionMenu(frame1, floor_no, 1, 2, 3)
        menubox2.grid(row=3, column=1)
        menubox2.config(width=20, bg="#79CDCD", activebackground="#79CDCD")

        label5 = Label(frame1, text="Up to", font=("Times New Roman", 12),
                    padx=33, pady=5, bg="darkturquoise", highlightthickness=2)
        label5.grid(row=4, column=0, pady=8)
        label5.config(highlightbackground="#00868B", highlightcolor="#00868B")
        txt2 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt2.grid(row=4, column=1, padx=5)

        label6 = Label(frame1, text="State", font=("Times New Roman", 12),
                    padx=35, pady=5, bg="darkturquoise", highlightthickness=2)
        label6.grid(row=5, column=0, pady=8)
        label6.config(highlightbackground="#00868B", highlightcolor="#00868B")
        state = StringVar()
        state.set("Select")
        menubox2 = OptionMenu(frame1, state, "Available", "Booked")
        menubox2.grid(row=5, column=1)
        menubox2.config(width=20, bg="#79CDCD", activebackground="#79CDCD")

        label7 = Label(frame1, text="Price", font=("Times New Roman", 12),
                    padx=35, pady=5, bg="darkturquoise", highlightthickness=2)
        label7.grid(row=6, column=0, pady=8)
        label7.config(highlightbackground="#00868B", highlightcolor="#00868B")
        txt3 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt3.grid(row=6, column=1, padx=5)

        frame2 = Frame(self.frame, bg="darkturquoise", padx=10, pady=20)
        frame2.grid(row=1, column=1, pady=20, padx=10)

        frame3 = Frame(frame2,bg="darkturquoise")
        frame3.grid(row=0,column=0)

        label8 = Label(frame3, text="Room ID", font=("Times New Roman", 12),
                    padx=20, pady=5, bg="darkturquoise", highlightthickness=2)
        label8.grid(row=0, column=0, pady=5)
        label8.config(highlightbackground="#00868B", highlightcolor="#00868B")
        txt4 = Entry(frame3, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt4.grid(row=0, column=1, padx=5)
        button1 = Button(frame3, text="Search", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=search)
        button1.grid(row=0, column=2)

        # adding style
        my_style = ttk.Style()
        my_style.theme_use("default")
        my_style.configure("Treeview",background="silver",foreground="black",rowheight=25,fieldbackground="silver")
        my_style.map("Treeview",background=[("selected","blue")])
        # add a scrollbutton
        my_scroll = Scrollbar(frame2)
        my_scroll.grid(row=1,column=4,sticky=NS)
        # creating treeveiw
        my_tree = ttk.Treeview(frame2,yscrollcommand=my_scroll.set)
        my_tree.grid(row=1, column=0)
        #configure tags
        my_tree.tag_configure("eventag",background="white")
        my_tree.tag_configure("oddtag",background="lightblue")
        # config scrollbar
        my_scroll.config(command=my_tree.yview)
        # define columns
        my_tree["columns"] = ("Room ID", "Category", "Floor No",
                            "Room No", "State", "Price")
        # format columns
        my_tree.column("#0", width=0, minwidth=0, stretch=NO)
        my_tree.column("Room ID", anchor=CENTER, width=100)
        my_tree.column("Category", anchor=CENTER, width=100)
        my_tree.column("Floor No", anchor=CENTER, width=100)
        my_tree.column("Room No", anchor=CENTER, width=100)
        my_tree.column("State", anchor=CENTER, width=100)
        my_tree.column("Price", anchor=CENTER, width=100)
        # create headiings
        my_tree.heading("#0", text="")
        my_tree.heading("Room ID", text="Room ID", anchor=CENTER)
        my_tree.heading("Category", text="Category", anchor=CENTER)
        my_tree.heading("Floor No", text="Floor No", anchor=CENTER)
        my_tree.heading("Room No", text="Room No", anchor=CENTER)
        my_tree.heading("State", text="State", anchor=CENTER)
        my_tree.heading("Price", text="Price", anchor=CENTER)
        # adding data
        connection = sqlite3.connect("hotelmanagement.db")
        cursor = connection.cursor()
        cursor.execute('select Room_ID,Category,Floor_No,Room_No ,Availability,Price_for_day from rooms')
        data = cursor.fetchall()
        connection.close()
        count = 0
        for record in data:
            if (count%2 == 0):
                my_tree.insert(parent='', index='end', iid=count, text="", values=record,tag="eventag")
            else:
                my_tree.insert(parent='',index='end',iid=count,text="",values=record,tag="oddtag")
            count += 1
        # binding
        my_tree.bind("<ButtonRelease-1>",enable_buttons)
        #creating buttons
        frame4 = Frame(self.frame,bg="#3A5FCD",pady=10)
        frame4.grid(row=2,column=0,columnspan=2)
        button2 = Button(frame4, text="Add", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=add)
        button2.grid(row=0, column=0,padx=50)
        button6 = Button(frame4, text="Select", padx=7, pady=0,
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
    
    def search_room(self,txt):
        connection = sqlite3.connect("hotelmanagement.db")
        cursor = connection.cursor()
        cursor.execute(f'select Room_ID,Category,Floor_No,Room_No ,Availability,Price_for_day from rooms where Room_ID="{txt}"')
        data = cursor.fetchall()
        if (len(data) == 0):
            messagebox.showerror("Admin tasks","Please Enter valid Room ID")
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

    def add_room(self):
        global txt1;global txt2;global txt3;global state;global category;global floor_no;global my_tree
        global count
        txtareas = [txt1,txt2,txt3]
        if (self.is_text_full(txtareas) and category.get() != "Select" and floor_no.get() != "Select" and state.get() != "Select"):
            room_id = idcreater("roomid")
            details = (room_id,category.get(),floor_no.get(),txt1.get(),state.get(),txt3.get())
            if (count%2 ==0):
                my_tree.insert(parent="",index="end",iid=count,text="",values=details,tags="eventag")
                count += 1
            else:
                my_tree.insert(parent="",index="end",iid=count,text="",values=details,tags="oddtag")
                count += 1
            day_cost = int(txt3.get())
            adding_details = [room_id,txt1.get(),floor_no.get(),category.get(),txt2.get(),state.get(),int(day_cost/12),day_cost]
            connection = sqlite3.connect("hotelmanagement.db")
            cursor = connection.cursor()
            cursor.execute('insert into rooms values (?,?,?,?,?,?,?,?)',adding_details)
            connection.commit()
            connection.close()
            self.clear_details()
        else:
            messagebox.showerror("Room Adding failed","Please fill all the text areas")
    
    def select_room(self):
        global txt1;global txt2;global txt3;global state;global category;global floor_no;global my_tree;global button3;global button6
        select_row = my_tree.focus();global details
        details = my_tree.item(select_row,"values")
        category.set(details[1]);floor_no.set(details[2]);txt1.insert(0,details[3]);state.set(details[4]);txt3.insert(0,details[5])
        connection = sqlite3.connect("hotelmanagement.db")
        cursor = connection.cursor()
        cursor.execute(f'select Up_to from rooms where Room_ID="{details[0]}"')
        up_to = cursor.fetchall()[0][0]
        txt2.insert(0,str(up_to))
        connection.close()
        button3.configure(state=NORMAL);button6.configure(state=DISABLED)
        

    def update_room(self):
        txtareas = [txt1,txt2,txt3];global button3
        select_row = my_tree.focus();global details
        if (self.is_text_full(txtareas) and category.get() != "Select" and floor_no.get() != "Select" and state.get() != "Select"):
            updated_details = (details[0],category.get(),floor_no.get(),txt1.get(),state.get(),txt3.get())
            my_tree.item(select_row,text="",values=updated_details)
            connection = sqlite3.connect("hotelmanagement.db")
            cursor = connection.cursor()
            day_cost = int(txt3.get())
            cursor.execute(f'update rooms set Room_No={txt1.get()},Floor_No={floor_no.get()},Category="{category.get()}",Up_to={txt2.get()},Availability="{state.get()}",\
                Price_for_hour={int(day_cost/12)},Price_for_day={day_cost} where Room_Id="{details[0]}"')
            connection.commit()
            connection.close()
            self.clear_details()
            button4.configure(state=DISABLED)
        else:
            messagebox.showerror("Room Adding failed","Please fill all the text areas")

    def delete_room(self):
        global button4
        select_row = my_tree.focus()
        details = my_tree.item(select_row,"values")
        x = my_tree.selection()
        for record in x:
            my_tree.delete(record)
        connection = sqlite3.connect("hotelmanagement.db")
        cursor = connection.cursor()
        cursor.execute(f'delete from rooms where Room_ID="{details[0]}"')
        connection.commit()
        connection.close()
        button4.configure(state=DISABLED)

    def clear_details(self):
        global txt1;global txt2;global txt3;global state;global category;global floor_no
        txt1.delete(0,END);txt2.delete(0,END);txt3.delete(0,END);category.set("Select");floor_no.set("Select");state.set("Select")
