from tkinter import *
from PIL import ImageTk,Image
from dbcreatefile import idcreater
from digital_bill import Bill
import datetime
import sqlite3
from tkinter import messagebox
import admin_login

class Check_out_details():

    def __init__(self,root,frame,username,password,name):
        self.root = root
        self.frame = frame
        self.username = username
        self.password = password
        self.name = name

    def show_details(self):
        x = int((1520-1000)/2)
        y = int((810-740)/2)
        self.root.geometry(f'1000x740+{x}+{y}')
        self.root.minsize(1000,740)
        self.root.maxsize(1000,740)
        ########### Button Commands ########
        def search():
            if (len(txt.get()) > 0):
                connection = sqlite3.connect("hotelmanagement.db")
                cursor = connection.cursor()
                cursor.execute(f'select Customer_ID,Room_ID,Check_In,Check_Out,Total_Price,Advance,Balance\
                     from checkin where Booking_No="{txt.get()}"')
                detail = cursor.fetchall()
                if (len(detail) > 0):
                    details = detail[0]
                    global contact_no
                    cursor.execute(f'select First_Name,Last_Name,Contact_No from customers where Customer_ID="{details[0]}"')
                    customer_details = cursor.fetchall()[0]
                    contact_no = customer_details[2]
                    cursor.execute(f'select Room_No from rooms where Room_ID="{details[1]}"')
                    room_no = cursor.fetchall()[0][0]
                    txt1.insert(0,customer_details[0]);txt2.insert(0,customer_details[1]);txt3.insert(0,room_no);txt4.insert(0,details[2]);txt5.insert(0,details[3])
                    txt6.insert(0,details[4]);txt7.insert(0,details[5]);txt8.insert(0,details[6])
                    button2.configure(state=NORMAL);button3.configure(state=NORMAL);button4.configure(state=NORMAL)
                else:
                    messagebox.showerror("Admin tasks","Please enter valid booking number")
                connection.close()
            else:
                messagebox.showerror("Admin tasks","Please enter booking number")

        def check_out():
            connection = sqlite3.connect("hotelmanagement.db")
            cursor = connection.cursor()
            cursor.execute(f'select * from checkin where Booking_No="{txt.get()}"')
            check_out_details = cursor.fetchall()[0]
            cursor.execute('insert into checkout values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',check_out_details)
            cursor.execute(f'delete from checkin where Booking_No="{txt.get()}"')
            cursor.execute(f'update rooms set Availability="Available" where Room_No="{txt3.get()}"')
            connection.commit()
            connection.close()
            txt.delete(0,END);txt1.delete(0,END);txt2.delete(0,END);txt3.delete(0,END);txt4.delete(0,END);txt5.delete(0,END)
            txt6.delete(0,END);txt7.delete(0,END);txt8.delete(0,END)
            button2.configure(state=DISABLED)

        def Print():
            button3.configure(text="Back",command=back)
            for w in frame3.winfo_children():
                w.destroy()
            date = str(datetime.datetime.now())[:10]
            detaillist = [txt1.get(),txt2.get(),contact_no,txt4.get(),txt5.get(),txt3.get(),txt6.get()]
            invoice_no = idcreater('invoiceno')
            bill = Bill(self.root,frame3,0,0,invoice_no,date,detaillist)
            bill.show()

        def cancel():
            response = messagebox.askyesno("Admin tasks","Do you want to cancel booking?")
            if (response==True):
                connection = sqlite3.connect("hotelmanagement.db")
                cursor = connection.cursor()
                cursor.execute(f'delete from checkin where Booking_No="{txt.get()}"')
                cursor.execute(f'update rooms set Availability="Available" where Room_No="{txt3.get()}"')
                connection.commit()
                connection.close()
                messagebox.showinfo("Admin tasks","Successfully canceled booking")
            txt.delete(0,END);txt1.delete(0,END);txt2.delete(0,END);txt3.delete(0,END);txt4.delete(0,END);txt5.delete(0,END)
            txt6.delete(0,END);txt7.delete(0,END);txt8.delete(0,END)
            button4.configure(state=DISABLED)
        
        def close():
            response = messagebox.askyesno("Admin tasks","Do you want to close Checkout?")
            if (response==True):
                for widject in self.frame.winfo_children():
                    widject.destroy()
                alogin = admin_login.Admin_login(self.root,self.frame,self.username,self.password,self.name)
                alogin.login()
        
        def back():
            for w in frame3.winfo_children():
                w.destroy()
            fake_lbl = Label(frame3,text="Click Print\nTo\nGet Digital Bill",font=("Cooper Black", 20),bg="darkturquoise",width=29,height=17)
            fake_lbl.grid(row=0,column=0)
            button3.configure(text="Print",command=Print)

        ####################################
        label1 = Label(self.frame,text="Check Out Details",font=("Cooper Black", 20),padx=30,pady=5,bg="#3A5FCD",bd=0)
        label1.grid(row=0,column=0,pady=0,padx=3)

        frame1 = Frame(self.frame,bg="#3A5FCD")
        frame1.grid(row=0,column=1,pady=5)

        label2 = Label(frame1, text="Booking No", font=("Times New Roman", 12),
                    padx=20, pady=5, bg="darkturquoise", highlightthickness=2)
        label2.grid(row=0, column=0, pady=5)
        label2.config(highlightbackground="#00868B", highlightcolor="#00868B")
        txt = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt.grid(row=0, column=1, padx=5)
        button1 = Button(frame1, text="Search", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 13), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=search)
        button1.grid(row=0, column=2)

        frame2 = Label(self.frame,bg="darkturquoise",padx=20,pady=10)
        frame2.grid(row=1,column=0,pady=10,padx=20)

        label3 = Label(frame2,text="First Name",font=("Times New Roman",12),padx=30,pady=5,bg="darkturquoise",highlightthickness=2)
        label3.grid(row=0,column=0,pady=10)
        label3.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt1 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt1.grid(row=0,column=1,padx=10)

        label4 = Label(frame2,text="Last Name",font=("Times New Roman",12),padx=30,pady=5,bg="darkturquoise",highlightthickness=2)
        label4.grid(row=1,column=0,pady=10,padx=7)
        label4.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt2 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt2.grid(row=1,column=1)

        label5 = Label(frame2,text="Room No",font=("Times New Roman",12),padx=33,pady=5,bg="darkturquoise",highlightthickness=2)
        label5.grid(row=2,column=0,pady=10)
        label5.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt3 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt3.grid(row=2,column=1)

        label6 = Label(frame2,text="Check In",font=("Times New Roman",12),padx=35,pady=5,bg="darkturquoise",highlightthickness=2)
        label6.grid(row=3,column=0,pady=10,padx=5)
        label6.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt4 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt4.grid(row=3,column=1)

        label7 = Label(frame2,text="Check Out",font=("Times New Roman",12),padx=30,pady=5,bg="darkturquoise",highlightthickness=2)
        label7.grid(row=4,column=0,pady=10,padx=5)
        label7.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt5 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt5.grid(row=4,column=1)

        label8 = Label(frame2,text="Total Price",font=("Times New Roman",12),padx=31,pady=5,bg="darkturquoise",highlightthickness=2)
        label8.grid(row=5,column=0,pady=10,padx=5)
        label8.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt6 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt6.grid(row=5,column=1)

        label9 = Label(frame2,text="Advance",font=("Times New Roman",12),padx=37,pady=5,bg="darkturquoise",highlightthickness=2)
        label9.grid(row=6,column=0,pady=10,padx=5)
        label9.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt7 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt7.grid(row=6,column=1)

        label10 = Label(frame2,text="Balance",font=("Times New Roman",12),padx=40,pady=5,bg="darkturquoise",highlightthickness=2)
        label10.grid(row=7,column=0,pady=10,padx=5)
        label10.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt8 = Entry(frame2, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt8.grid(row=7,column=1)

        frame3 = Frame(self.frame,padx=5,pady=5)
        frame3.grid(row=1,column=1,pady=10)
        #############################################
        frame3.configure(bg="darkturquoise")
        fake_lbl = Label(frame3,text="Click Print\nTo\nGet Digital Bill",font=("Cooper Black", 20),bg="darkturquoise",width=29,height=17)
        fake_lbl.grid(row=0,column=0)
        #############################################
        frame9 = LabelFrame(self.frame,padx=0,pady=0,borderwidth=0)
        frame9.grid(row=9,column=0,columnspan=2,pady=15,padx=0)
        frame9.configure(bg="#3A5FCD")

        button2 = Button(frame9, text="Check Out", padx=10, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=check_out,state=DISABLED)
        button2.grid(row=0, column=1,padx=40)
        button3 = Button(frame9, text="Print", padx=15, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=Print,state=DISABLED)
        button3.grid(row=0, column=2,padx=40)
        button4 = Button(frame9, text="Cancel Booking", padx=5, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="crimson", bd=3,command=cancel,state=DISABLED)
        button4.grid(row=0, column=3,padx=40)
        button7 = Button(frame9, text="Close", padx=15, pady=0,
                 font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                 relief=RAISED, activebackground="crimson", bd=3,command=close)
        button7.grid(row=0, column=4,padx=50,pady=10)

        self.root.mainloop()
