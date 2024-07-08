from tkinter import *
from PIL import ImageTk,Image

class Room_category():

    def __init__(self,root,frame):
        self.root = root
        self.frame = frame
    
    def run(self):
        self.root.title("Royal Hotel")
        self.root.iconbitmap("hotel.ico")
        self.root.geometry('600x630')
        self.root.minsize(600,630)
        self.root.maxsize(600,630)
        self.frame.configure(bg="#3A5FCD")
        i = 0

        def Move_forward():
            nonlocal i
            nonlocal label1;nonlocal label2;nonlocal imglbl;nonlocal my_img
            i += 1
            label1.grid_forget()
            imglbl.grid_forget()
            label2.grid_forget()

            self.root.geometry(sizes[i])
            w , h = int(sizes[i][:3]) , int(sizes[i][4:])
            self.root.minsize(w,h)
            self.root.maxsize(w,h)

            label1 = Label(frame,text=categories[i],font=("Berlin Sans FB Demi", 20),bg="darkturquoise")
            label1.grid(row=0,column=0,padx=5,pady=5)

            my_img = ImageTk.PhotoImage(Image.open(imagepaths[i]))
            imglbl = Label(frame,image=my_img, bg="#87CEFA")
            imglbl.grid(row=1,column=0,padx=5,pady=5)

            label2 = Label(frame,text=discriptions[i],anchor=CENTER,font=("Berlin Sans FB Demi", 12), bg="#87CEFA")
            label2.grid(row=2,column=0,sticky="we",padx=5,pady=5)

            if (i == 7):
                next_button.configure(state=DISABLED)
            if (i > 0):
                back_button.configure(state=NORMAL)

        def Move_backward():
            nonlocal i
            nonlocal label1;nonlocal label2;nonlocal imglbl;nonlocal my_img
            i -= 1
            label1.grid_forget()
            imglbl.grid_forget()
            label2.grid_forget()
            self.root.geometry(sizes[i])
            w , h = int(sizes[i][:3]) , int(sizes[i][4:])
            self.root.minsize(w,h)
            self.root.maxsize(w,h)

            label1 = Label(frame,text=categories[i],font=("Berlin Sans FB Demi", 20),bg="darkturquoise")
            label1.grid(row=0,column=0,padx=5,pady=5)

            my_img = ImageTk.PhotoImage(Image.open(imagepaths[i]))
            imglbl = Label(frame,image=my_img, bg="#87CEFA")
            imglbl.grid(row=1,column=0,padx=5,pady=5)

            label2 = Label(frame,text=discriptions[i],anchor=CENTER,font=("Berlin Sans FB Demi", 12), bg="#87CEFA")
            label2.grid(row=2,column=0,sticky="we",padx=5,pady=5)

            if (i <= 0):
                back_button.configure(state=DISABLED)
            if (i < 7):
                next_button.configure(state=NORMAL)
        
        def close():
            self.root.destroy()

        sizes = ["600x630","610x600","670x580","600x625","605x625","590x555","595x580","645x555"]
        frame = Frame(self.frame,bg="#3A5FCD")
        frame.grid(row=0,column=0,padx=15,pady=15,columnspan=3)

        categories = ["Single Room","Double Room","Triple Room","Quad Room","Queen Room","King Room","Twin Room","Suit Room"]
        label1 = Label(frame,text=categories[i],font=("Berlin Sans FB Demi", 20),bg="darkturquoise")
        label1.grid(row=0,column=0,padx=5,pady=5)

        imagepaths = ["Single.jpg","double.jpg","Triple.jpg","Quad.jpg","Queen.jpg","King.jpg","Twin.jpg","suite.jpeg"]
        my_img = ImageTk.PhotoImage(Image.open(imagepaths[i]))
        imglbl = Label(frame,image=my_img, bg="#87CEFA")
        imglbl.grid(row=1,column=0,padx=5,pady=5)

        Single_Room = "A room assigned to one person.\nCan have one or more beds.\nThe room size or area of Single Rooms are generally between 37 m² to 45 m²."
        Double_Room = "A room assigned to two people.\nCan have one or more beds.\nThe room size or area of Double Rooms are generally between 40 m² to 45 m²."
        Triple_Room = "A room that can accommodate three persons and has been fitted with three twin beds,\none double bed and one twin bed or two double beds.\n\
            The room size or area of Triple Rooms are generally between 45 m² to 65 m²."
        Quad_Room = "A room assigned to four people.\nCan have two or more beds.\nThe room size or area of Quad Rooms are generally between 70 m² to 85 m²."
        Queen_Room = "A room with a queen-sized bed.\nCan be occupied by one or more people.\nThe room size or area of Queen Rooms are generally between 32 m² to 50 m²."
        King_Room = "A room with a king-sized bed.\nCan be occupied by one or more people.\nThe room size or area of King Rooms are generally between 32 m² to 50 m²."
        Twin_Room = "A room with two twin beds.\nCan be occupied by one or more people.\nThe room size or area of Twin Rooms are generally between 32 m² to 40 m²."
        Suit_Room = "A parlour or living room connected with to one or more bedrooms.\n (A room with one or more bedrooms and a separate living space.)\n\
            The room size or area of Suite rooms are generally between 70 m² to 100 m²."

        discriptions = [Single_Room,Double_Room,Triple_Room,Quad_Room,Queen_Room,King_Room,Twin_Room,Suit_Room]
        label2 = Label(frame,text=discriptions[i],anchor=CENTER,font=("Berlin Sans FB Demi", 12), bg="#87CEFA")
        label2.grid(row=2,column=0,sticky="we",padx=5,pady=5)

        back_button = Button(self.frame, text="Previous",
                                    padx=5, pady=5,
                                    font=("Berlin Sans FB Demi", 12), bg="#87CEFA",
                                    relief=RAISED, activebackground="mediumspringgreen",command = Move_backward,state=DISABLED)
        back_button.grid(row=1, column=0, pady=5)

        close_button = Button(self.frame, text="Close",
                                    padx=5, pady=5,
                                    font=("Berlin Sans FB Demi", 12), bg="#87CEFA",
                                    relief=RAISED, activebackground="mediumspringgreen",command = close)
        close_button.grid(row=1, column=1, pady=5)

        next_button = Button(self.frame, text="Next",
                                    padx=15, pady=5,
                                    font=("Berlin Sans FB Demi", 12), bg="#87CEFA",
                                    relief=RAISED, activebackground="mediumspringgreen",command = Move_forward)
        next_button.grid(row=1, column=2, pady=5)

        self.root.mainloop()