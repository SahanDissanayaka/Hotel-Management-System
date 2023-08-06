from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox
import customer_login
from dbcreatefile import idcreater
import Customersection

class Account():

    def __init__(self,root,frame,user,clipboard={}):
        self.root = root
        self.frame = frame
        self.user = user
        self.name = "Name"
        self.clipboard = clipboard
        self.username = "Username"
        self.password = "password"
        

    def run_account_creater(self):
        self.root.title("Royal Hotel ")
        self.root.iconbitmap("hotel.ico")
        self.root.configure(bg="#3A5FCD")
        x = int((1520-710)/2)
        y = int((810-730)/2)
        self.root.geometry(f'710x730+{x}+{y}')
        self.root.minsize(710,730)
        self.root.maxsize(710,730)
        ####### button command #########
        def create_account():
            txtareas = [txt,txt1,txt2,txt3,txt4,txt6,txt7,txt8,txt9,txt10,txt11]
            if (self.is_text_full(txtareas) and selected.get() != "Select"):
                if(txt10.get() == txt11.get()):
                    self.username = txt9.get() ; self.password = txt10.get()
                    if (self.user == "Customer"):new_id = idcreater("customerid")
                    else:new_id = idcreater("adminid")
                    lines = txtbox.get("1.0","end-1c").split("\n");address = ""
                    while ("" in lines):
                        lines.remove("")
                    for line in lines:
                        address += line + " "
                    details = [(new_id,txt.get(),txt1.get(),txt2.get(),address,selected.get(),txt3.get(),txt4.get(),txt6.get(),
                    txt8.get(),txt9.get(),txt10.get(),txt7.get())]
                    connection = sqlite3.connect("hotelmanagement.db")
                    cursor = connection.cursor()
                    cursor.execute(f'insert into {self.user}s values(?,?,?,?,?,?,?,?,?,?,?,?,?)',*details)
                    connection.commit()
                    connection.close()
                    messagebox.showinfo(self.user+" Registation","Successfully Registed \n"+self.user+"ID: "+new_id)
                    if (self.user == "Customer"):self.check_user_again()
                else:
                    messagebox.showerror(self.user+" Registation Failed","Please check password again")
            else:
                messagebox.showerror(self.user+" Registation Failed","Fill required text areas")
        
        def close():
            
            if (self.user == "Customer"):
                response = messagebox.askyesno("Customer tasks","Do you want to close?")
                if (response==True):
                    for widject in self.frame.winfo_children():
                        widject.destroy()
                    customer = Customersection.CustomerSection(self.root,self.frame)
                customer.run_customer()
            else:
                response = messagebox.askyesno("Admin tasks","Do you want to close?")
                if (response==True):
                    for widject in self.frame.winfo_children():
                        widject.destroy()
                    self.root.destroy()
        
        def check_username():
            if (len(txt9.get()) > 0):
                if (len(txt9.get()) >= 5):
                    conn = sqlite3.connect('hotelmanagement.db')
                    cursor = conn.cursor()
                    cursor.execute(f'select Customer_ID from {self.user}s where username="{txt9.get()}"')
                    d = cursor.fetchall()
                    conn.close()

                    if (len(d) == 0):
                        messagebox.showinfo("User Registration","You are good to go!!!")
                        show_info()
                        button4.configure(state=NORMAL)
                        txt9.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black")
                        button3.configure(state=DISABLED)

                    else:
                        messagebox.showerror("User Registration","This username is not available")

                else:
                    messagebox.showerror("User Registration","Username should have minimum 5 characters")

            else:
                messagebox.showerror("User Registration","Please enter a username")

        def check_password():
            if (len(txt10.get()) > 0):
                if (len(txt10.get()) >= 8):
                    if (is_valid_password(txt10.get())):
                        messagebox.showinfo("User Registration","You are good to go!!!")
                        button.configure(state=NORMAL)
                        txt10.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black")
                        button4.configure(state=DISABLED);button5.configure(state=NORMAL)
                    else:
                        messagebox.showerror("User Registration","Please enter a valid password")
                        show_info()

                else:
                    messagebox.showerror("User Registration","Username should have minimum 8 characters") 

            else:
                messagebox.showerror("User Registration","Please enter a password")
        
        def is_valid_password(password):
            valid = 1
            for char in password:
                if (char.isdigit()):
                    valid *= 2
                    break
            for char in password:
                if (char.isupper()):
                    valid *= 2
                    break
            for char in password:
                if (char.islower()):
                    valid *= 2
                    break
            for char in password:
                if (char == "!" or char == "@" or char == "*" or char == "#"):
                    valid *= 2
                    break
            if (valid >= 8):
                return True
            else:
                return False
        
        def show_info():
            top = Toplevel()
            x = int((1520-560)/2)
            y = int((810-260)/2)
            top.geometry(f'560x260+{x}+{y}')
            top.minsize(560,260)
            top.maxsize(560,260)
            infoframe = Frame(top,padx=20,pady=20)
            infoframe.grid(row=0,column=0,pady=20,padx=20)

            def infoclose():
                top.destroy()

            info = "Password should include at least 3 from below options\n\
                    1.At least one Simple letter                         \n\
                    2.At least one Capital letter                        \n\
                    3.At least one number                                 \n\
                    4.At least one symbol (@,#,!,*)                  \n"
            infolabel = Label(infoframe,text=info,font=("Times New Roman",15),padx=10,pady=3,bg="darkturquoise",highlightthickness=2,anchor=W)
            infolabel.grid(row=0,column=0,pady=5,padx=5)
            infolabel.config(highlightbackground="#00868B",highlightcolor="#00868B")
            buttonc = Button(infoframe, text="Close", padx=35, pady=0,
                    font=("Cooper Black", 15), bg="#00BFFF",
                    relief=RAISED, activebackground="crimson", bd=3,command=infoclose)
            buttonc.grid(row=1, column=0,padx=5,pady=10)
        
        def reset():
            button3.configure(state=NORMAL);button.configure(state=DISABLED)
            txt10.configure(state=NORMAL);txt9.configure(state=NORMAL)
            button5.configure(state=DISABLED)

        ################################
        frame = Frame(self.frame,bg="#00BFFF")
        frame.grid(row=0,column=0,pady=5,columnspan=2)
        label1 = Label(frame,text="Create a new profile",font=("Cooper Black", 20),padx=10,pady=10,bg="#3A5FCD",bd=0)
        label1.grid(row=0,column=0,pady=3,padx=3)

        label2 = Label(self.frame,text="Fill Your Details",font=("Berlin Sans FB Demi", 15),bg="#3A5FCD")
        label2.grid(row=1,column=0,sticky=W,padx=10)

        frame1 = LabelFrame(self.frame,padx=10,pady=10,borderwidth=5)
        frame1.grid(row=2,column=0,pady=10,padx=20,columnspan=2)
        frame1.configure(bg="darkturquoise")

        label = Label(frame1,text="Title",font=("Times New Roman",12),padx=41,pady=3,bg="darkturquoise",highlightthickness=2)
        label.grid(row=1,column=0,pady=5,padx=5)
        label.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt.grid(row=1,column=1)

        label3 = Label(frame1,text="First Name",font=("Times New Roman",12),padx=20,pady=5,bg="darkturquoise",highlightthickness=2)
        label3.grid(row=2,column=0,pady=5)
        label3.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt1 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt1.grid(row=2,column=1)

        label4 = Label(frame1,text="Last Name",font=("Times New Roman",12),padx=20,pady=5,bg="darkturquoise",highlightthickness=2)
        label4.grid(row=2,column=2,pady=5,padx=7)
        label4.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt2 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt2.grid(row=2,column=3)

        label5 = Label(frame1,text="Date of Birth",font=("Times New Roman",12),padx=15,pady=5,bg="darkturquoise",highlightthickness=2)
        label5.grid(row=3,column=0,pady=5)
        label5.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt3 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt3.grid(row=3,column=1)

        label6 = Label(frame1,text="ID No",font=("Times New Roman",12),padx=35,pady=5,bg="darkturquoise",highlightthickness=2)
        label6.grid(row=3,column=2,pady=5)
        label6.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt4 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt4.grid(row=3,column=3)

        selected = StringVar()
        selected.set("Select")
        label7 = Label(frame1,text="Gender",font=("Times New Roman",12),padx=31,pady=5,bg="darkturquoise",highlightthickness=2)
        label7.grid(row=4,column=0,pady=5)
        label7.config(highlightbackground="#00868B",highlightcolor="#00868B")
        menubox = OptionMenu(frame1,selected,"Male","Female")
        menubox.grid(row=4,column=1)
        menubox.config(width=20,bg="#79CDCD",activebackground="#79CDCD")

        label7 = Label(frame1,text="Address",font=("Times New Roman",12),padx=29,pady=5,bg="darkturquoise",highlightthickness=2)
        label7.grid(row=4,column=2,pady=5)
        label7.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txtbox = Text(frame1,width=21,height=4,bg="#79CDCD",font=("Times New Roman", 13))
        txtbox.grid(row=4,column=3,rowspan=2)

        label8 = Label(frame1,text="Nationality",font=("Times New Roman",12),padx=21,pady=5,bg="darkturquoise",highlightthickness=2)
        label8.grid(row=5,column=0,pady=5)
        label8.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt6 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt6.grid(row=5,column=1)

        label9 = Label(frame1,text="Contact No",font=("Times New Roman",12),padx=20,pady=5,bg="darkturquoise",highlightthickness=2)
        label9.grid(row=6,column=2,pady=5)
        label9.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt7 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt7.grid(row=6,column=3)

        label10 = Label(frame1,text="Email Address",font=("Times New Roman",12),padx=10,pady=5,bg="darkturquoise",highlightthickness=2)
        label10.grid(row=6,column=0,pady=5)
        label10.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt8 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt8.grid(row=6,column=1)

        label11 = Label(self.frame,text="Give username and password ",font=("Berlin Sans FB Demi", 15),bg="#3A5FCD")
        label11.grid(row=3,column=0,sticky=W,padx=10)

        frame2 = LabelFrame(self.frame,padx=10,pady=10,borderwidth=5)
        frame2.grid(row=4,column=0,sticky=W,pady=10,padx=20,columnspan=2)
        frame2.configure(bg="darkturquoise")

        label12 = Label(frame2,text="Username",font=("Times New Roman",12),padx=35,pady=5,bg="darkturquoise",highlightthickness=2)
        label12.grid(row=0,column=0,pady=5,padx=5)
        label12.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt9 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt9.grid(row=0,column=1)
        button3 = Button(frame2,text="Check Username",font=("Cooper Black", 13),bg="#00BFFF",relief=RAISED,
                        activebackground="mediumspringgreen",command=check_username)
        button3.grid(row=0,column=2)

        label13 = Label(frame2,text="Password",font=("Times New Roman",12),padx=35,pady=5,bg="darkturquoise",highlightthickness=2)
        label13.grid(row=1,column=0,pady=5)
        label13.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt10 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt10.grid(row=1,column=1)
        button4 = Button(frame2,text="Check Password",font=("Cooper Black", 13),bg="#00BFFF",relief=RAISED,
                        activebackground="mediumspringgreen",command=check_password,state=DISABLED)
        button4.grid(row=1,column=2)

        label12 = Label(frame2,text="Confirm Password",font=("Times New Roman",12),padx=9,pady=5,bg="darkturquoise",highlightthickness=2)
        label12.grid(row=2,column=0,pady=5)
        label12.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt11 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt11.grid(row=2,column=1)
        button5 = Button(frame2,text="Reset",font=("Cooper Black", 13),bg="#00BFFF",relief=RAISED,
                        activebackground="mediumspringgreen",command=reset,state=DISABLED)
        button5.grid(row=2,column=2)

        button = Button(self.frame,text="Create Account",font=("Cooper Black", 15),bg="#00BFFF",relief=RAISED,
                        activebackground="mediumspringgreen",command=create_account,state=DISABLED)
        button.grid(row=6,column=0)
        button1 = Button(self.frame, text="Close", padx=35, pady=0,
                 font=("Cooper Black", 15), bg="#00BFFF",
                 relief=RAISED, activebackground="crimson", bd=3,command=close)
        button1.grid(row=6, column=1,padx=30,pady=10)

        self.root.mainloop()
    
    def check_user_again(self):
        self.clear_widjects()
        self.root.geometry('420x670')
        self.root.minsize(420,670)
        self.root.maxsize(420,670)
        ###### button command #####
        def login():
            username = str(txt1.get()) ; self.username = username
            password = str(txt2.get()) ; self.password = password
            if (self.confirm_user(username,password)):
                self.clear_widjects()
                connection = sqlite3.connect('hotelmanagement.db')
                cursor = connection.cursor()
                cursor.execute(f'insert into clipboard values ("{self.username}","{self.clipboard["Room ID"]}",{self.clipboard["Room No"]})')
                connection.commit()
                connection.close()
                clogin = customer_login.Customer_login(self.root,self.frame,self.username,self.password,self.name)
                clogin.login()
            else:
                messagebox.showerror(self.user + " Login Failed","Invalid username or password")
        def close():
            self.clear_widjects()
            customer = Customersection.CustomerSection(self.root,self.frame)
            customer.run_customer()
            
        ###########################
        frame1 = LabelFrame(self.frame, padx=30, pady=10,borderwidth=5)
        frame1.grid(row=0, column=0, padx=25, pady=30)
        frame1.configure(bg="darkturquoise")

        icon1 = ImageTk.PhotoImage(Image.open("hotel2.png"))
        img_lbl1 = Label(frame1, image=icon1, bg="darkturquoise")
        img_lbl1.grid(row=0, column=0)

        label1 = Label(frame1, text= self.user + " LOGIN",
                    bg="darkturquoise", font=("Cooper Black", 20))
        label1.grid(row=0, column=1, padx=10)

        my_img = ImageTk.PhotoImage(Image.open("hotellogo2.jpg"))
        img_lbl3 = Label(frame1, image=my_img, bg="darkturquoise")
        img_lbl3.grid(row=1, column=0, columnspan=2, pady=10)

        icon2 = ImageTk.PhotoImage(Image.open("user2.png"))
        img_lbl2 = Label(frame1, image=icon2, bg="darkturquoise")
        img_lbl2.grid(row=2, column=0)

        label2 = Label(frame1, text="Username", bg="darkturquoise",
                    font=("Berlin Sans FB Demi", 20))
        label2.grid(row=2, column=1, pady=30)

        txt1 = Entry(frame1, width=27, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 15))
        txt1.grid(row=3, column=0, columnspan=2)

        icon3 = ImageTk.PhotoImage(Image.open("password2.png"))
        img_lbl2 = Label(frame1, image=icon3, bg="darkturquoise")
        img_lbl2.grid(row=4, column=0)

        label3 = Label(frame1, text="Password", bg="darkturquoise",
                    font=("Berlin Sans FB Demi", 20))
        label3.grid(row=4, column=1, pady=30)

        txt2 = Entry(frame1, width=27, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 15),show="*")
        txt2.grid(row=5, column=0, columnspan=2)

        login_button = Button(frame1, text="LOGIN",
                            padx=57, pady=5,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=login)
        login_button.grid(row=6, column=0, pady=10, columnspan=2)

        close_button = Button(frame1, text="CLOSE",
                            padx=59, pady=5,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="crimson",command=close)
        close_button.grid(row=7, column=0, pady=10, columnspan=2)

        self.root.mainloop()
    
    def is_text_full(self,List):# can know whether entry boxes are full or not by giving there variable in a list as a parameter
        for entry in List:
            x = len(entry.get())
            if (x==0):
                return False
        else:
            return True
    
    def clear_widjects(self):
        for widject in self.frame.winfo_children():
            widject.destroy()
    
    def confirm_user(self,username,password):
        try:
            connection = sqlite3.connect("hotelmanagement.db")
            cursor = connection.cursor()
            cursor.execute(f'select password,First_Name from {self.user}s where username="{username}"')
            detail = cursor.fetchall()
            self.name = detail[0][1]
            connection.close()
            if (detail[0][0] == password):
                return True
            else:
                return False
        except IndexError:
            return False
    
    def idcreater(self,type):
        connection = sqlite3.connect("hotelmanagement.db")
        cursor = connection.cursor()
        cursor.execute(f'select id from idcreate where type="{type}"')
        Id = cursor.fetchall()[0][0]
        right_num = int(Id[2:])
        if (right_num == 999999):
            left_num = int(Id[0])
            new_id = str(left_num+1) + Id[1] + "0000001"
        else:
            new_id = Id[:2] + str(right_num+1).zfill(6)
        cursor.execute(f'update idcreate set id="{new_id}" where type="{type}"')
        connection.commit()
        connection.close()
        return Id
    