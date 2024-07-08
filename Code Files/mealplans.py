from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class Mealplan():

    def __init__(self,root,frame):
        self.root = root
        self.frame = frame
        self.user = "Customer"
    
    def show_mealplans(self):
        self.root.title("Royal Hotel")
        self.root.iconbitmap("hotel.ico")
        self.root.configure(bg="#3A5FCD")
        self.frame.configure(bg="#3A5FCD")
        if (self.user == "Customer"):
            x = int((1520-480)/2)
            y = int((810-500)/2)
            self.root.geometry(f'480x500+{x}+{y}')
            self.root.minsize(480,500)
            self.root.maxsize(480,500)
        else:
            x = int((1520-505)/2)
            y = int((810-655)/2)
            self.root.geometry(f'505x655+{x}+{y}')
            self.root.minsize(505,655)
            self.root.maxsize(505,655)
        ###############################
        def enable_buttons(e):
            self.active_buttons()
        ###############################
        global my_tree;global count
        label1 = Label(self.frame, text="Meal Plans", font=(
            "Cooper Black", 20), padx=30, pady=5, bg="#3A5FCD", bd=0)
        label1.grid(row=0, column=0, pady=3, padx=3)

        frame1 = Frame(self.frame, bg="darkturquoise", padx=10, pady=19)
        frame1.grid(row=1, column=0, pady=10, padx=20)
        #adding style
        my_style = ttk.Style()
        my_style.theme_use("default")
        my_style.configure("Treeview",background="silver",foreground="black",rowheight=30,fieldbackground="silver")
        my_style.map("Treeview",background=[("selected","blue")])
        # add a scrollbutton
        my_scroll = Scrollbar(frame1)
        my_scroll.grid(row=1,column=1,sticky=NS)
        #creating treeview
        my_tree = ttk.Treeview(frame1,yscrollcommand=my_scroll.set)
        my_tree.grid(row=1,column=0)
        #tags
        my_tree.tag_configure("eventag",background="white")
        my_tree.tag_configure("oddtag",background="lightblue")
        #configure scrollbar
        my_scroll.config(command=my_tree.yview)
        #define columns
        my_tree["columns"] = ("Meal Plan","Price for one guest")
        #format columns
        my_tree.column("#0", width=0, minwidth=0, stretch=NO)
        my_tree.column("Meal Plan", anchor=CENTER, width=200)
        my_tree.column("Price for one guest", anchor=CENTER, width=200)
        #create headings
        my_tree.heading("#0", text="")
        my_tree.heading("Meal Plan", text="Meal Plan", anchor=CENTER)
        my_tree.heading("Price for one guest", text="Price for one guest", anchor=CENTER)
        #insert data
        connection = sqlite3.connect('hotelmanagement.db')
        cursor = connection.cursor()
        cursor.execute('select * from mealplans')
        data = cursor.fetchall()
        count = 0
        for record in data:
            if (count%2 == 0):
                my_tree.insert(parent="",index="end",iid=count,text="",values=record,tags="eventag")
                count += 1
            else:
                my_tree.insert(parent="",index="end",iid=count,text="",values=record,tags="oddtag")
                count += 1
        #binding
        my_tree.bind("<ButtonRelease-1>",enable_buttons)
        connection.close()
        self.make_footer()
        self.root.mainloop()
    
    def make_footer(self):
        def close():
            self.root.destroy()

        frame2 = Frame(self.frame, bg="#3A5FCD", padx=10, pady=10)
        frame2.grid(row=2, column=0, pady=5, padx=20)

        button = Button(frame2, text="Close", padx=15, pady=0,
                        font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                        relief=RAISED, activebackground="crimson", bd=3,command=close)
        button.grid(row=0, column=0,padx=10)
    
    def add_mealplan(self,new_record):
        global my_tree;global count
        if (count%2 == 0):
            my_tree.insert(parent="",index="end",iid=count,text="",values=new_record,tags="eventag")
            count += 1
        else:
            my_tree.insert(parent="",index="end",iid=count,text="",values=new_record,tags="oddtag")
            count += 1
        count += 1
        connection = sqlite3.connect('hotelmanagement.db')
        cursor = connection.cursor()
        cursor.execute('insert into mealplans values (?,?)',new_record)
        connection.commit()
        connection.close()
    
    def get_details(self):
        row = my_tree.focus()
        row_details = my_tree.item(row,"values")
        return row_details
    
    def update_mealplan(self,updated_record):
        row = my_tree.focus()
        prerec = my_tree.item(row,"values")
        my_tree.item(row,text="",values=updated_record)
        connection = sqlite3.connect('hotelmanagement.db')
        cursor = connection.cursor();rec = list(updated_record)
        cursor.execute(f'update mealplans set Price_for_one_to_one_customer={rec[1]} where Meal_Plan="{prerec[0]}"')
        connection.commit()
        connection.close()
    
    def delete_mealplan(self):
        selected = my_tree.focus()
        details = my_tree.item(selected,"values")
        my_tree.delete(selected)
        connection = sqlite3.connect('hotelmanagement.db')
        cursor = connection.cursor()
        cursor.execute(f'delete from mealplans where Meal_Plan="{details[0]}"')
        connection.commit()
        connection.close()


class Advancedmealplan(Mealplan):

    def __init__(self,root,frame):
        super().__init__(root,frame)
        self.user = "Admin"
    
    def make_footer(self):
        frame2 = Frame(self.frame, bg="darkturquoise", padx=5, pady=5)
        frame2.grid(row=2, column=0, pady=0, padx=20)
        ###########################################
        def add():
            if (len(txt1.get()) > 0 and len(txt2.get()) > 0):
                new_record = (txt1.get(),txt2.get())
                self.add_mealplan(new_record)
                clear()
            else:
                messagebox.showerror("Admin tasks","Please fill required text areas")
        def select():
            record = self.get_details()
            clear()
            txt1.insert(0,record[0]);txt2.insert(0,record[1])
            button3.configure(state=NORMAL)
        def update():
            if (len(txt1.get()) > 0 and len(txt2.get()) > 0):
                new_record = (txt1.get(),txt2.get())
                self.update_mealplan(new_record)
                clear()
                button3.configure(state=DISABLED)
            else:
                messagebox.showerror("Admin tasks","Please fill required text areas")
        def delete():
            self.delete_mealplan()
            button4.configure(state=DISABLED)
        def clear():
            txt1.delete(0,END);txt2.delete(0,END)
        def close():
            response = messagebox.askyesno("Admin tasks","Do you want to close Mealplans?")
            if (response==True):
                self.root.destroy()
        ###########################################
        global button6;global button4
        frame4 = Frame(frame2, bg="darkturquoise", padx=5, pady=5)
        frame4.grid(row=0, column=0, pady=5, padx=10)

        label1 = Label(frame4,text="Meal Plan",font=("Times New Roman",12),padx=71,pady=5,bg="darkturquoise",highlightthickness=2)
        label1.grid(row=0,column=0,pady=5)
        label1.config(highlightbackground="#00868B",highlightcolor="#00868B")
        label2 = Label(frame4,text="Price for one guest",font=("Times New Roman",12),padx=45,pady=5,bg="darkturquoise",highlightthickness=2)
        label2.grid(row=0,column=1,pady=5)
        label2.config(highlightbackground="#00868B",highlightcolor="#00868B")

        txt1 = Entry(frame4, width=25, borderwidth=5, bg="#79CDCD",font=("Times New Roman",12))
        txt1.grid(row=1,column=0)
        txt2 = Entry(frame4, width=25, borderwidth=5, bg="#79CDCD",font=("Times New Roman",12))
        txt2.grid(row=1,column=1)

        frame3 = Frame(frame2,bg="#3A5FCD",pady=5)
        frame3.grid(row=2,column=0,pady=10)
        button2 = Button(frame3, text="Add", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 12), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=add)
        button2.grid(row=0, column=0,padx=10)
        button6 = Button(frame3, text="Select", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 12), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=select,state=DISABLED)
        button6.grid(row=0, column=1,padx=10)
        button3 = Button(frame3, text="Update", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 12), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=update,state=DISABLED)
        button3.grid(row=0, column=2,padx=10)
        button4 = Button(frame3, text="Delete", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 12), bg="#87CEFA",
                        relief=RAISED, activebackground="crimson", bd=3,command=delete,state=DISABLED)
        button4.grid(row=0, column=3,padx=10)
        button5 = Button(frame3, text="Clear", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 12), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=clear)
        button5.grid(row=0, column=4,padx=10)

        frame5 = Frame(self.frame, bg="#3A5FCD", padx=10, pady=10)
        frame5.grid(row=3, column=0, pady=5, padx=20)

        button = Button(frame5, text="Close", padx=15, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="crimson", bd=3,command=close)
        button.grid(row=0, column=0,padx=10)
    
    def active_buttons(self):
       global button4;global button6
       button4.configure(state=NORMAL);button6.configure(state=NORMAL) 


