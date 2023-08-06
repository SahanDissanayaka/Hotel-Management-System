import datetime
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3
from check_availability import Smartavailability
from user_profile import User_profile
from booking import Booking
from room_category import Room_category
from my_bookings import My_bookings
from mealplans import Mealplan
from discounts import Discounts

class Customer_login():
    
    def __init__(self,root,frame,username,password,name):
        self.root = root
        self.frame = frame
        self.username = username
        self.password = password
        self.name = name
        self.user = "Customer"

    def login(self):
        time = datetime.datetime.now()
        x = int((1520-1170)/2)
        y = int((810-735)/2)
        self.root.geometry(f'1170x735+{x}+{y}')
        self.root.minsize(1170,735)
        self.root.maxsize(1170,735)
        ####### button commands ########
        def profile():
            self.clear_widjects()
            customer_profile = User_profile(self.root,self.frame,self.user,self.username,self.password,self.name)
            customer_profile.run_profile()

        def book():
            self.clear_widjects()
            cbooking = Booking(self.root,self.frame,self.username,self.password,self.name)
            cbooking.book_room()

        def see_categories():
            top = Toplevel(bg="#3A5FCD")
            mainframe = Frame(top)
            mainframe.grid(row=0,column=0)
            rcategory = Room_category(top,mainframe)
            rcategory.run()
        
        def see_my_bookings():
            top = Toplevel()
            mainframe = Frame(top)
            mainframe.grid(row=0,column=0)
            customer_id = self.get_customer_id()
            booking = My_bookings(top,mainframe,customer_id)
            booking.check_bookings()
        
        def search():
            txtareas = [txt1,txt2,txt3,txt4]
            if (self.is_text_full(txtareas) and txt1.get() != "yyyy/mm/dd,time" and txt3.get() != "yyyy/mm/dd,time" and txt1.get() != "Age > 12"):
                details = [txt1.get(),txt2.get(),txt3.get(),txt4.get()]
                top = Toplevel()
                frame = Frame(top)
                frame.grid(row=0,column=0)
                sc = Smartavailability(top,frame)
                sc.is_available(details)
            else:
                messagebox.showerror("Customer tasks","Please fill text areas")
        
        def show_meals():
            top = Toplevel()
            frame = Frame(top)
            frame.grid(row=0,column=0)
            meal = Mealplan(top,frame)
            meal.show_mealplans()

        def show_discounts():
            top = Toplevel()
            frame = Frame(top)
            frame.grid(row=0,column=0)
            discount = Discounts(top,frame)
            discount.show_discounts()
        
        def signout():
            response = messagebox.askyesno("Customer tasks","Do you want to Sign Out?")
            if (response==True):
                connection = sqlite3.connect('hotelmanagement.db')
                cursor = connection.cursor()
                cursor.execute(f'delete from clipboard where User_ID="{self.username}"')
                connection.commit()
                connection.close()
                self.root.destroy()
        #################################
        frame1 = LabelFrame(self.frame, padx=10, pady=10,borderwidth=5)
        frame1.grid(row=0, column=0, padx=10, pady=15)
        frame1.configure(bg="darkturquoise")

        icon1 = ImageTk.PhotoImage(Image.open("hotel2.png"))
        img_lbl1 = Label(frame1, image=icon1, bg="darkturquoise")
        img_lbl1.grid(row=0, column=0,pady=10)

        label1 = Label(frame1, text="Customer Tasks",
                    bg="darkturquoise", font=("Cooper Black", 20))
        label1.grid(row=0, column=1, padx=10)

        my_img = ImageTk.PhotoImage(Image.open("hotellogo2.jpg"))
        img_lbl2 = Label(frame1, image=my_img, bg="darkturquoise")
        img_lbl2.grid(row=1, column=0, columnspan=2, pady=5)

        prof_button = Button(frame1, text="Profile",padx=90, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=profile)
        prof_button.grid(row=2, column=0,columnspan=2,pady=7)

        room_button = Button(frame1, text="Book a Room",padx=60, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=book)
        room_button.grid(row=3, column=0,columnspan=2,pady=7)

        detail_button = Button(frame1, text="Booking Details",padx=50, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=see_my_bookings)
        detail_button.grid(row=4, column=0,columnspan=2,pady=7)

        category_button = Button(frame1, text="Room Categories",padx=44, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=see_categories)
        category_button.grid(row=5, column=0,columnspan=2,pady=7)

        meal_button = Button(frame1, text="Meal Plans",padx=71, pady=0,
                      font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                      relief=RAISED, activebackground="mediumspringgreen",command=show_meals)
        meal_button.grid(row=6, column=0,columnspan=2,pady=7)

        dis_button = Button(frame1, text="Available Discounts",padx=33, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=show_discounts)
        dis_button.grid(row=7, column=0,columnspan=2,pady=7)

        fakelbl = Label(frame1,bg="darkturquoise")
        fakelbl.grid(row=8,column=0,pady=36)

        close_button = Button(frame1, text="Sign OUT",
                            padx=45, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="crimson",command=signout)
        close_button.grid(row=9, column=0, pady=10, columnspan=2)

        frame2 = LabelFrame(self.frame, padx=20, pady=5,borderwidth=5)
        frame2.grid(row=0, column=1, padx=15, pady=15)
        frame2.configure(bg="darkturquoise")

        label2 = Label(frame2,text="Welcome "+ self.name,font=("Cooper Black", 25),padx=0,bg="darkturquoise",anchor=W)
        label2.grid(row=0,column=0,padx=20,pady=5,sticky=W,columnspan=3)

        label3 = Label(frame2,text=""+str(time)[:-7],font=("Times New Roman",12),padx=10,pady=5, bg="#87CEFA")
        label3.grid(row=0,column=3,padx=10,sticky=E)

        label4 = Label(frame2,text="Check IN",font=("Times New Roman",12),padx=48,pady=3,bg="darkturquoise",highlightthickness=2)
        label4.grid(row=1,column=0,pady=1,padx=5)
        label4.config(highlightbackground="#00868B",highlightcolor="#00868B")

        txt1 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt1.grid(row=1,column=1);txt1.insert(0,"yyyy/mm/dd,time")

        label5 = Label(frame2,text="Num of Adults",font=("Times New Roman",12),padx=41,pady=3,bg="darkturquoise",highlightthickness=2)
        label5.grid(row=1,column=2,pady=1,padx=5)
        label5.config(highlightbackground="#00868B",highlightcolor="#00868B")

        txt2 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt2.grid(row=1,column=3)

        label6 = Label(frame2,text="Check OUT",font=("Times New Roman",12),padx=41,pady=3,bg="darkturquoise",highlightthickness=2)
        label6.grid(row=2,column=0,pady=1,padx=5)
        label6.config(highlightbackground="#00868B",highlightcolor="#00868B")

        txt3 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt3.grid(row=2,column=1);txt3.insert(0,"yyyy/mm/dd,time")

        label7 = Label(frame2,text="Num of childs",font=("Times New Roman",12),padx=44,pady=3,bg="darkturquoise",highlightthickness=2)
        label7.grid(row=2,column=2,pady=1,padx=5)
        label7.config(highlightbackground="#00868B",highlightcolor="#00868B")

        txt4 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt4.grid(row=2,column=3);txt4.insert(0,"Age > 12")

        button3 = Button(frame2, text="Search",padx=40, pady=4,
                            font=("Berlin Sans FB Demi", 13), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=search)
        button3.grid(row=3, column=0,pady=5)

        my_img2 = ImageTk.PhotoImage(Image.open("image1.jpg"))
        img_lbl3 = Label(frame2, image=my_img2, bg="darkturquoise")
        img_lbl3.grid(row=4, column=0, columnspan=4, pady=5)


        self.root.mainloop()

    def clear_widjects(self):
        for widject in self.frame.winfo_children():
            widject.destroy()
    
    def get_customer_id(self):
        connection = sqlite3.connect('hotelmanagement.db')
        cursor = connection.cursor()
        cursor.execute(f'select Customer_ID from customers where username="{self.username}" and password="{self.password}"')
        ID = cursor.fetchall()[0][0]
        connection.close()
        return ID
    
    def is_text_full(self,List):
        for entry in List:
            x = len(entry.get())
            if (x==0):
                return False
        else:
            return True
    