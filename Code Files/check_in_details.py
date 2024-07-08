from tkinter import *
from tkinter import messagebox
import sqlite3
import admin_login
from dbcreatefile import idcreater

class Check_In_Details():

    def __init__(self,root,frame,username,password,name):
        self.root = root
        self.frame = frame
        self.username = username
        self.password = password
        self.name = name
    
    def show_details(self):
        x = int((1520-750)/2)
        y = int((810-765)/2)
        self.root.geometry(f'750x765+{x}+{y}')
        self.root.minsize(750,765)
        self.root.maxsize(750,765)
        global Continue_booking ; Continue_booking = False
        global Booking_No; Booking_No = ""
        global discount;discount = 0
        ########## Button commands #############
        def first_search():
            self.show_customer_details()

        def paste_Id():
            connection = sqlite3.connect('hotelmanagement.db')
            cursor = connection.cursor()
            cursor.execute(f'select Room_ID,Room_No from clipboard where User_ID="{self.username}"')
            clipboard = cursor.fetchall()[0]
            if (clipboard[0] != ""):
                txt5.delete(0,END);txt8.delete(0,END)
                Id = clipboard[0];No = clipboard[1]
                txt5.insert(0,Id);txt8.insert(0,No)
            else:
                messagebox.showerror("Customer Booking","Clipboard is Empty")

        def second_search():
            if (len(txt5.get()) > 0):
                connection = sqlite3.connect("hotelmanagement.db")
                cursor = connection.cursor()
                cursor.execute(f'select Room_No from rooms where Room_ID="{txt5.get()}"')
                room = cursor.fetchall()
                if (len(room) == 1):
                    global discount
                    nodays = days.get()+months.get()*30
                    discount = self.get_discount(txt5.get(),meal.get(),nodays)
                    Tuple = self.get_total(txt5.get(),meal.get(),discount,hours.get(),nodays,adults.get(),childs2.get(),childs3.get())
                    txt6.delete(0,END);txt7.delete(0,END);txt9.delete(0,END);txt10.delete(0,END);txt8.delete(0,END)
                    txt6.insert(0,Tuple[0]);txt7.insert(0,Tuple[1]);txt9.insert(0,Tuple[2]);txt10.insert(0,Tuple[3]);txt8.insert(0,Tuple[4])
                    if (discount > 0):
                        messagebox.showinfo("Booking",f"Congratulations!!!\n{discount}% discount is offered")
                else:
                    messagebox.showerror("Admin tasks","Please enter valid Room Id")
            else:
                messagebox.showerror("Admin tasks","Please enter Room Id")


        def checkin():
            txtareas = [txt1,txt2,txt3,txt4,txt11,txt12,txt6,txt7,txt8,txt9,txt10]
            if (self.is_text_full(txtareas) and txt11.get() != "yy/mm/dd,time" and txt12.get() != "yy/mm/dd,time"):
                global Continue_booking;global Booking_No
                if (Continue_booking):
                    booking_no = Booking_No
                else:
                    booking_no = idcreater("bookingid")
                booking_details = (txt.get(),booking_no,txt5.get(),hours.get(),days.get()+months.get()*30,childs1.get(),childs2.get(),childs3.get(),adults.get(),
                meal.get(),txt13.get(),txt11.get(),txt12.get(),txt7.get(),discount,txt9.get(),txt10.get(),txt15.get())
                conn = sqlite3.connect('hotelmanagement.db')
                cursor = conn.cursor()
                cursor.execute('insert into checkin values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',booking_details)
                cursor.execute(f'update rooms set Availability="Checkin" where Room_ID="{txt5.get()}"')
                if (Continue_booking):
                    cursor.execute(f'delete from bookings where Booking_No="{booking_no}"')
                messagebox.showinfo("Room Booking",f"Room Booking Successfull\nBooking ID={booking_no}")
                conn.commit()
                cursor.close()
                clear()
                button3.configure(state=DISABLED)
            else:
                messagebox.showerror("Admin tasks","Please fill all the text areas")


        def update():
            txtareas = [txt1,txt2,txt3,txt4,txt11,txt12,txt6,txt7,txt8,txt9,txt10]
            if (self.is_text_full(txtareas) and txt11.get() != "yy/mm/dd,time" and txt12.get() != "yy/mm/dd,time"):
                details = (hours.get(),days.get()+months.get()*30,childs1.get(),childs2.get(),childs3.get(),adults.get(),
                meal.get(),txt13.get(),txt11.get(),txt12.get(),txt7.get(),txt9.get(),txt10.get(),txt15.get(),txt5.get(),discount)
                conn = sqlite3.connect('hotelmanagement.db')
                cursor = conn.cursor()
                cursor.execute(f'update checkin set Room_ID="{details[14]}",Duration_by_hours="{details[0]}",Duration_by_days="{details[1]}",NOC_1="{details[2]}",NOC_2="{details[3]}",NOC_3="{details[4]}",NOA="{details[5]}",\
                    Mealplan="{details[6]}",Meal_Price="{details[7]}",Check_In="{details[8]}",Check_Out="{details[9]}",Total_Price="{details[10]}",Advance="{details[11]}",Balance="{details[12]}",Comments="{details[13]}",Discount="{details[15]}" where Customer_ID="{txt.get()}"')
                conn.commit()
                cursor.close()
                messagebox.showinfo("Admin tasks","Check in Updated successfully")
                clear()
                button4.configure(state=DISABLED)
            else:
                messagebox.showerror("Admin tasks","Please fill all the text areas")

        def delete():
            res = messagebox.askyesno("Admin tasks","Are you sure to delete booking")
            if (res == True):
                conn = sqlite3.connect('hotelmanagement.db')
                cursor = conn.cursor()
                cursor.execute(f'delete from bookings where Booking_No="{Booking_No}"')
                conn.commit()
                cursor.close()
                button5.configure(state=DISABLED)

        def clear():
            hours.set(0);days.set(0);months.set(0);childs1.set(0);childs2.set(0);childs3.set(0);meal.set(mealplans[0])
            txt11.delete(0,END);txt11.insert(0,"yy/mm/dd,time");txt12.delete(0,END);txt12.insert(0,"yy/mm/dd,time")
            txt13.delete(0,END);txt13.insert(0,"0");adults.set(0);txt15.delete(0,END)
            txt5.delete(0,END);txt6.delete(0,END);txt7.delete(0,END);txt8.delete(0,END);txt9.delete(0,END);txt10.delete(0,END)

        def auto_fill_price(e):
            mealplan = meal.get()
            connection = sqlite3.connect("hotelmanagement.db")
            cursor = connection.cursor()
            cursor.execute(f'select Price_for_one_to_one_customer from mealplans where Meal_Plan="{mealplan}"')
            price_for_one = cursor.fetchall()[0][0];NOC2 = childs2.get();NOC3 = childs3.get();NOA = adults.get()
            Additional_price = str(price_for_one*(NOC2/2+NOC3+NOA))
            txt13.delete(0,END);txt13.insert(0,Additional_price)
            connection.close()
        
        def close():
            response = messagebox.askyesno("Admin tasks","Do you want to close Checkin?")
            if (response==True):
                for widject in self.frame.winfo_children():
                    widject.destroy()
                alogin = admin_login.Admin_login(self.root,self.frame,self.username,self.password,self.name)
                alogin.login()
        ########################################
        global txt;global txt1;global txt2;global txt3;global txt4;global txt11;global txt12;global txt13;global adults;global txt15;global txt6;global txt7
        global txt5;global txt8;global txt9;global txt10;global hours;global days;global months;global childs1;global childs2;global childs3;global meal;global button5
        
        label1 = Label(self.frame,text="Check In Details",font=("Cooper Black", 20),padx=30,pady=5,bg="#3A5FCD",bd=0)
        label1.grid(row=0,column=0,pady=0,padx=3)

        frame = Frame(self.frame,bg="#3A5FCD")
        frame.grid(row=0,column=1,pady=5)

        label8 = Label(frame, text="Customer ID", font=("Times New Roman", 12),
                    padx=20, pady=5, bg="darkturquoise", highlightthickness=2)
        label8.grid(row=0, column=0, pady=5)
        label8.config(highlightbackground="#00868B", highlightcolor="#00868B")
        txt = Entry(frame, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt.grid(row=0, column=1, padx=5)
        button1 = Button(frame, text="Search", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 13), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=first_search)
        button1.grid(row=0, column=2)

        frame1 = LabelFrame(self.frame,padx=10,pady=7,borderwidth=5)
        frame1.grid(row=2,column=0,columnspan=2,pady=5,padx=20)
        frame1.configure(bg="darkturquoise")

        label3 = Label(frame1,text="First Name",font=("Times New Roman",12),padx=20,pady=5,bg="darkturquoise",highlightthickness=2)
        label3.grid(row=2,column=0,pady=5)
        label3.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt1 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt1.grid(row=2,column=1)

        label4 = Label(frame1,text="Last Name",font=("Times New Roman",12),padx=20,pady=5,bg="darkturquoise",highlightthickness=2)
        label4.grid(row=2,column=2,pady=5)
        label4.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt2 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt2.grid(row=2,column=3)

        label5 = Label(frame1,text="Contact No",font=("Times New Roman",12),padx=18,pady=5,bg="darkturquoise",highlightthickness=2)
        label5.grid(row=3,column=0,pady=5)
        label5.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt3 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt3.grid(row=3,column=1)

        label6 = Label(frame1,text="Customer ID",font=("Times New Roman",12),padx=15,pady=5,bg="darkturquoise",highlightthickness=2)
        label6.grid(row=3,column=2,pady=5)
        label6.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt4 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt4.grid(row=3,column=3)

        frame2 = LabelFrame(self.frame,padx=10,pady=10,borderwidth=5)
        frame2.grid(row=6,column=0,columnspan=2,pady=5,padx=20)
        frame2.configure(bg="darkturquoise")

        count = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

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
        txt11.insert(0,"yy/mm/dd,time")

        label19 = Label(frame2,text="Check Out",font=("Times New Roman",12),padx=30,pady=5,bg="darkturquoise",highlightthickness=2)
        label19.grid(row=1,column=3,pady=5,columnspan=2)
        label19.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt12 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt12.grid(row=1,column=5,columnspan=2)
        txt12.insert(0,"yy/mm/dd,time")

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
        label21.grid(row=3,column=3,columnspan=2,pady=5)
        label21.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt13 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt13.grid(row=3,column=5,columnspan=2)

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
        button7 = Button(frame3,text="Paste ID",padx=0, pady=0,
                            font=("Berlin Sans FB Demi", 12), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",bd=3,command=paste_Id)
        button7.grid(row=0,column=2)
        
        label12 = Label(frame3,text="Room No",font=("Times New Roman",12),padx=20,pady=5,bg="darkturquoise",highlightthickness=2)
        label12.grid(row=1,column=0,pady=5)
        label12.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt8 = Entry(frame3, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt8.grid(row=1,column=1)
        button2 = Button(frame3,text="Search",padx=7, pady=0,
                            font=("Berlin Sans FB Demi", 12), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",bd=3,command=second_search)
        button2.grid(row=1,column=2)

        frame4 = LabelFrame(self.frame,padx=10,pady=10,borderwidth=5)
        frame4.grid(row=8,column=0,columnspan=2,pady=0,padx=20)
        frame4.configure(bg="darkturquoise")

        label10 = Label(frame4,text="Price",font=("Times New Roman",12),padx=35,pady=5,bg="darkturquoise",highlightthickness=2)
        label10.grid(row=1,column=0,pady=5)
        label10.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt6 = Entry(frame4, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt6.grid(row=1,column=1)

        label11 = Label(frame4,text="Total Price",font=("Times New Roman",12),padx=16,pady=5,bg="darkturquoise",highlightthickness=2)
        label11.grid(row=1,column=2,pady=5)
        label11.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt7 = Entry(frame4, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt7.grid(row=1,column=3)

        label13 = Label(frame4,text="Advance",font=("Times New Roman",12),padx=25,pady=5,bg="darkturquoise",highlightthickness=2)
        label13.grid(row=2,column=0,pady=5)
        label13.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt9 = Entry(frame4, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt9.grid(row=2,column=1)

        label14 = Label(frame4,text="Balance",font=("Times New Roman",12),padx=25,pady=5,bg="darkturquoise",highlightthickness=2)
        label14.grid(row=2,column=2,pady=5)
        label14.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt10 = Entry(frame4, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt10.grid(row=2,column=3)

        frame5 = LabelFrame(self.frame,padx=0,pady=0,borderwidth=0)
        frame5.grid(row=9,column=0,columnspan=2,pady=15,padx=0)
        frame5.configure(bg="#3A5FCD")
        global button3;global button4
        button3 = Button(frame5, text="Check In", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=checkin,state=DISABLED)
        button3.grid(row=0, column=0,padx=30)
        button4 = Button(frame5, text="Update", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=update,state=DISABLED)
        button4.grid(row=0, column=1,padx=30)
        button5 = Button(frame5, text="Delete", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="crimson", bd=3,command=delete,state=DISABLED)
        button5.grid(row=0, column=2,padx=30)
        button6 = Button(frame5, text="Clear", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=clear)
        button6.grid(row=0, column=3,padx=30)
        button7 = Button(frame5, text="Close", padx=15, pady=0,
                 font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                 relief=RAISED, activebackground="crimson", bd=3,command=close)
        button7.grid(row=0, column=4,padx=30,pady=10)

        self.root.mainloop()

    def show_customer_details(self):
        global txt;global txt1;global txt2;global txt3;global txt4;global txt11;global txt12;global txt13;global adults;global txt15;global txt6;global txt7
        global txt5;global txt8;global txt9;global txt10;global hours;global days;global months;global childs1;global childs2;global childs3;global meal;global button5

        if (len(txt.get()) > 0):
            connection = sqlite3.connect("hotelmanagement.db")
            cursor = connection.cursor()
            cursor.execute(f'select First_Name,Last_Name,Contact_No from customers where Customer_ID="{txt.get()}"')
            customer_details = cursor.fetchall()
            if (len(customer_details) > 0):
                cursor.execute(f'select Room_ID from bookings where Customer_ID="{txt.get()}"')
                t = cursor.fetchall();test = []
                if (len(t) > 0):test = t[0]
                cursor.execute(f'select Room_ID from checkin where Customer_ID="{txt.get()}"')
                t2 = cursor.fetchall();test2 = []
                if (len(t2) > 0):test2 = t2[0]

                if (len(test) == 0 and len(test2) == 0):#come to checkin without a booking or previous checkin
                    global button3
                    cursor.execute(f'select First_Name,Last_Name,Contact_No from customers where Customer_ID="{txt.get()}"')
                    customer_details = cursor.fetchall()[0]
                    txt1.delete(0,END);txt2.delete(0,END);txt3.delete(0,END);txt4.delete(0,END)
                    txt1.insert(0,customer_details[0]);txt2.insert(0,customer_details[1]);txt3.insert(0,customer_details[2]);txt4.insert(0,txt.get())
                    txt1.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black");txt2.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black")
                    txt3.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black");txt4.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black")
                    button3.configure(state=NORMAL)
                else:
                    if (len(test) > 0 and len(test2) > 0):
                        messagebox.showerror("Admin tasks","Oops!!!\nCan not do anything for this Customer")
                    elif (len(test) > 0):#have a previous booking
                        response = messagebox.askyesno("Admin tasks","Does customer want to continue\nwith his booking?")
                        cursor.execute(f'select First_Name,Last_Name,Contact_No from customers where Customer_ID="{txt.get()}"')
                        customer_details = cursor.fetchall()[0]
                        txt1.delete(0,END);txt2.delete(0,END);txt3.delete(0,END);txt4.delete(0,END)
                        txt1.insert(0,customer_details[0]);txt2.insert(0,customer_details[1]);txt3.insert(0,customer_details[2]);txt4.insert(0,txt.get())
                        txt1.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black");txt2.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black")
                        txt3.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black");txt4.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black")
                        if (response == True):#to continue with previous booking
                            global Continue_booking ; Continue_booking = True;global Booking_No;global discount
                            cursor.execute(f'select Booking_No,Duration_by_hours,Duration_by_days,NOC_1,NOC_2,NOC_3,NOA,Check_In,Check_Out,Mealplan,Meal_Price,\
                            Total_Price,Advance,Balance,Comment,Room_ID,Discount from bookings where Customer_ID="{txt.get()}"')
                            bookings_details = cursor.fetchall()[0]
                            discount = bookings_details[16]
                            hours.set(bookings_details[1]);txt11.delete(0,END);txt12.delete(0,END)
                            days.set(bookings_details[2]%30);months.set(bookings_details[2]//30);childs1.set(bookings_details[3]);childs2.set(bookings_details[4])
                            childs3.set(bookings_details[5]);adults.set(int(bookings_details[6]));txt11.insert(0,bookings_details[7]);txt12.insert(0,bookings_details[8])
                            meal.set(bookings_details[9]);txt13.insert(0,bookings_details[10]);txt7.insert(0,bookings_details[11]);txt9.insert(0,bookings_details[12])
                            txt10.insert(0,bookings_details[13]);txt15.insert(0,bookings_details[14]);txt5.insert(0,bookings_details[15])
                            Booking_No = bookings_details[0]
                            button5.configure(state=NORMAL)
                            button3.configure(state=NORMAL)
                        else:# only checkin
                            cursor.execute(f'select First_Name,Last_Name,Contact_No from customers where Customer_ID="{txt.get()}"')
                            customer_details = cursor.fetchall()[0]
                            txt1.delete(0,END);txt2.delete(0,END);txt3.delete(0,END);txt4.delete(0,END)
                            txt1.insert(0,customer_details[0]);txt2.insert(0,customer_details[1]);txt3.insert(0,customer_details[2]);txt4.insert(0,txt.get())
                            txt1.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black");txt2.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black")
                            txt3.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black");txt4.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black")
                            button3.configure(state=NORMAL)
                    elif (len(test2) > 0):#have a previous checkin
                        response2 = messagebox.askyesno("Admin tasks","Does customer want to continue\nwith his previous checkin?")
                        if (response2 == True):#want to update checkin
                            global button4
                            cursor.execute(f'select First_Name,Last_Name,Contact_No from customers where Customer_ID="{txt.get()}"')
                            customer_details = cursor.fetchall()[0]
                            txt1.delete(0,END);txt2.delete(0,END);txt3.delete(0,END);txt4.delete(0,END)
                            txt1.insert(0,customer_details[0]);txt2.insert(0,customer_details[1]);txt3.insert(0,customer_details[2]);txt4.insert(0,txt.get())
                            txt1.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black");txt2.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black")
                            txt3.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black");txt4.configure(state=DISABLED,disabledbackground="#79CDCD",disabledforeground="black")
                            cursor.execute(f'select Booking_No,Duration_by_hours,Duration_by_days,NOC_1,NOC_2,NOC_3,NOA,Check_In,Check_Out,Mealplan,Meal_Price,\
                                Total_Price,Advance,Balance,Comments,Room_ID,Discount from checkin where Customer_ID="{txt.get()}"')
                            bookings_details = cursor.fetchall()[0]
                            discount = bookings_details[16]
                            hours.set(bookings_details[1]);txt11.delete(0,END);txt12.delete(0,END)
                            days.set(bookings_details[2]%30);months.set(bookings_details[2]//30);childs1.set(bookings_details[3]);childs2.set(bookings_details[4])
                            childs3.set(bookings_details[5]);adults.set(int(bookings_details[6]));txt11.insert(0,bookings_details[7]);txt12.insert(0,bookings_details[8])
                            meal.set(bookings_details[9]);txt13.insert(0,bookings_details[10]);txt7.insert(0,bookings_details[11]);txt9.insert(0,bookings_details[12])
                            txt10.insert(0,bookings_details[13]);txt15.insert(0,bookings_details[14]);txt5.insert(0,bookings_details[15])
                            button4.configure(state=NORMAL)
                        else:#new checkin
                            messagebox.showerror("Admin tasks","Customer can not checkin twice")
                    else:
                        pass
                connection.close()
            else:
                messagebox.showerror("Admin tasks","Please enter valid Customer ID")
        else:
            messagebox.showerror("Admin tasks","Please enter Customer ID")
    
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
    
    def is_text_full(self,List):# can know whether entry boxes are full or not by giving there variable in a list as a parameter
        for entry in List:
            x = len(entry.get())
            if (x==0):
                return False
        else:
            return True
    
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
        if (len(fil_discounts) == 0):
            return 0
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
            return 
    
    