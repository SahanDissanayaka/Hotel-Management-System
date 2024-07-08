from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import datetime
import sqlite3
from customer_details import Customer_details
from room_details import Room_details
from check_out_details import Check_out_details
from check_in_details import Check_In_Details
from reports import Reports
from mealplans import Advancedmealplan
from discounts import Advanceddiscounts
import create_account
import user_profile

class Admin_login():

    def __init__(self,root,frame,username,password,name):
        self.root = root
        self.frame = frame 
        self.user = "Admin"
        self.username = username
        self.password = password
        self.name = name
    
    def login(self):
        time = datetime.datetime.now()
        x = int((1520-1165)/2)
        y = int((810-700)/2)
        self.root.geometry(f'1165x700+{x}+{y}')
        self.root.minsize(1165,700)
        self.root.maxsize(1165,700)
        ####### button commands ##############
        def profile():
            self.clear_widjects()
            admin_profile = user_profile.User_profile(self.root,self.frame,self.user,self.username,self.password,self.name)
            admin_profile.run_profile()

        def customers():
            self.clear_widjects()
            customer_detail = Customer_details(self.root,self.frame,self.username,self.password,self.name)
            customer_detail.show()

        def rooms():
            self.clear_widjects()
            room_detail = Room_details(self.root,self.frame,self.username,self.password,self.name)
            room_detail.show()
        
        def check_in():
            self.clear_widjects()
            checkin = Check_In_Details(self.root,self.frame,self.username,self.password,self.name)
            checkin.show_details()

        def check_out():
            self.clear_widjects()
            checkout = Check_out_details(self.root,self.frame,self.username,self.password,self.name)
            checkout.show_details()

        def reports():
            self.clear_widjects()
            rep = Reports(self.root,self.frame,"cid",self.username,self.password,self.name)
            rep.check_bookings()
        
        def show_more():
            global my_img3
            for widject in frame3.winfo_children():
                widject.destroy()
            img = Image.open("image1.jpg")
            reimg = img.resize((600,385))
            my_img3 = ImageTk.PhotoImage(reimg)
            img_lbl5 = Label(frame3, image=my_img3, bg="darkturquoise")
            img_lbl5.grid(row=1, column=0,columnspan=3, pady=25)
            ###########################################################
            def add_admin():
                top = Toplevel()
                frame = Frame(top,bg="#3A5FCD")
                frame.grid(row=0,column=0)
                acc = create_account.Account(top,frame,"Admin")
                acc.run_account_creater()

            def show_meals():
                top = Toplevel()
                frame = Frame(top)
                frame.grid(row=0,column=0)
                meal = Advancedmealplan(top,frame)
                meal.show_mealplans()

            def show_discounts():
                top = Toplevel()
                frame = Frame(top)
                frame.grid(row=0,column=0)
                discount = Advanceddiscounts(top,frame)
                discount.show_discounts()

            def back():
                global my_img2
                for widject in frame3.winfo_children():
                    widject.destroy()
                my_img2 = ImageTk.PhotoImage(Image.open("image1.jpg"))
                img_lbl3 = Label(frame3, image=my_img2, bg="darkturquoise")
                img_lbl3.grid(row=4, column=0, pady=5)
                mor_button.configure(text="More Tasks",padx=69,command=show_more)
            
            ###########################################################
            add_button = Button(frame3, text="Add Admin",padx=50, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=add_admin)
            add_button.grid(row=2, column=0,pady=20,padx=20)

            mel_button = Button(frame3, text="Meal Plans",padx=50, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=show_meals)
            mel_button.grid(row=2, column=1,pady=15,padx=20)

            dis_button = Button(frame3, text="Discounts",padx=50, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=show_discounts)
            dis_button.grid(row=2, column=2,pady=15,padx=20)

            mor_button.configure(text="Back",padx=97,command=back)
        
        def signout():
            response = messagebox.askyesno("Admin tasks","Do you want to close Sign Out?")
            if (response==True):
                connection = sqlite3.connect('hotelmanagement.db')
                cursor = connection.cursor()
                cursor.execute(f'delete from clipboard where User_ID="{self.username}"')
                connection.commit()
                connection.close()
                self.root.destroy()
        ###############################################
        frame1 = LabelFrame(self.frame, padx=20, pady=8,borderwidth=5)
        frame1.grid(row=0, column=0, padx=15, pady=20)
        frame1.configure(bg="darkturquoise")

        icon1 = ImageTk.PhotoImage(Image.open("hotel2.png"))
        img_lbl1 = Label(frame1, image=icon1, bg="darkturquoise")
        img_lbl1.grid(row=0, column=0,pady=10)

        label1 = Label(frame1, text="Admin Tasks",
                    bg="darkturquoise", font=("Cooper Black", 20),pady=0)
        label1.grid(row=0, column=1, padx=10,pady=10)

        my_img = ImageTk.PhotoImage(Image.open("hotellogo2.jpg"))
        img_lbl2 = Label(frame1, image=my_img, bg="darkturquoise")
        img_lbl2.grid(row=1, column=0, columnspan=2, pady=5)

        prof_button = Button(frame1, text="Profile",padx=90, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=profile)
        prof_button.grid(row=2, column=0,columnspan=2,pady=7)

        cust_button = Button(frame1, text="Customers",padx=74, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=customers)
        cust_button.grid(row=3, column=0,columnspan=2,pady=7)

        in_button = Button(frame1, text="Check In",padx=82, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=check_in)
        in_button.grid(row=4, column=0,columnspan=2,pady=7)

        out_button = Button(frame1, text="Check Out",padx=73, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=check_out)
        out_button.grid(row=5, column=0,columnspan=2,pady=7)

        room_button = Button(frame1, text="Rooms",padx=90, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=rooms)
        room_button.grid(row=6, column=0,columnspan=2,pady=7)

        rep_button = Button(frame1, text="Reports",padx=84, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=reports)
        rep_button.grid(row=7, column=0,columnspan=2,pady=7)

        mor_button = Button(frame1, text="More Tasks",padx=69, pady=0,
                      font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                      relief=RAISED, activebackground="mediumspringgreen",command=show_more)
        mor_button.grid(row=8, column=0,columnspan=2,pady=7)

        close_button = Button(frame1, text="Sign OUT",
                            padx=45, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="crimson",command=signout)
        close_button.grid(row=9, column=0, pady=10, columnspan=2)

        frame2 = LabelFrame(self.frame, padx=15, pady=5,borderwidth=5)
        frame2.grid(row=0, column=1, padx=15, pady=20)
        frame2.configure(bg="darkturquoise")

        label2 = Label(frame2,text="Welcome "+ self.name,font=("Cooper Black", 25),padx=20,bg="darkturquoise")
        label2.grid(row=0,column=0,padx=20,pady=5,sticky=W,columnspan=2)

        label3 = Label(frame2,text=""+str(time)[:-7],font=("Times New Roman",15),padx=10,pady=5, bg="#87CEFA")
        label3.grid(row=0,column=2,padx=10,sticky=E)
        #############################################
        connection = sqlite3.connect('hotelmanagement.db')
        cursor = connection.cursor()
        cursor.execute('select Customer_ID from customers')
        Ids = cursor.fetchall();NOC = len(Ids)
        cursor.execute('select Room_ID from rooms where Availability="Available"')
        RIds = cursor.fetchall();NOAR = len(RIds)
        cursor.execute('select Check_In from checkin')
        checkins = cursor.fetchall()
        count = 0
        for checkin in checkins:
            checkin_list = checkin[0].split(',')[0].split('/')
            today_list = str(time)[:10].split('-')
            if (checkin_list == today_list):
                count += 1
        connection.close()
        #############################################
        label4 = Label(frame2,text=f"Today's Check IN\n({count})",font=("Times New Roman",15),padx=30,pady=5,bg="darkturquoise",highlightthickness=2)
        label4.grid(row=1,column=0,pady=5,padx=5)
        label4.config(highlightbackground="#00868B",highlightcolor="#00868B")

        label5 = Label(frame2,text=f"Num of Customers\n({NOC})",font=("Times New Roman",15),padx=30,pady=5,bg="darkturquoise",highlightthickness=2)
        label5.grid(row=1,column=1,pady=5,padx=5)
        label5.config(highlightbackground="#00868B",highlightcolor="#00868B")

        label6 = Label(frame2,text=f"Available Rooms\n({NOAR})",font=("Times New Roman",15),padx=30,pady=5,bg="darkturquoise",highlightthickness=2)
        label6.grid(row=1,column=2,pady=5,padx=5)
        label6.config(highlightbackground="#00868B",highlightcolor="#00868B")

        frame3 = Frame(frame2,bg="darkturquoise")
        frame3.grid(row=4,column=0,columnspan=3)
        my_img2 = ImageTk.PhotoImage(Image.open("image1.jpg"))
        img_lbl3 = Label(frame3, image=my_img2, bg="darkturquoise")
        img_lbl3.grid(row=4, column=0, columnspan=3, pady=5)

        self.root.mainloop()

    def clear_widjects(self):
        for widject in self.frame.winfo_children():
            widject.destroy()

