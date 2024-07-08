from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

class Availability():

    def __init__(self,root,frame):
        self.root = root
        self.frame = frame
        self.clipboard = {"Room ID":"","Room No":0}
        self.mode = "normal"
    
    def is_available(self):
        connection = sqlite3.connect('hotelmanagement.db')
        cursor = connection.cursor()
        cursor.execute('select Room_ID,Category,Floor_No,Room_No,Availability,Price_for_day from rooms where Availability="Available"')
        available_rooms = cursor.fetchall()
        connection.close()
        if (len(available_rooms) == 0):
            messagebox.showinfo("Customer tasks","Sorry!!!\nNo available rooms")
        else:
            self.check_availability(available_rooms)

    def check_availability(self,data):
        self.root.title("Royal Hotel")
        self.root.iconbitmap("hotel.ico")
        if (self.mode == "normal"):
            x = int((1520-680)/2)
            y = int((810-500)/2)
            self.root.geometry(f'680x500+{x}+{y}');self.root.minsize(680,500);self.root.maxsize(680,500)
        else:
            x = int((1520-770)/2)
            y = int((810-500)/2)
            self.root.geometry(f'770x500+{x}+{y}')
        self.root.configure(bg="#3A5FCD")
        self.frame.configure(bg="#3A5FCD")

        def enable_button(e):
            button.configure(state=NORMAL)

        def copy_id():
            selected = my_tree.focus()
            details = my_tree.item(selected,"values")
            connection = sqlite3.connect('hotelmanagement.db')
            cursor = connection.cursor()
            cursor.execute('select * from clipboard')
            c = cursor.fetchall()
            if (len(c) == 1):
                cursor.execute(f'update clipboard set Room_ID="{details[0]}",Room_No="{details[3]}"')
                connection.commit()
            else:
                self.clipboard["Room ID"] = details[0];self.clipboard["Room No"] = details[3]
            cursor.close()
            messagebox.showinfo("Room Availability","Id copied to clipboard")
            button.configure(state=DISABLED)
        
        def close():
            self.root.destroy()
            
        label1 = Label(self.frame, text="Room Availability", font=(
            "Cooper Black", 20), padx=30, pady=5, bg="#3A5FCD", bd=0)
        label1.grid(row=0, column=0, pady=0, padx=3, columnspan=2)

        frame1 = Frame(self.frame, bg="darkturquoise", padx=10, pady=19)
        frame1.grid(row=1, column=0, pady=20, padx=20,columnspan=2)

        # adding style
        my_style = ttk.Style()
        my_style.theme_use("default")
        my_style.configure("Treeview",background="silver",foreground="black",rowheight=30,fieldbackground="silver")
        my_style.map("Treeview",background=[("selected","blue")])
        # add a scrollbutton
        my_scroll = Scrollbar(frame1)
        my_scroll.grid(row=1,column=4,sticky=NS)
        # creating treeveiw
        my_tree = ttk.Treeview(frame1,yscrollcommand=my_scroll.set)
        my_tree.grid(row=1, column=0)
        #configure tags
        my_tree.tag_configure("eventag",background="white")
        my_tree.tag_configure("oddtag",background="lightblue")
        # config scrollbar
        my_scroll.config(command=my_tree.yview)
        # define columns
        if (self.mode == "normal"):
            my_tree["columns"] = ("Room ID", "Category", "Floor No","Room No", "State", "Price")
        else:
            my_tree["columns"] = ("Room ID", "Category", "Floor No","Room No", "State", "Price","Available From")

        # format columns
        my_tree.column("#0", width=0, minwidth=0, stretch=NO)
        my_tree.column("Room ID", anchor=CENTER, width=100)
        my_tree.column("Category", anchor=CENTER, width=100)
        my_tree.column("Floor No", anchor=CENTER, width=100)
        my_tree.column("Room No", anchor=CENTER, width=100)
        my_tree.column("State", anchor=CENTER, width=100)
        my_tree.column("Price", anchor=CENTER, width=100)
        if (self.mode == "smart"):my_tree.column("Available From", anchor=CENTER, width=100)
        # create headiings
        my_tree.heading("#0", text="")
        my_tree.heading("Room ID", text="Room ID", anchor=CENTER)
        my_tree.heading("Category", text="Category", anchor=CENTER)
        my_tree.heading("Floor No", text="Floor No", anchor=CENTER)
        my_tree.heading("Room No", text="Room No", anchor=CENTER)
        my_tree.heading("State", text="State", anchor=CENTER)
        my_tree.heading("Price", text="Price", anchor=CENTER)
        if (self.mode == "smart"):my_tree.heading("Available From", text="Available From", anchor=CENTER)
        
        count = 0
        for record in data:
            if (count%2 == 0):
                my_tree.insert(parent='', index='end', iid=count, text="", values=record,tag="eventag")
            else:
                my_tree.insert(parent='',index='end',iid=count,text="",values=record,tag="oddtag")
            count += 1
        #binding
        my_tree.bind("<ButtonRelease-1>",enable_button)#<Double-1> for double click

        button = Button(self.frame, text="Copy Room ID", padx=7, pady=0,
                        font=("Berlin Sans FB Demi", 13), bg="#87CEFA",
                        relief=RAISED, activebackground="mediumspringgreen", bd=3,command=copy_id,state=DISABLED)
        button.grid(row=2, column=1,padx=10)

        button2 = Button(self.frame, text="Close", padx=15, pady=0,
                        font=("Berlin Sans FB Demi", 13), bg="#87CEFA",
                        relief=RAISED, activebackground="crimson", bd=3,command=close)
        button2.grid(row=2, column=0,padx=10)

        self.root.mainloop()
    def get_clipboard(self):
        clipboard = self.clipboard
        return clipboard


class Smartavailability(Availability):

    def __init__(self, root, frame):
        super().__init__(root, frame)
        self.clipboard = {}
        self.mode = "smart"
    
    def is_available(self,detail_list):
        checkin = detail_list[0];checkout = detail_list[2];noa = int(detail_list[1]);noc = int(detail_list[3])
        checkindate = checkin.split(',')[0];checkinyear,checkinmonth,checkinday = checkindate.split('/')
        checkoutdate = checkout.split(',')[0];checkoutyear,checkoutmonth,checkoutday = checkoutdate.split('/')
        if (noa + noc > 4):
            rec_list = []
        elif (checkinyear != checkoutyear or ((int(checkoutmonth)-int(checkinmonth))*30 + int(checkoutday) - int(checkinday) > 90)):
            rec_list = ["d"]
        else:
            if (noa + noc == 4):
                rec_list = ["Quad","Suite","blank","blank","blank","blank"]
            elif (noa + noc == 3):
                rec_list = ["Triple","Quad","Suite","blank","blank","blank"]
            elif (noa + noc == 2):
                rec_list = ["Double","Triple","Quad","King","Queen","Twin"]
            elif (noa + noc == 1):
                rec_list = ["Single","Double","Triple","King","Queen","Twin"]
            else:
                rec_list = []

        if (rec_list == []):
            messagebox.showinfo("Availability checking","Can't supply a room for these\nno of guests")
            self.root.destroy()
        elif (rec_list == ["d"]):
            messagebox.showinfo("Availability checking","Please Check checkin and checkout again\nmaximum duration is 3 months")
            self.root.destroy()
        else:
            #getting availble rooms
            list1 = self.get_available_rooms(rec_list,"Available",checkin)
            #getting booked rooms
            list2 = self.get_available_rooms(rec_list,"Booked",checkin)
            #getting checkin rooms
            list3 = self.get_available_rooms(rec_list,"CheckIn",checkin)
            data = list1+list2+list3
            self.check_availability(data)
    
    def get_available_rooms(self,List,State,checkin):
        connection = sqlite3.connect('hotelmanagement.db')
        cursor = connection.cursor()
        condition = f'Category="{List[0]}" or Category="{List[1]}" or Category="{List[2]}" or Category="{List[3]}" or Category="{List[4]}" or Category="{List[5]}"'
        
        if (State == "Available"):
            cursor.execute(f'select Room_ID,Category,Floor_No,Room_No,Availability,Price_for_day from rooms where ({condition}) and Availability="Available"')
            rooms = cursor.fetchall()
        elif (State == "Booked"):
            cursor.execute(f'select Room_ID,Category,Floor_No,Room_No,Availability,Price_for_day from rooms where ({condition}) and Availability="Booked"')
            test = cursor.fetchall()
            new_test = []
            for room in test:
                room1 = list(room)
                cursor.execute(f'select Check_Out from bookings where Room_ID="{room1[0]}"')
                details = cursor.fetchall()
                if (len(details) > 0):
                    checkout = details[0][0]
                    room1.append(checkout)
                    new_test.append(tuple(room1))
            rooms = self.filter_rooms(new_test,checkin)
        else:
            cursor.execute(f'select Room_ID,Category,Floor_No,Room_No,Availability,Price_for_day from rooms where ({condition}) and Availability="Checkin"')
            test = cursor.fetchall()
            new_test = []
            for room in test:
                room1 = list(room)
                cursor.execute(f'select Check_Out from checkin where Room_ID="{room1[0]}"')
                details = cursor.fetchall()
                if (len(details) > 0):
                    checkout = details[0][0]
                    room1.append(checkout)
                    new_test.append(tuple(room1))
            rooms = self.filter_rooms(new_test,checkin)
        connection.close()
        return rooms

    def filter_rooms(self,room_list,checkin):# checkin yy/mm/dd,hh.mm pm
        filter_list = []
        for room in room_list:
            room1 = list(room)
            checkoutdate = room1[-1].split(',')[0];checkouttime = room1[-1].split(',')[1] 
            checkoutyear,checkoutmonth,checkoutday = checkoutdate.split('/');checkouthour = checkouttime.split('.')[0]
            checkindate = checkin.split(',')[0];checkintime = checkin.split(',')[1] 
            checkinyear,checkinmonth,checkinday = checkindate.split('/');checkinhour = checkintime.split('.')[0]
            room1.remove(room[-1])
            if (int(checkinyear) > int(checkoutyear)):
                availble_date = checkoutyear+"/"+checkoutmonth+"/"+str(int(checkoutday)+1)
                room1.append(availble_date)
                filter_list.append(tuple(room1))
            
            elif (int(checkinyear) == int(checkoutyear)):

                if (int(checkinmonth) > int(checkoutmonth)):
                    availble_date = checkoutyear+"/"+checkoutmonth+"/"+str(int(checkoutday)+1)
                    room1.append(availble_date)
                    filter_list.append(tuple(room1))

                elif (int(checkinmonth) == int(checkoutmonth)):

                    if (int(checkinday) > int(checkoutday)):
                        availble_date = checkoutyear+"/"+checkoutmonth+"/"+str(int(checkoutday)+1)
                        room1.append(availble_date)
                        filter_list.append(tuple(room1))
                    elif (int(checkinday) == int(checkoutday)):
                        if (int(checkinhour) > int(checkouthour)+3):
                            availble_date = checkoutdate+","+str(int(checkouthour)+3)+"."+"00"
                            room1.append(availble_date)
                            filter_list.append(tuple(room1))
                    else:
                        pass
                else:
                    pass
            
            else:
                pass
        return filter_list







