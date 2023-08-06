from tkinter import *
from PIL import ImageTk,Image
from Customersection import CustomerSection
from Adminsection import AdminSection
import datetime
import sqlite3
from tkinter import messagebox

def clear_widjects(bgcolour="darkturquoise"):
    for widject in Mainframe.winfo_children():
        widject.destroy()
    Mainframe.configure(bg=bgcolour)

def runcustomer():
    clear_widjects(bgcolour="#3A5FCD")
    customer = CustomerSection(root,Mainframe)
    customer.run_customer()

def runadmin():
    clear_widjects(bgcolour="#3A5FCD")
    admin = AdminSection(root,Mainframe)
    admin.run_admin()

def Next():
    clear_widjects()# clear widjects of previous slide
    auto_delete_bookings()
    #run the second slide
    root.configure(bg="darkturquoise")
    x = int((1520-1160)/2)
    y = int((810-500)/2)
    root.geometry(f"1160x500+{x}+{y}")
    root.minsize(1160, 500)
    root.maxsize(1160, 500)
    label = Label(Mainframe, text="Hotel Management System",
                padx=390,
                pady=30,
                bg="darkturquoise",
                font=("Showcard Gothic", 20))
    label.grid(row=0, column=0, columnspan=3)

    welcome_img = ImageTk.PhotoImage(Image.open("welcomepage2.jpg"))
    img_label = Label(Mainframe,image=welcome_img,borderwidth=5,bg="mediumspringgreen")
    img_label.grid(row=1, column=1, rowspan=2)

    admin_label = Label(Mainframe,
                        text="Visit \n Admin \n Site",
                        pady=50,
                        padx=30,
                        bg="dodgerblue",
                        font=("Cooper Black", 15))
    admin_label.grid(row=1, column=0)
    admin_button = Button(Mainframe, text="<<<<<",
                        padx=20,
                        pady=10,
                        font=30,
                        bg="dodgerblue",
                        activebackground="mediumspringgreen",
                        relief=RAISED,border=5,command=runadmin)
    admin_button.grid(row=2, column=0)

    customer_label = Label(Mainframe,
                        text="Visit \n Customer \n Site",
                        padx=20,
                        pady=50,
                        bg="dodgerblue",
                        font=("Cooper Black", 15))
    customer_label.grid(row=1, column=2)
    customer_button = Button(Mainframe,
                            text=">>>>>",
                            padx=20,
                            pady=10,
                            font=30,
                            bg="dodgerblue",
                            activebackground="mediumspringgreen",
                            relief=RAISED,border=5,command=runcustomer)
    customer_button.grid(row=2, column=2)
    root.mainloop()

def Quit():
    response = messagebox.askyesno("Admin tasks","Do you want to Quit?")
    if (response==True):
        quit()

def auto_delete_bookings():
    time = datetime.datetime.now()
    date = str(time)[:10]
    year,month,day = date.split('-')
    conn = sqlite3.connect('hotelmanagement.db')
    cursor = conn.cursor()
    cursor.execute('select Room_ID,Booking_No,Check_In from bookings')
    bookings = cursor.fetchall()
    for booking in bookings:
        y,m,d = booking[2].split(',')[0].split('/')
        if (int(y) > int(year)):
            pass
        elif (int(y) == int(year)):
            if (int(m) > int(month)):
                pass
            elif (int(m) == int(month)):
                if (int(d) > int(day)):
                    pass
                elif (int(d) == int(day)):
                    pass
                else:
                    cursor.execute(f'delete from bookings where Booking_No="{booking[1]}"')
                    cursor.execute(f'update rooms set Availability="Available" where Room_ID="{booking[0]}"')
            else:
                cursor.execute(f'delete from bookings where Booking_No="{booking[1]}"')
                cursor.execute(f'update rooms set Availability="Available" where Room_ID="{booking[0]}"')
        else:
            cursor.execute(f'delete from bookings where Booking_No="{booking[1]}"')
            cursor.execute(f'update rooms set Availability="Available" where Room_ID="{booking[0]}"') 
    conn.commit()
    conn.close()

while True:
    # run 1st slide
    root = Tk()#make the window
    root.title("Royal Hotel ")
    root.iconbitmap("hotel.ico")
    x = int((1520-500)/2)
    y = int((810-500)/2)
    root.geometry(f"500x500+{x}+{y}")
    root.configure(bg="darkturquoise")
    root.minsize(500, 500)
    root.maxsize(500, 500)
    
    Mainframe = Frame(root,bg="darkturquoise")
    Mainframe.grid(row=0,column=0)
    
    label = Label(Mainframe, text="Welcome \n To \n Hotel Management \n System",
                font=("Showcard Gothic", 20),
                bg="darkturquoise",
                padx=108,
                pady=160)
    label.grid(row=0, column=0, columnspan=2)
    
    quit_button = Button(Mainframe, text="Quit", padx=35, pady=10,
                        font=("Showcard Gothic", 10),
                        activebackground="crimson",
                        bg="aquamarine",
                        relief=RAISED,
                        borderwidth=5,command=Quit)
    quit_button.grid(row=1, column=0, sticky=W)
    
    continue_button = Button(Mainframe, text="Continue", padx=35, pady=10,
                            font=("Showcard Gothic", 10),
                            bg="aquamarine",
                            activebackground="limegreen",
                            relief=RAISED,
                            borderwidth=5,command=Next)
    continue_button.grid(row=1, column=1, sticky=E)
    
    root.mainloop()
