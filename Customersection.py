from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox
from create_account import Account
from customer_login import Customer_login
from check_availability import Availability

class CustomerSection():

    def __init__(self,root,frame):
        self.root = root
        self.frame = frame
        self.user = "Customer"
        self.username = "Username"
        self.password = "Password"
        self.name = "Name"
    
    def run_customer(self):

        self.root.title("Royal Hotel")
        self.root.iconbitmap("hotel.ico")
        self.root.configure(bg="#3A5FCD")
        self.frame.configure(bg="#3A5FCD")
        x = int((1520-1300)/2)
        y = int((810-680)/2)
        self.root.geometry(f'1300x680+{x}+{y}')
        self.root.minsize(1300,680)
        self.root.maxsize(1300,680)
        check_available = False
        ###### button commands########
        def login():
            username = str(txt1.get()) ; self.username = username
            password = str(txt2.get()) ; self.password = password
            if (self.confirm_user(username,password)):
                self.clear_widjects()
                if (check_available):clipboard = available.get_clipboard()
                else:clipboard = {"Room ID":"","Room No":0}
                connection = sqlite3.connect('hotelmanagement.db')
                cursor = connection.cursor()
                cursor.execute(f'insert into clipboard values ("{self.username}","{clipboard["Room ID"]}",{clipboard["Room No"]})')
                connection.commit()
                connection.close()
                clogin = Customer_login(self.root,self.frame,self.username,self.password,self.name)
                clogin.login()
            else:
                messagebox.showerror(self.user + " Login Failed","Invalid username or password")

        def signup():
            self.clear_widjects()
            if (check_available):clipboard = available.get_clipboard()
            else:clipboard = {"Room ID":"","Room No":0}
            customer_account = Account(self.root,self.frame,self.user,clipboard)
            customer_account.run_account_creater()

        def check_availability():
            nonlocal check_available
            check_available = True
            top = Toplevel()
            mainframe = Frame(top)
            mainframe.grid(row=0,column=0)
            global available
            available = Availability(top,mainframe)
            available.is_available()
        
        def back():
            response = messagebox.askyesno("Customer tasks","Do you want to Go Back?")
            if (response==True):
                self.root.destroy()

        ##############################
        frame1 = LabelFrame(self.frame, padx=30, pady=10,borderwidth=5)
        frame1.grid(row=0, column=0, padx=25, pady=20)
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
        label2.grid(row=2, column=1, pady=20)

        txt1 = Entry(frame1, width=27, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 15))
        txt1.grid(row=3, column=0, columnspan=2)

        icon3 = ImageTk.PhotoImage(Image.open("password2.png"))
        img_lbl2 = Label(frame1, image=icon3, bg="darkturquoise")
        img_lbl2.grid(row=4, column=0)

        label3 = Label(frame1, text="Password", bg="darkturquoise",
                       font=("Berlin Sans FB Demi", 20))
        label3.grid(row=4, column=1, pady=20)

        txt2 = Entry(frame1, width=27, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 15),show="*")
        txt2.grid(row=5, column=0, columnspan=2)

        login_button = Button(frame1, text="LOGIN",
                              padx=57, pady=5,
                              font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                              relief=RAISED, activebackground="mediumspringgreen",command=login)#1
        login_button.grid(row=6, column=0, pady=10, columnspan=2)

        signup_button = Button(frame1, text="SIGN UP",
                               padx=50, pady=5,
                               font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                               relief=RAISED, activebackground="mediumspringgreen",command=signup)#2
        signup_button.grid(row=7, column=0, pady=5, columnspan=2)

        back_button = Button(frame1, text="BACK",
                               padx=50, pady=5,
                               font=("Berlin Sans FB Demi", 13), bg="#87CEFA",
                               relief=RAISED, activebackground="crimson",command=back)#3
        back_button.grid(row=8, column=0, pady=10, columnspan=2)

        frame2 = LabelFrame(self.frame, padx=10, pady=10,borderwidth=3)
        frame2.grid(row=0, column=1, padx=25, pady=20)
        frame2.configure(bg="darkturquoise")

        label = Label(frame2,text="Check availability without login or sign up >>>",font=(5),bg="darkturquoise")
        label.grid(row=0,column=0,sticky=W)

        button3 = Button(frame2, text="Check Availability",padx=60, pady=5,
                              font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                              relief=RAISED, activebackground="mediumspringgreen",command=check_availability)#3
        button3.grid(row=0, column=1,sticky=E)

        my_img2 = ImageTk.PhotoImage(Image.open("reception.jpg"))
        img_lbl4 = Label(frame2, image=my_img2, bg="darkturquoise")
        img_lbl4.grid(row=1, column=0, columnspan=2, pady=10)

        self.root.mainloop()


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


    
