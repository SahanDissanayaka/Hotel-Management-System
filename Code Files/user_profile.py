from tkinter import *
from PIL import ImageTk,Image
import datetime
import sqlite3
from tkinter import messagebox
import customer_login
import admin_login

class User_profile():

    def __init__(self,root,frame,user,username,password,name):
        self.root = root
        self.frame = frame
        self.user = user
        self.username = username
        self.password = password
        self.name = name
    
    def run_profile(self):
        time = datetime.datetime.now()
        x = int((1520-1100)/2)
        y = int((810-700)/2)
        self.root.geometry(f'1100x700+{x}+{y}')
        self.root.minsize(1100,700)
        self.root.maxsize(1100,700)
        details = self.get_details()
        ####### button commands ######
        def edit():
            top = Toplevel()
            mainframe = Frame(top)
            mainframe.grid(row=0,column=0)
            self.edit_profile(top,mainframe)

        def change_pwd():
            top = Toplevel()
            mainframe = Frame(top)
            mainframe.grid(row=0,column=0)
            self.change_pwd(top,mainframe)
        
        def refresh():
            details = self.get_details()
            lines = details[6].split(" ")
            if ("" in lines):lines.remove("")
            address1=""
            for line in lines:
                address1 += line + "\n"
            label19.configure(text=details[0]);label18.configure(text=details[1]);label17.configure(text=details[2]);label16.configure(text=details[3])
            label15.configure(text=details[4]);label14.configure(text=details[5]);label13.configure(text=address1);label12.configure(text=details[7])
            label11.configure(text=details[8]);label21.configure(text=details[9])
        
        def close():
            if (self.user == "Customer"):
                response = messagebox.askyesno("Customer tasks","Do you want to close Profile?")
                if (response==True):
                    self.clear_widjects()
                    clogin = customer_login.Customer_login(self.root,self.frame,self.username,self.password,self.name)
                    clogin.login()
            else:
                response = messagebox.askyesno("Admin tasks","Do you want to close Profile?")
                if (response==True):
                    self.clear_widjects()
                    alogin = admin_login.Admin_login(self.root,self.frame,self.username,self.password,self.name)
                    alogin.login()
        ##############################
        frame1 = LabelFrame(self.frame, padx=10, pady=10,borderwidth=5)
        frame1.grid(row=0, column=0, padx=10, pady=20)
        frame1.configure(bg="darkturquoise")

        icon1 = ImageTk.PhotoImage(Image.open("hotel2.png"))
        img_lbl1 = Label(frame1, image=icon1, bg="darkturquoise")
        img_lbl1.grid(row=0, column=0,pady=10)

        label1 = Label(frame1, text= self.user +" Profile",
                    bg="darkturquoise", font=("Cooper Black", 20))
        label1.grid(row=0, column=1, padx=10)

        my_img = ImageTk.PhotoImage(Image.open("hotellogo2.jpg"))
        img_lbl2 = Label(frame1, image=my_img, bg="darkturquoise")
        img_lbl2.grid(row=1, column=0, columnspan=2, pady=5)

        edit_button = Button(frame1, text="Edit Details",padx=68, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=edit)
        edit_button.grid(row=3, column=0,columnspan=2,pady=10)

        pwd_button = Button(frame1, text="Change Password",padx=40, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=change_pwd)
        pwd_button.grid(row=4, column=0,columnspan=2,pady=10)

        ref_button = Button(frame1, text="Refresh Profile",padx=53, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="mediumspringgreen",command=refresh)
        ref_button.grid(row=5, column=0,columnspan=2,pady=10)

        fakelbl = Label(frame1,bg="darkturquoise")
        fakelbl.grid(row=6,column=0,pady=61)

        close_button = Button(frame1, text="Cancel",
                            padx=45, pady=0,
                            font=("Berlin Sans FB Demi", 15), bg="#87CEFA",
                            relief=RAISED, activebackground="crimson",command=close)
        close_button.grid(row=7, column=0, pady=10, columnspan=2)

        frame2 = LabelFrame(self.frame, padx=5, pady=2,borderwidth=5)
        frame2.grid(row=0, column=1, padx=15, pady=20)
        frame2.configure(bg="darkturquoise")

        label2 = Label(frame2,text="Welcome "+ self.name,font=("Cooper Black", 25),padx=20,bg="darkturquoise")
        label2.grid(row=0,column=0,padx=20,pady=3,sticky=W)

        label3 = Label(frame2,text=""+str(time)[:-7],font=("Times New Roman",12),padx=10,pady=5, bg="#87CEFA")
        label3.grid(row=0,column=1,padx=10,sticky=E)

        frame4 = LabelFrame(frame2, padx=20, pady=20,bd=0)
        frame4.grid(row=1, column=0, padx=15, pady=5,columnspan=2)
        frame4.configure(bg="#87CEFA")

        my_img2 = ImageTk.PhotoImage(Image.open("profile2.jpg"))
        label20 = Label(frame4,image=my_img2,bg="#87CEFA")
        label20.grid(row=0,column=0)

        frame3 = LabelFrame(frame2,padx=10,pady=10,borderwidth=5)
        frame3.grid(row=2,column=0,pady=10,padx=20,columnspan=2)
        frame3.configure(bg="darkturquoise")

        label = Label(frame3,text="Title",font=("Times New Roman",12),padx=41,pady=3,bg="darkturquoise",highlightthickness=2)
        label.grid(row=1,column=0,pady=3,padx=5)
        label.config(highlightbackground="#00868B",highlightcolor="#00868B")
        label19 = Label(frame3,text=details[0],font=("Times New Roman",12),width=20,bg="darkturquoise")
        label19.grid(row=1,column=1,pady=3)

        label3 = Label(frame3,text="First Name",font=("Times New Roman",12),padx=20,pady=5,bg="darkturquoise",highlightthickness=2)
        label3.grid(row=2,column=0,pady=3)
        label3.config(highlightbackground="#00868B",highlightcolor="#00868B")
        label18 = Label(frame3,text=details[1],font=("Times New Roman",12),width=20,bg="darkturquoise")
        label18.grid(row=2,column=1,pady=3)

        label4 = Label(frame3,text="Last Name",font=("Times New Roman",12),padx=24,pady=5,bg="darkturquoise",highlightthickness=2)
        label4.grid(row=2,column=2,pady=3,padx=7)
        label4.config(highlightbackground="#00868B",highlightcolor="#00868B")
        label17 = Label(frame3,text=details[2],font=("Times New Roman",12),width=20,bg="darkturquoise")
        label17.grid(row=2,column=3,pady=3)

        label5 = Label(frame3,text="Date of Birth",font=("Times New Roman",12),padx=15,pady=5,bg="darkturquoise",highlightthickness=2)
        label5.grid(row=3,column=0,pady=3)
        label5.config(highlightbackground="#00868B",highlightcolor="#00868B")
        label16 = Label(frame3,text=details[3],font=("Times New Roman",12),width=20,bg="darkturquoise")
        label16.grid(row=3,column=1,pady=3)

        label6 = Label(frame3,text="ID No",font=("Times New Roman",12),padx=37,pady=5,bg="darkturquoise",highlightthickness=2)
        label6.grid(row=3,column=2,pady=3)
        label6.config(highlightbackground="#00868B",highlightcolor="#00868B")
        label15 = Label(frame3,text=str(details[4]),font=("Times New Roman",12),width=20,bg="darkturquoise")
        label15.grid(row=3,column=3,pady=3)

        label7 = Label(frame3,text="Gender",font=("Times New Roman",12),padx=31,pady=5,bg="darkturquoise",highlightthickness=2)
        label7.grid(row=4,column=0,pady=3)
        label7.config(highlightbackground="#00868B",highlightcolor="#00868B")
        label14 = Label(frame3,text=details[5],font=("Times New Roman",12),width=20,bg="darkturquoise")
        label14.grid(row=4,column=1,pady=3)

        label7 = Label(frame3,text="Address",font=("Times New Roman",12),padx=31,pady=5,bg="darkturquoise",highlightthickness=2)
        label7.grid(row=4,column=2,pady=3)
        label7.config(highlightbackground="#00868B",highlightcolor="#00868B")
        lines = details[6].split(" ")
        if ("" in lines):lines.remove("")
        address1=""
        for line in lines:
            address1 += line + "\n"
        label13 = Label(frame3,text=address1,font=("Times New Roman",12),width=20,bg="darkturquoise")
        label13.grid(row=4,column=3,pady=3,rowspan=2)

        label8 = Label(frame3,text="Nationality",font=("Times New Roman",12),padx=21,pady=5,bg="darkturquoise",highlightthickness=2)
        label8.grid(row=5,column=0,pady=3)
        label8.config(highlightbackground="#00868B",highlightcolor="#00868B")
        label12 = Label(frame3,text=details[7],font=("Times New Roman",12),width=20,bg="darkturquoise")
        label12.grid(row=5,column=1,pady=3)

        label9 = Label(frame3,text="Contact No",font=("Times New Roman",12),padx=20,pady=5,bg="darkturquoise",highlightthickness=2)
        label9.grid(row=6,column=2,pady=3)
        label9.config(highlightbackground="#00868B",highlightcolor="#00868B")
        label11 = Label(frame3,text=str(details[8]),font=("Times New Roman",12),width=20,bg="darkturquoise")
        label11.grid(row=6,column=3,pady=3)

        label10 = Label(frame3,text="Email Address",font=("Times New Roman",12),padx=10,pady=5,bg="darkturquoise",highlightthickness=2)
        label10.grid(row=6,column=0,pady=3)
        label10.config(highlightbackground="#00868B",highlightcolor="#00868B")
        label21 = Label(frame3,text=details[9],font=("Times New Roman",12),width=20,bg="darkturquoise")
        label21.grid(row=6,column=1,pady=3)

        self.root.mainloop()

    def get_details(self):
        connection = sqlite3.connect("hotelmanagement.db")
        cursor = connection.cursor()
        cursor.execute(f'select Title,First_Name,Last_Name,DOB,ID_No,Gender,Address,Nationality,Contact_No,Email_Address\
                from {self.user}s where username="{self.username}" and password="{self.password}"')
        details = cursor.fetchall()[0]
        connection.close()
        return details
    
    def edit_profile(self,root,frame):
        root.title("Royal Hotel")
        root.iconbitmap("hotel.ico")
        x = int((1520-710)/2)
        y = int((810-700)/2)
        root.geometry(f'710x700+{x}+{y}')
        root.minsize(710,700)
        root.maxsize(710,700)
        root.configure(bg="#3A5FCD")
        frame.configure(bg="#3A5FCD")
        details = self.get_details()
        ###### button commands #######
        def clear():
            txt.delete(0,END);txt1.delete(0,END);txt2.delete(0,END);txt3.delete(0,END);txt4.delete(0,END);txtbox.delete("1.0","end")
            txt6.delete(0,END);txt7.delete(0,END);txt8.delete(0,END);selected.set("Select")

        def submit():
            txtlist = [txt,txt2,txt3,txt4,txt6,txt7,txt8]
            if (self.is_text_full(txtlist) and selected.get() != "Select"):
                lines = txtbox.get("1.0","end-1c").split("\n");address = ""
                while ("" in lines):
                    lines.remove("")
                for line in lines:
                    address += line + " "
                connection = sqlite3.connect("hotelmanagement.db")
                cursor = connection.cursor()
                cursor.execute(f'update {self.user}s set Title="{txt.get()}",First_Name="{txt1.get()}",Last_Name="{txt2.get()}",DOB="{txt3.get()}",\
                    ID_No="{txt4.get()}",Gender="{selected.get()}",Address="{address}",Nationality="{txt6.get()}",Contact_No="{txt7.get()}",\
                        Email_Address="{txt8.get()}" where username="{self.username}"')
                connection.commit()
                connection.close()
                messagebox.showinfo(self.user + " Profile","Successfully Updated")
                root.destroy()
            else:
                messagebox.showerror("Edit Details","Fill empty text areas")
        
        def close():
            root.destroy()
        ################################
        label2 = Label(frame,text="Edit Your Details",font=("Cooper Black", 25),padx=20,bg="#3A5FCD")
        label2.grid(row=0,column=0,padx=20,pady=5)

        frame3 = LabelFrame(frame, padx=20, pady=20,bd=0)
        frame3.grid(row=1, column=0, padx=15, pady=5,columnspan=2)
        frame3.configure(bg="#87CEFA")

        my_img2 = ImageTk.PhotoImage(Image.open("profile2.jpg"))
        label20 = Label(frame3,image=my_img2,bg="#87CEFA")
        label20.grid(row=0,column=0)

        frame1 = LabelFrame(frame,padx=10,pady=10,borderwidth=5)
        frame1.grid(row=2,column=0,pady=10,padx=20)
        frame1.configure(bg="darkturquoise")

        label = Label(frame1,text="Title",font=("Times New Roman",12),padx=41,pady=3,bg="darkturquoise",highlightthickness=2)
        label.grid(row=1,column=0,pady=5,padx=5)
        label.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt.grid(row=1,column=1);txt.insert(0,details[0])

        label3 = Label(frame1,text="First Name",font=("Times New Roman",12),padx=20,pady=5,bg="darkturquoise",highlightthickness=2)
        label3.grid(row=2,column=0,pady=5)
        label3.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt1 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt1.grid(row=2,column=1);txt1.insert(0,details[1])

        label4 = Label(frame1,text="Last Name",font=("Times New Roman",12),padx=20,pady=5,bg="darkturquoise",highlightthickness=2)
        label4.grid(row=2,column=2,pady=5,padx=7)
        label4.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt2 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt2.grid(row=2,column=3);txt2.insert(0,details[2])

        label5 = Label(frame1,text="Date of Birth",font=("Times New Roman",12),padx=15,pady=5,bg="darkturquoise",highlightthickness=2)
        label5.grid(row=3,column=0,pady=5)
        label5.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt3 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt3.grid(row=3,column=1);txt3.insert(0,details[3])

        label6 = Label(frame1,text="ID No",font=("Times New Roman",12),padx=35,pady=5,bg="darkturquoise",highlightthickness=2)
        label6.grid(row=3,column=2,pady=5)
        label6.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt4 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt4.grid(row=3,column=3);txt4.insert(0,str(details[4]))

        selected = StringVar()
        selected.set(details[5])
        label7 = Label(frame1,text="Gender",font=("Times New Roman",12),padx=31,pady=5,bg="darkturquoise",highlightthickness=2)
        label7.grid(row=4,column=0,pady=5)
        label7.config(highlightbackground="#00868B",highlightcolor="#00868B")
        menubox = OptionMenu(frame1,selected,"Male","Female")
        menubox.grid(row=4,column=1)
        menubox.config(width=20,bg="#79CDCD",activebackground="#79CDCD")

        label7 = Label(frame1,text="Address",font=("Times New Roman",12),padx=29,pady=5,bg="darkturquoise",highlightthickness=2)
        label7.grid(row=4,column=2,pady=5)
        label7.config(highlightbackground="#00868B",highlightcolor="#00868B")
        lines = details[6].split(" ")
        if ("" in lines):lines.remove("")
        address2=""
        for line in lines:
            address2 += line + "\n"
        txtbox = Text(frame1,width=21,height=4,bg="#79CDCD",font=("Times New Roman", 13))
        txtbox.grid(row=4,column=3,rowspan=2);txtbox.insert("1.0",address2)

        label8 = Label(frame1,text="Nationality",font=("Times New Roman",12),padx=21,pady=5,bg="darkturquoise",highlightthickness=2)
        label8.grid(row=5,column=0,pady=5)
        label8.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt6 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt6.grid(row=5,column=1);txt6.insert(0,details[7])

        label9 = Label(frame1,text="Contact No",font=("Times New Roman",12),padx=20,pady=5,bg="darkturquoise",highlightthickness=2)
        label9.grid(row=6,column=2,pady=5)
        label9.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt7 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt7.grid(row=6,column=3);txt7.insert(0,details[8])

        label10 = Label(frame1,text="Email Address",font=("Times New Roman",12),padx=10,pady=5,bg="darkturquoise",highlightthickness=2)
        label10.grid(row=6,column=0,pady=5)
        label10.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt8 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt8.grid(row=6,column=1);txt8.insert(0,details[9])

        frame2 = Frame(frame,bg="#3A5FCD",pady=10)
        frame2.grid(row=7,column=0,pady=10)
        button2 = Button(frame2, text="Submit", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=submit)
        button2.grid(row=0, column=0,padx=50)
        button3 = Button(frame2, text="Clear", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=clear)
        button3.grid(row=0, column=1,padx=50)
        button4 = Button(frame2, text="Close", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="crimson", bd=3,command=close)
        button4.grid(row=0, column=2,padx=40)

        root.mainloop()
    
    def change_pwd(self,root,frame):
        root.title("Royal Hotel")
        root.iconbitmap("hotel.ico")
        root.configure(bg="#3A5FCD")
        x = int((1520-555)/2)
        y = int((810-620)/2)
        root.geometry(f'555x620+{x}+{y}')
        root.minsize(555,620)
        root.maxsize(555,620)
        frame.configure(bg="#3A5FCD")
        ########## button commands ###########
        def clear():
                txt1.delete(0,END);txt2.delete(0,END);txt3.delete(0,END);txt4.delete(0,END)

        def confirm():
            txtareas = [txt1,txt2,txt3,txt4]
            if (self.is_text_full(txtareas)):
                if (str(txt1.get()) == self.username and str(txt2.get()) == self.password and str(txt3.get()) == str(txt4.get())):
                    self.password = txt3.get()
                    connection = sqlite3.connect("hotelmanagement.db")
                    cursor = connection.cursor()
                    cursor.execute(f'update {self.user}s set password="{txt3.get()}" where username="{self.username}"')
                    self.password = txt4.get()
                    connection.commit()
                    connection.close()
                    messagebox.showinfo(self.user+" Profile","Successfully Updated")
                    root.destroy()
                else:
                    messagebox.showerror("change password","check details again")
            else:
                messagebox.showerror("Edit Details","Fill empty text areas")
        
        def close():
            response = messagebox.askyesno("Admin tasks","Do you want to close Change Password?")
            if (response==True):
                root.destroy()
        ######################################
        label1 = Label(frame,text="Edit Password",font=("Cooper Black", 22),padx=30,bg="#3A5FCD",anchor=CENTER)
        label1.grid(row=0,column=0,padx=10,pady=5)

        frame3 = LabelFrame(frame, padx=20, pady=20,bd=0)
        frame3.grid(row=1, column=0, padx=15, pady=5)
        frame3.configure(bg="#87CEFA")

        my_img2 = ImageTk.PhotoImage(Image.open("profile2.jpg"))
        label20 = Label(frame3,image=my_img2,bg="#87CEFA")
        label20.grid(row=0,column=0)

        frame1 = LabelFrame(frame,padx=10,pady=10,borderwidth=5)
        frame1.grid(row=2,column=0,pady=10,padx=20)
        frame1.configure(bg="darkturquoise")

        label2 = Label(frame1,text="Username",font=("Times New Roman",12),padx=37,pady=5,bg="darkturquoise",highlightthickness=2)
        label2.grid(row=0,column=0,pady=5,padx=5)
        label2.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt1 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt1.grid(row=0,column=1)

        label3 = Label(frame1,text="Previous Password",font=("Times New Roman",12),padx=9,pady=5,bg="darkturquoise",highlightthickness=2)
        label3.grid(row=1,column=0,pady=5)
        label3.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt2 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt2.grid(row=1,column=1)

        label4 = Label(frame1,text="New Password",font=("Times New Roman",12),padx=20,pady=5,bg="darkturquoise",highlightthickness=2)
        label4.grid(row=2,column=0,pady=5)
        label4.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt3 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt3.grid(row=2,column=1)

        label5 = Label(frame1,text="Confirm Password",font=("Times New Roman",12),padx=11,pady=5,bg="darkturquoise",highlightthickness=2)
        label5.grid(row=3,column=0,pady=5)
        label5.config(highlightbackground="#00868B",highlightcolor="#00868B")
        txt4 = Entry(frame1, width=20, borderwidth=5, bg="#79CDCD",font=("Times New Roman", 13))
        txt4.grid(row=3,column=1)

        frame2 = Frame(frame,bg="#3A5FCD",pady=10)
        frame2.grid(row=7,column=0,pady=10)

        button2 = Button(frame2, text="Confirm", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=confirm)
        button2.grid(row=0, column=0,padx=40)
        button3 = Button(frame2, text="Clear", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=clear)
        button3.grid(row=0, column=1,padx=40)
        button4 = Button(frame2, text="Close", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 14), bg="#87CEFA",
                        relief=RAISED, activebackground="crimson", bd=3,command=close)
        button4.grid(row=0, column=2,padx=40)

        root.mainloop()

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

