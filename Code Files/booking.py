from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import messagebox
from dbcreatefile import idcreater
from user_profile import User_profile
import datetime
import customer_login

class Booking():

    def __init__(self,root,frame,username,password,name):
        self.root = root
        self.frame = frame
        self.username = username
        self.password = password
        self.name = name
        self.user = "Customer"

    def book_room(self):
        x = int((1520-720)/2)
        y = int((810-765)/2)
        self.root.geometry(f'720x765+{x}+{y}')
        self.root.minsize(720,765)
        self.root.maxsize(720,765)
        ######## button commands #########
        def back_to_profile():
            self.clear_widjects()
            customer_profile = User_profile(self.root,self.frame,self.user,self.username,self.password,self.name)
            customer_profile.run_profile()

        def paste_Id():
            connection = sqlite3.connect('hotelmanagement.db')
            cursor = connection.cursor()
            cursor.execute(f'select Room_ID,Room_No from clipboard where User_ID="{self.username}"')
            clipboard = cursor.fetchall()[0]
            if (clipboard[0] != ""):
                txt5.delete(0,END);txt8.delete(0,END)
                Id = clipboard[0];No = str(clipboard[1])
                txt5.insert(0,Id);txt8.insert(0,No)
            else:
                messagebox.showerror("Customer Booking","Clipboard is Empty")

        def search():
            if (len(txt5.get()) > 0):
                connection = sqlite3.connect("hotelmanagement.db")
                cursor = connection.cursor()
                cursor.execute(f'select Room_No from rooms where Room_ID="{txt5.get()}"')
                room = cursor.fetchall()
                if (len(room) == 1):
                    nodays = days.get()+months.get()*30
                    discount = self.get_discount(txt5.get(),meal.get(),nodays)
                    Tuple = self.get_total(txt5.get(),meal.get(),discount,hours.get(),nodays,adults.get(),childs2.get(),childs3.get())
                    txt6.delete(0,END);txt7.delete(0,END);txt9.delete(0,END);txt10.delete(0,END);txt8.delete(0,END)
                    txt6.insert(0,Tuple[0]);txt7.insert(0,Tuple[1]);txt9.insert(0,Tuple[2]);txt10.insert(0,Tuple[3]);txt8.insert(0,Tuple[4])
                    if (discount > 0):
                        messagebox.showinfo("Booking",f"Congratulations!!!\n{discount}% discount is offered")
                else:
                    messagebox.showerror("Booking","Please enter valid Room Id")
            else:
                messagebox.showerror("Booking","Please enter Room Id")

        def book():
            txtareas = [txt11,txt12,txt7]
            if (self.is_text_full(txtareas) and txt11.get() != "yyyy/mm/dd,time" and txt12.get() != "yyyy/mm/dd,time"):
                if (self.check_room(txt5.get(),adults.get(),childs3.get())):
                    if (self.check_format(txt11.get(),txt12.get())):
                        duration = (hours.get(),days.get()+months.get()*30,txt11.get(),txt12.get())
                        validation = self.is_valid_duration(duration)
                        if (validation[0]):
                            date = str(datetime.datetime.now())[:10]
                            booking_id = idcreater("bookingid")
                            discount = self.get_discount(txt5.get(),meal.get(),days.get())
                            booking_details = [(booking_id,date,customer_details[3],txt5.get(),hours.get(),days.get()+months.get()*30,childs1.get(),childs2.get(),childs3.get(),adults.get(),
                            meal.get(),txt13.get(),txt11.get(),txt12.get(),txt7.get(),discount,txt9.get(),txt10.get(),txt15.get())]
                            connection = sqlite3.connect("hotelmanagement.db")
                            cursor = connection.cursor()
                            cursor.execute('insert into bookings values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',*booking_details)
                            cursor.execute(f'update rooms set Availability="Booked" where Room_ID="{txt5.get()}"')
                            connection.commit()
                            connection.close()
                            messagebox.showinfo("Room Booking","Room Booking Successfull\nBooking ID: "+booking_id)
                            clear()
                        else:
                            top = Toplevel()
                            x = int((1520-510)/2)
                            y = int((810-280)/2)
                            top.geometry(f'510x280+{x}+{y}')
                            top.minsize(510,280)
                            top.maxsize(510,280)
                            infoframe = Frame(top,padx=20,pady=20)
                            infoframe.grid(row=0,column=0,pady=20,padx=20)

                            def infoclose():
                                top.destroy()
                            
                            def autocorrect():
                                hours.set(validation[1]);days.set(validation[2]);months.set(validation[3])

                            info = "Please check duration or checkin,checkout areas\n\nAccording to checkin,checkout duration should be\n\
Hours = {:2s} Days = {:2s} months = {:1s}\n\n\
Press correct to autocorrect duration".format(str(validation[1]),str(validation[2]),str(validation[3]))
                            infolabel = Label(infoframe,text=info,font=("Times New Roman",15),padx=10,pady=3,bg="darkturquoise",highlightthickness=2,anchor=CENTER)
                            infolabel.grid(row=0,column=0,pady=5,padx=5,columnspan=2)
                            infolabel.config(highlightbackground="#00868B",highlightcolor="#00868B")
                            buttonc = Button(infoframe, text="Close", padx=35, pady=0,
                                    font=("Cooper Black", 15), bg="#00BFFF",
                                    relief=RAISED, activebackground="crimson", bd=3,command=infoclose)
                            buttonc.grid(row=1, column=1,padx=5,pady=10)
                            buttona = Button(infoframe, text="Correct", padx=25, pady=0,
                                    font=("Cooper Black", 15), bg="#00BFFF",
                                    relief=RAISED, activebackground="crimson", bd=3,command=autocorrect)
                            buttona.grid(row=1, column=0,padx=5,pady=10)
                    else:
                        messagebox.showerror("Room Booking","Check checkin.checkout formats")
                        self.show_info()
                else:
                    messagebox.showerror("Room Booking","Room is not available\nor\nNot suitable for this no of guests")
            else:
                messagebox.showerror("Room Booking","Fill empty text areas")
        
        def clear():
            hours.set(0);days.set(0);months.set(0);childs1.set(0);childs2.set(0);childs3.set(0);meal.set(mealplans[0])
            txt11.delete(0,END);txt11.insert(0,"yy/mm/dd,time");txt12.delete(0,END);txt12.insert(0,"yy/mm/dd,time")
            txt13.delete(0,END);txt13.insert(0,"0");adults.set(0);txt15.delete(0,END)
            txt5.delete(0,END);txt6.delete(0,END);txt7.delete(0,END);txt8.delete(0,END);txt9.delete(0,END);txt10.delete(0,END)

        def auto_fill_price(c):
            mealplan = meal.get()
            connection = sqlite3.connect("hotelmanagement.db")
            cursor = connection.cursor()
            cursor.execute(f'select Price_for_one_to_one_customer from mealplans where Meal_Plan="{mealplan}"')
            price_for_one = cursor.fetchall()[0][0];NOC2 = childs2.get();NOC3 = childs3.get();NOA = adults.get()
            Additional_price = str(price_for_one*(NOC2/2+NOC3+NOA))
            txt13.delete(0,END);txt13.insert(0,Additional_price)
            connection.close()
        
        def close():
            response = messagebox.askyesno("Customer tasks","Do you want to close Booking?")
            if (response==True):
                self.clear_widjects()
                clogin = customer_login.Customer_login(self.root,self.frame,self.username,self.password,self.name)
                clogin.login()
        ########################################
        connection = sqlite3.connect("hotelmanagement.db")
        cursor = connection.cursor()
        cursor.execute(f'select First_Name,Last_Name,Contact_No,Customer_ID from customers where username="{self.username}"')
        customer_details = cursor.fetchall()[0]
        connection.close()

        label1 = Label(self.frame,text="Booking",font=("Cooper Black", 20),padx=30,pady=5,bg="#3A5FCD",bd=0)
        label1.grid(row=0,column=0,pady=0,padx=3,columnspan=2)

        frame1 = LabelFrame(self.frame,padx=10,pady=7,borderwidth=5)
        frame1.grid(row=2,column=0,columnspan=2,pady=10,padx=20)
        frame1.configure(bg="darkturquoise")

        label3 = Label(frame1,text="First Name",font=("Times New Roman",12),padx=20,pady=5,bg="darkturquoise",highlightthickness=2)
        label3.grid(row=2,column=0,pady=5)
        label3.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt1 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt1.grid(row=2,column=1);txt1.insert(0,customer_details[0])
        txt1.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black")

        label4 = Label(frame1,text="Last Name",font=("Times New Roman",12),padx=20,pady=5,bg="darkturquoise",highlightthickness=2)
        label4.grid(row=2,column=2,pady=5,padx=7)
        label4.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt2 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt2.grid(row=2,column=3);txt2.insert(0,customer_details[1])
        txt2.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black")

        label5 = Label(frame1,text="Contact No",font=("Times New Roman",12),padx=18,pady=5,bg="darkturquoise",highlightthickness=2)
        label5.grid(row=3,column=0,pady=5)
        label5.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt3 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt3.grid(row=3,column=1);txt3.insert(0,customer_details[2])
        txt3.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black")

        label6 = Label(frame1,text="Customer ID",font=("Times New Roman",12),padx=15,pady=5,bg="darkturquoise",highlightthickness=2)
        label6.grid(row=3,column=2,pady=5)
        label6.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt4 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt4.grid(row=3,column=3);txt4.insert(0,customer_details[3])
        txt4.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black")

        label7 = Label(self.frame,text="*If above details are not correct please >>>",bg="#3A5FCD",font=(7))
        label7.grid(row=4,column=0)
        button1 = Button(self.frame,text="Go To Profile",padx=0, pady=0,
                            font=("Berlin Sans FB Demi", 12), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",bd=3,command=back_to_profile)
        button1.grid(row=4,column=1)

        frame2 = LabelFrame(self.frame,padx=10,pady=10,borderwidth=5)
        frame2.grid(row=6,column=0,columnspan=2,pady=0,padx=20)
        frame2.configure(bg="darkturquoise")

        count = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

        label15 = Label(frame2,text="Duration",font=("Times New Roman",12),padx=33,pady=5,bg="darkturquoise",highlightthickness=2)
        label15.grid(row=0,column=0,pady=5)
        label15.config(highlightbackground="#00868B",highlightcolor="#00868B")

        hours = IntVar()
        hours.set(0)
        menubox1 = OptionMenu(frame2,hours,*count[:15])
        menubox1.grid(row=0,column=1)
        menubox1.config(width=3,bg="#79CDCD",activebackground="#79CDCD")
        label16 = Label(frame2,text="Hours",font=("Times New Roman",10),padx=0,pady=3,bg="darkturquoise")
        label16.grid(row=0,column=2)

        days = IntVar()
        days.set(0)
        menubox2 = OptionMenu(frame2,days,*count)
        menubox2.grid(row=0,column=3)
        menubox2.config(width=3,bg="#79CDCD",activebackground="#79CDCD")
        label17 = Label(frame2,text="Days",font=("Times New Roman",10),padx=0,pady=3,bg="darkturquoise")
        label17.grid(row=0,column=4)

        months = IntVar()
        months.set(0)
        menubox3 = OptionMenu(frame2,months,*count[:3])
        menubox3.grid(row=0,column=5)
        menubox3.config(width=3,bg="#79CDCD",activebackground="#79CDCD")
        label18 = Label(frame2,text="Months",font=("Times New Roman",10),padx=0,pady=3,bg="darkturquoise")
        label18.grid(row=0,column=6)

        label18 = Label(frame2,text="Check In",font=("Times New Roman",12),padx=31,pady=5,bg="darkturquoise",highlightthickness=2)
        label18.grid(row=1,column=0,pady=5)
        label18.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt11 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt11.grid(row=1,column=1,columnspan=2)
        txt11.insert(0,"yyyy/mm/dd,time")

        label19 = Label(frame2,text="Check Out",font=("Times New Roman",12),padx=30,pady=5,bg="darkturquoise",highlightthickness=2)
        label19.grid(row=1,column=3,pady=5,columnspan=2)
        label19.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt12 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt12.grid(row=1,column=5,columnspan=2)
        txt12.insert(0,"yyyy/mm/dd,time")

        label20 = Label(frame2,text="No of Childs",font=("Times New Roman",12),padx=20,pady=5,bg="darkturquoise",highlightthickness=2)
        label20.grid(row=2,column=0,pady=5)
        label20.config(highlightbackground="#00868B",highlightcolor="#00868B")

        childs1 = IntVar()
        childs1.set(0)
        menubox4 = OptionMenu(frame2,childs1,*count[:7])
        menubox4.grid(row=2,column=1)
        menubox4.config(width=3,bg="#79CDCD",activebackground="#79CDCD")
        label16 = Label(frame2,text="0<=Age<=6",font=("Times New Roman",10),padx=0,pady=3,bg="darkturquoise")
        label16.grid(row=2,column=2)

        childs2 = IntVar()
        childs2.set(0)
        menubox5 = OptionMenu(frame2,childs2,*count[:7],command=auto_fill_price)
        menubox5.grid(row=2,column=3)
        menubox5.config(width=3,bg="#79CDCD",activebackground="#79CDCD")
        label17 = Label(frame2,text="6<Age<=12",font=("Times New Roman",10),padx=0,pady=3,bg="darkturquoise")
        label17.grid(row=2,column=4)

        childs3 = IntVar()
        childs3.set(0)
        menubox6 = OptionMenu(frame2,childs3,*count[:7],command=auto_fill_price)
        menubox6.grid(row=2,column=5)
        menubox6.config(width=3,bg="#79CDCD",activebackground="#79CDCD")
        label18 = Label(frame2,text="12<Age",font=("Times New Roman",10),padx=0,pady=3,bg="darkturquoise")
        label18.grid(row=2,column=6)

        mealplans = ["Room Only","Breakfast Only","Lunch Only","Dinner Only","Breakfast & Lunch","Breakfast & Dinner","Lunch & Dinner","3 Meals"]
        label20 = Label(frame2,text="Mealplan",font=("Times New Roman",12),padx=30,pady=5,bg="darkturquoise",highlightthickness=2)
        label20.grid(row=3,column=0,pady=5)
        label20.config(highlightbackground="#00868B",highlightcolor="#00868B")
        meal = StringVar()
        meal.set(mealplans[0])
        menubox7 = OptionMenu(frame2,meal,*mealplans,command=auto_fill_price)
        menubox7.grid(row=3,column=1,columnspan=2)
        menubox7.config(width=19,bg="#79CDCD",activebackground="#79CDCD")

        label21 = Label(frame2,text="Additional Price",font=("Times New Roman",12),padx=15,pady=5,bg="darkturquoise",highlightthickness=2)
        label21.grid(row=3,column=3,columnspan=2,pady=5,padx=5)
        label21.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt13 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt13.grid(row=3,column=5,columnspan=2);txt13.insert(0,"0")

        label22 = Label(frame2,text="No of Adults",font=("Times New Roman",12),padx=20,pady=5,bg="darkturquoise",highlightthickness=2)
        label22.grid(row=4,column=0,pady=5)
        label22.config(highlightbackground="#00868B",highlightcolor="#00868B")
        adults = IntVar()
        adults.set(0)
        menubox8 = OptionMenu(frame2,adults,*count[:7],command=auto_fill_price)
        menubox8.grid(row=4,column=1,columnspan=2)
        menubox8.config(width=3,bg="#79CDCD",activebackground="#79CDCD")

        label23 = Label(frame2,text="Comments",font=("Times New Roman",12),padx=31,pady=5,bg="darkturquoise",highlightthickness=2)
        label23.grid(row=4,column=3,columnspan=2,pady=5)
        label23.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt15 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt15.grid(row=4,column=5,columnspan=2)

        frame3 = LabelFrame(self.frame,borderwidth=5,padx=5)
        frame3.grid(row=7,column=0,columnspan=2)
        frame3.configure(bg="darkturquoise")

        label9 = Label(frame3,text="Room ID",font=("Times New Roman",12),padx=22,pady=5,bg="darkturquoise",highlightthickness=2)
        label9.grid(row=0,column=0,pady=5)
        label9.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt5 = Entry(frame3, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt5.grid(row=0,column=1)
        button2 = Button(frame3,text="Paste ID",padx=0, pady=0,
                            font=("Berlin Sans FB Demi", 12), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",bd=3,command=paste_Id)
        button2.grid(row=0,column=2)
        label12 = Label(frame3,text="Room No",font=("Times New Roman",12),padx=20,pady=5,bg="darkturquoise",highlightthickness=2)
        label12.grid(row=1,column=0,pady=5)
        label12.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt8 = Entry(frame3, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt8.grid(row=1,column=1)
        button3 = Button(frame3,text="Search",padx=7, pady=0,
                            font=("Berlin Sans FB Demi", 12), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",bd=3,command=search)
        button3.grid(row=1,column=2)

        frame4 = LabelFrame(self.frame,padx=10,pady=10,borderwidth=5)
        frame4.grid(row=8,column=0,columnspan=2,pady=0,padx=20)
        frame4.configure(bg="darkturquoise")

        label10 = Label(frame4,text="Price",font=("Times New Roman",12),padx=31,pady=5,bg="darkturquoise",highlightthickness=2)
        label10.grid(row=0,column=0,pady=5)
        label10.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt6 = Entry(frame4, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt6.grid(row=0,column=1)

        label11 = Label(frame4,text="Total Price",font=("Times New Roman",12),padx=16,pady=5,bg="darkturquoise",highlightthickness=2)
        label11.grid(row=0,column=2,pady=5)
        label11.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt7 = Entry(frame4, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt7.grid(row=0,column=3)

        label13 = Label(frame4,text="Advance",font=("Times New Roman",12),padx=20,pady=5,bg="darkturquoise",highlightthickness=2)
        label13.grid(row=1,column=0,pady=5)
        label13.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt9 = Entry(frame4, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt9.grid(row=1,column=1)

        label14 = Label(frame4,text="Balance",font=("Times New Roman",12),padx=25,pady=5,bg="darkturquoise",highlightthickness=2)
        label14.grid(row=1,column=2,pady=5)
        label14.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt10 = Entry(frame4, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt10.grid(row=1,column=3)

        frame5 = LabelFrame(self.frame,padx=0,pady=0,borderwidth=0)
        frame5.grid(row=9,column=0,columnspan=2,pady=5,padx=0)
        frame5.configure(bg="#3A5FCD")

        button4 = Button(frame5,text="Book",padx=10, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",bd=3,command=book)
        button4.grid(row=0,column=0,pady=5,padx=30)
        button5 = Button(frame5,text="Clear",padx=10, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="crimson",bd=3,command=clear)
        button5.grid(row=0,column=1,pady=5,padx=30)
        button6 = Button(frame5,text="Close",padx=10, pady=0,
                      font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                      relief=RAISED, activebackground="crimson",bd=3,command=close)
        button6.grid(row=0,column=2,pady=5,padx=30)
        self.show_info()

        self.root.mainloop()
        
    def get_total(self,Room_Id,Meal_plan,discount,Hours=0,Days=0,NOA=0,NOC2=0,NOC3=0):
        connection = sqlite3.connect("hotelmanagement.db")
        cursor1 = connection.cursor()
        cursor1.execute(f'select Price_for_hour,Price_for_day,Up_to,Room_No from rooms where Room_ID="{Room_Id}"')
        Room_price = cursor1.fetchall()[0]
        cursor2 = connection.cursor()
        cursor2.execute(f'select Price_for_one_to_one_customer from mealplans where Meal_Plan="{Meal_plan}"')
        Meal_price = cursor2.fetchall()[0]
        connection.close()
        price_for_room = Hours*(NOA+NOC3+NOC2/2)*(Room_price[0]/Room_price[2]) + Days*(NOA+NOC3+NOC2/2)*(Room_price[1]/Room_price[2])
        price_for_meal = Meal_price[0]*(NOA+NOC3+NOC2/2)
        Total_price = int((price_for_room + price_for_meal)*(100-discount)/100) ; Advance = int(Total_price/4) ; Balance = Total_price - Advance
        return (Room_price[1],Total_price,Advance,Balance,Room_price[3])
    
    def clear_widjects(self):
        for widject in self.frame.winfo_children():
            widject.destroy()
    
    def is_text_full(self,List):
        for entry in List:
            x = len(entry.get())
            if (x==0):
                return False
        else:
            return True

    def show_info(self):
        top = Toplevel()
        x = int((1520-610)/2)
        y = int((810-300)/2)
        top.geometry(f'610x300+{x}+{y}')
        top.minsize(610,300)
        top.maxsize(610,300)
        infoframe = Frame(top,padx=20,pady=20)
        infoframe.grid(row=0,column=0,pady=20,padx=20)

        def infoclose():
            top.destroy()

        info = "Fill Checkin Checkout areas according to the following format\n\n\
            year/month/day,time\n\
            example:- 2022.07.29,6.30\n\n\
            always give the time in 24 hour format\n\
            example:- 2022.07.29,18.30\n"
        infolabel = Label(infoframe,text=info,font=("Times New Roman",15),padx=10,pady=3,bg="darkturquoise",highlightthickness=2,anchor=CENTER)
        infolabel.grid(row=0,column=0,pady=5,padx=5)
        infolabel.config(highlightbackground="#00868B",highlightcolor="#00868B")
        buttonc = Button(infoframe, text="Close", padx=35, pady=0,
                font=("Cooper Black", 15), bg="#00BFFF",
                relief=RAISED, activebackground="crimson", bd=3,command=infoclose)
        buttonc.grid(row=1, column=0,padx=5,pady=10)
    
    def is_valid_duration(self,Tuple):
        hours = Tuple[0];days = Tuple[1];checkin = Tuple[2];checkout = Tuple[3]
        checkindate = checkin.split(",")[0];checkintime = checkin.split(",")[1];inhour = checkintime.split('.')[0]
        checkoutdate = checkout.split(",")[0];checkouttime = checkout.split(",")[1];outhour = checkouttime.split('.')[0]
        inyear,inmonth,inday = checkindate.split("/");outyear,outmonth,outday = checkoutdate.split("/")
        dur1 = (((int(outyear)-int(inyear))*12+int(outmonth)-int(inmonth))*30+int(outday)-int(inday))*24+int(outhour)-int(inhour)
        dur2 = int(days)*24 + int(hours)
        if (dur1 == dur2):
            return True,
        else:
            correcthours = int(dur1%24);correctdays = int((dur1//24)%30) ;correctmonths = int((dur1//24)//30)
            return False,correcthours,correctdays,correctmonths

    def check_format(self,checkin,checkout):
        try:
            checkinlist =checkin.split(',');checkoutlist =checkout.split(',')
            if (len(checkinlist) , len(checkoutlist) == 2):
                indate = checkinlist[0].split('/');outdate = checkoutlist[0].split('/')
                intime = checkinlist[1].split('.');outtime = checkoutlist[1].split('.')
                if (len(indate),len(outdate) == 3 and len(intime),len(outtime) == 2):
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False

    def check_room(self,roomid,noc,noa):
        conn = sqlite3.connect('hotelmanagement.db')
        cursor = conn.cursor()
        cursor.execute(f'select Availability,Up_to from rooms where Room_ID="{roomid}"')
        details = cursor.fetchall()[0]
        conn.close()
        if (details[0] == "Available"):
            if (int(details[1] >= noc+noa)):
                return True
            else:
                return False
        else:
            return False

    def get_discount(self,roomid,mealplan,days):
        conn = sqlite3.connect('hotelmanagement.db')
        cursor = conn.cursor()
        cursor.execute(f'select Category from rooms where Room_ID="{roomid}"')
        cat = cursor.fetchall()[0][0]
        cursor.execute(f'select Mealplan,Minimum_days,Discount from discounts where Category="{cat}"')
        discounts = cursor.fetchall()
        conn.close()
        fil_discounts = []
        for conditions in discounts:
            if (conditions[0] == mealplan):
                fil_discounts.append(conditions)
        fil_discounts2 = []
        if (len(fil_discounts) > 0):
            for condition in fil_discounts:
                if (int(condition[1]) <= days):
                    fil_discounts2.append(condition)
            if (len(fil_discounts2) > 0):
                if (len(fil_discounts2) == 1):
                    return int(fil_discounts2[0][2])
                else:
                    l = []
                    for condition in fil_discounts2:
                        l.append(condition[2])
                    return int(max(l))
            else:
                return 0
        else:
            return 0

            
        
