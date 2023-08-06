import sqlite3

connection = sqlite3.connect("hotelmanagement.db")
cursor = connection.cursor()

# cursor.execute('create table customers ("Customer_ID" text,"Title" text,"First_Name" text,"Last_Name" text,"Address" text,"Gender" text,\
#     "DOB" text,"ID_No" int,"Nationality" text,"Email_Address" text,"username" text,"password" text,"Contact_No" int)')

# cursor.execute('create table admins ("Admin_ID","Title" text,"First_Name" text,"Last_Name" text,"Address" text,"Gender" text,"DOB" text,\
#     "ID_No" int,"Nationality" text,"Email_Address" text,"username" text,"password" text,"Contact_No" int)')

# cursor.execute('create table rooms ("Room_ID" text,"Room_No" int,"Floor_No" int,"Category" text,"Up_to" int,"Availability" text,"Price_for_hour" int,"Price_for_day" int)')

# cursor.execute('create table bookings ("Booking_No" text,"Booking_Date" text,"Customer_ID" text,"Room_ID" text,"Duration_by_hours" int,"Duration_by_days" int,"NOC_1" int,"NOC_2" int,\
#     "NOC_3" int,"NOA" int,"Mealplan" text,"Meal_Price" int,"Check_In" text,"Check_Out" text,"Total_Price" int,"Discount" text,"Advance" int,"Balance" int,\
#     "Comment" text)')

# cursor.execute('create table mealplans ("Meal_Plan" text,"Price_for_one_to_one_customer" int)')

# cursor.execute('create table checkout ("Booking_No" text,"First_Name" text,"Last_Name" text,"Room_No" int,"Check_In" text,"Check_Out" text,"Total_Price" int,"Discount" text,\
#     "Advance" int,"Balance" int)')bookingdate
# cursor.execute('create table checkout ("Customer_ID" text,"Booking_No" text,"Room_ID" text,"Duration_by_hours" int,"Duration_by_days" int,"NOC_1" int,"NOC_2" int,"NOC_3" int,"NOA" int,\
#     "Mealplan" txt,"Meal_Price" int,"Check_In" text,"Check_Out" text,"Total_Price" int,"Discount" int,"Advance" int,"Balance" int,"Comments" text)')

#cursor.execute('create table discounts ("Category" text,"Minimum_days" int,"Mealplan" text,"Discount" int)')
# discounts = [("Single",60,"3 Meals",5),("Double",60,"3 Meals",6),("Triple",30,"3 Meals",5),("Triple",60,"3 Meals",8),("Quad",15,"3 Meals",5),
# ("Quad",30,"3 Meals",8),("Quad",60,"3 Meals",10),("Queen",15,"3 Meals",8),("King",15,"3 Meals",8),("Twin",15,"3 Meals",10),("Suit",15,"3 Meals",10),
# ("Suit",30,"3 Meals",15)]
# cursor.executemany('insert into discounts values (?,?,?,?)',discounts)

#cursor.execute('create table idcreate ("type" text,"Id" text)')
# data = [("customerid" , "0C000001"),
# ("adminid" , "0A000001"),
# ("roomid" , "0R000001"),
# ("bookingid" , "0B000001")]
# cursor.executemany('insert into idcreate values(?,?)',data)

def idcreater(type):
    connection = sqlite3.connect("hotelmanagement.db")
    cursor = connection.cursor()
    cursor.execute(f'select id from idcreate where type="{type}"')
    Id = cursor.fetchall()[0][0]
    right_num = int(Id[2:])
    if (right_num == 999999):
        left_num = int(Id[0])
        new_id = str(left_num+1) + Id[1] + "0000001"
    else:
        new_id = Id[:2] + str(right_num+1).zfill(6)
    cursor.execute(f'update idcreate set id="{new_id}" where type="{type}"')
    connection.commit()
    connection.close()
    return Id

# mealplans = [("Room Only",0),("Breakfast Only",500),("Lunch Only",500),("Dinner Only",500),("Breakfast & Lunch",1000),("Breakfast & Dinner",1000),("Lunch & Dinner",1000),("3 Meals",1500)]
# cursor.executemany('insert into mealplans values(?,?)',mealplans)

#cursor.execute('insert into admins values("test","test","test","test","test","test","test",1,"test","test","admin","pass",1)')

#cursor.execute('create table clipboard ("User_ID" text,"Room_ID" text,"Room_No" int)')

# cursor.execute('insert into idcreate values("invoiceno","0I000001")')

connection.commit()
connection.close()