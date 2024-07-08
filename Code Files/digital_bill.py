from tkinter import *
from PIL import ImageTk,Image

class Bill():

    def __init__(self,root,frame,row,column,invoice_no,date,detaillist):
        self.root = root
        self.frame = frame
        self.row = row
        self.column = column
        self.invoice_no = invoice_no
        self.date = date
        self.details = detaillist
    
    def show(self):
        frame1 = Frame(self.frame)
        frame1.grid(row=self.row,column=self.column,pady=5,padx=5)
        frame1.config(highlightthickness=3,highlightbackground="black",highlightcolor="black")

        frame2 = Frame(frame1,bg="darkturquoise")
        frame2.grid(row=0,column=0)
        frame2.config(highlightthickness=3,highlightbackground="black",highlightcolor="black")
        
        frame3 = Frame(frame2,bg="darkturquoise")
        frame3.grid(row=2,column=0,sticky=W,pady=10)

        my_img = ImageTk.PhotoImage(Image.open("hotel2.png"))
        imglbl = Label(frame3,image=my_img,bg="darkturquoise",padx=5)
        imglbl.grid(row=0,column=0,sticky=S)

        label11 = Label(frame3,text="Invoice",font=("Times New Roman",25),padx=0,pady=0,bg="darkturquoise")
        label11.grid(row=1,column=0,pady=0,padx=5,sticky=NW)

        frame7 = Frame(frame2,bg="darkturquoise")
        frame7.grid(row=0,column=0,columnspan=3)

        label10 = Label(frame7,text="    Royal  Hotel ",font=("Times New Roman",30),width=25,height=1,bg="darkturquoise")
        label10.grid(row=0,column=0,pady=10)

        my_img2 = ImageTk.PhotoImage(Image.open("hotellogo2.jpg"))
        imglbl2 = Label(frame2,image=my_img2)
        imglbl2.grid(row=2,column=1,pady=10)

        frame4 = Frame(frame2,bg="darkturquoise")
        frame4.grid(row=2,column=2,sticky=E,pady=10)

        label11 = Label(frame4,text="540/A/2\nSamurdhi\nMawatha\nGaligamuwa\nKegalle",font=("Times New Roman",12),padx=0,pady=3,bg="darkturquoise")
        label11.grid(row=1,column=0,pady=0,padx=0,sticky=E)

        label12 = Label(frame2,text="Contact Us : 03501132017              \nEmail Us : royalhotelkeg@gmail.com",font=("Times New Roman",12),padx=0,pady=3,bg="darkturquoise",anchor=W)
        label12.grid(row=3,column=0,pady=5,padx=5,sticky="we",columnspan=3)

        frame5 = Frame(frame1)
        frame5.grid(row=3,column=0,sticky="we")
        frame5.config(highlightthickness=1,highlightbackground="black",highlightcolor="black")

        label13 = Label(frame5,text=f"Invoice No : {self.invoice_no}",font=("Times New Roman",13),padx=0,pady=3)
        label13.grid(row=0,column=0,pady=0,padx=5,sticky=W)
        label14 = Label(frame5,text=f"Issue Date  : {self.date}",font=("Times New Roman",13),padx=0,pady=3)
        label14.grid(row=1,column=0,pady=0,padx=5,sticky=W)
        label15 = Label(frame5,text="Customer Details           ",font=("Times New Roman",13),padx=0,pady=3)
        label15.grid(row=2,column=0,pady=0,padx=5,sticky=W)

        frame6 = Frame(frame5)
        frame6.grid(row=3,column=0,sticky="we",columnspan=2,pady=5,padx=3)
        frame6.config(highlightthickness=1,highlightbackground="black",highlightcolor="black")

        label15 = Label(frame6,text="First Name : {:12s}".format(self.details[0]),font=("Times New Roman",13),padx=0,pady=3)
        label15.grid(row=0,column=0,pady=0,padx=5,sticky=W)
        label16 = Label(frame6,text="Last Name : {:12s}".format(self.details[1]),font=("Times New Roman",13),padx=0,pady=3)
        label16.grid(row=1,column=0,pady=0,padx=5,sticky=W)
        label17 = Label(frame6,text="Contact No : {:12s}".format(str(self.details[2])),font=("Times New Roman",13),padx=0,pady=3)
        label17.grid(row=2,column=0,pady=0,padx=5,sticky=W)
        label18 = Label(frame6,text="{:10s}".format("Check In")+":"+"{:10s}".format(self.details[3][:10]),font=("Times New Roman",13),padx=0,pady=3)
        label18.grid(row=0,column=2,pady=0,padx=5,sticky=W)
        label19 = Label(frame6,text="{:10s}".format("Check Out")+":"+"{:10s}".format(self.details[4][:10]),font=("Times New Roman",13),padx=0,pady=3)
        label19.grid(row=1,column=2,pady=0,padx=5,sticky=W)
        label20 = Label(frame6,text="{:10s}".format("Room No")+":"+"{:10s}".format(str(self.details[5])),font=("Times New Roman",13),padx=0,pady=3)
        label20.grid(row=2,column=2,pady=0,padx=5,sticky=W)

        fakelabel = Label(frame6,padx=0,pady=3)
        fakelabel.grid(row=0,column=1,pady=0,padx=86)

        label21 = Label(frame5,text="Total Price",font=("Times New Roman",15),padx=0,pady=3)
        label21.grid(row=4,column=0,pady=0,padx=5,sticky=W)
        label22 = Label(frame5,text="Rs. {:12s}".format(self.details[6]),font=("Times New Roman",15),padx=0,pady=3)
        label22.grid(row=4,column=1,pady=0,padx=5,sticky=E)

        label23 = Label(frame5,text="Note:This is computer generated Bill,\nNo signature is required.                   ",font=("Dutch801 ItHd BT",11),padx=0,pady=3)
        label23.grid(row=5,column=0,pady=5,padx=5,sticky=W)

        self.root.mainloop()
