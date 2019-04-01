from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import random

depart = " "
arrive = " "
date_departing = " "
row = " "
name = " "
clicks = 0
number_seats = 102
row_seats = 122
number = 0
number_rows = 20
text_list = []

def kill(depart_choice, arrive_choice, name_entry, Date_departing_Entry):
	root1.destroy()
	global depart 
	depart = depart_choice
	global arrive 
	arrive = arrive_choice
	global name
	name = name_entry
	global date_departing
	date_departing = Date_departing_Entry
	global clicks
	clicks += 1
	
def button_click(event = None):
	which_button = event.widget
	which_text = button_dictionary[which_button]
	num = str(which_text.get())
	which_text.set(str(num))
	global number
	number = num
	global clicks
	clicks += 1
	root2.destroy()
	
	
def seat(i, row):
			global text_list
			if i % 6 == 0:
				text_list[i].set(str(row) + "A")
			if i % 6 == 1:
				text_list[i].set(str(row) + "B")
			if i % 6 == 2:
				text_list[i].set(str(row) + "C")
			if i % 6 == 3:
				text_list[i].set(str(row) + "D")
			if i % 6 == 4:
				text_list[i].set(str(row) + "E")
			if i % 6 == 5:
				text_list[i].set(str(row) + "F")	
def button_name(i):
		global text_list
		if i >= 0 and i <= 5:
			row = 1
			seat(i, row)	
		if i >= 6 and i <= 12:
			row = 2
			seat(i, row)
		if i >= 12 and i <= 17:
			row = 3
			seat(i, row)		
		if i >= 18 and i <= 23:
			row = 4
			seat(i, row)
		if i >= 24 and i <= 29:
			row = 5
			seat(i, row)
		if i >= 30 and i <= 35:
			row = 6
			seat(i, row)
		if i >= 36 and i <= 41:
			row = 7
			seat(i, row)
		if i >= 42 and i <= 47:
			row = 8
			seat(i, row)
		if i >= 48 and i <= 53:
			row = 9
			seat(i, row)
		if i >= 54 and i <= 59:
			row = 10
			seat(i, row)
		if i >= 60 and i <= 65:
			row = 11
			seat(i, row)
		if i >= 66 and i <= 71:
			row = 12
			seat(i, row)
		if i >= 72 and i <= 77:
			row = 13
			seat(i, row)
		if i >= 78 and i <= 83:
			row = 14
			seat(i, row)
		if i >= 84 and i <= 89:
			row = 15
			seat(i, row)
		if i >= 90 and i <= 95:
			row = 16
			seat(i, row)
		if i >= 96 and i <= 102:
			row = 17
			seat(i, row)

while clicks == 0:

	#First window
	root1 = tk.Tk()
	root1.title("United Airlines Main Menu")
	root1.configure(background='white')

	#Importing Image
	img = ImageTk.PhotoImage(Image.open("download.png"))
	imglabel = Label(root1, image=img).grid(row=0, columnspan=2)        

	#Name
	wordName = StringVar()
	wordName.set("Name:")
	wordNameLabel = Label(root1, textvariable = wordName)
	wordNameLabel.grid(row = 1, column = 0)
	
	#Adding the input name box
	Name = StringVar()
	Name_entry = Entry(root1, textvariable = Name)
	Name_entry.grid(row = 1, column = 1)
	
	#Blank Space
	blank = StringVar()
	blank.set(" ")
	blankLabel = Label(root1, textvariable = blank)
	blankLabel.grid(row = 2, column = 0)
	
	#Blank Space
	blank = StringVar()
	blank.set(" ")
	blankLabel = Label(root1, textvariable = blank)
	blankLabel.grid(row = 3, column = 0)
	
	#Adding a title
	title = StringVar()
	title.set("Select Your Departure and Arrival Airports")
	titleLabel = Label(root1, textvariable = title)
	titleLabel.grid(row = 4, column = 1)

	#Adding the word "From"
	fro = StringVar()
	fro.set("From:")
	froLabel = Label(root1, textvariable = fro)
	froLabel.grid(row = 5, column = 0)

	#Adding depart dropdown menu
	airports_options_depart = ["ORD", "JFK", "ATL", "DFW", "LAX", "IAH", "SFO", "EWR", "MCO"]
	var_depart = StringVar()
	var_depart.set("Airport Departure")
	depart = OptionMenu(root1,var_depart,*airports_options_depart)
	depart.pack()
	depart.grid(row = 5, column = 1)
	
	#Adding the word "to"
	to = StringVar()
	to.set("to:")
	toLabel = Label(root1, textvariable = to)
	toLabel.grid(row = 5, column = 2)

	#Adding arriving dropdown menu
	airports_options_arrive = ["ORD", "JFK", "ATL", "DFW", "LAX", "IAH", "SFO", "EWR", "MCO"]
	var_arrive = StringVar()
	var_arrive.set("Airport Arrival")
	arrive = OptionMenu(root1,var_arrive,*airports_options_arrive)
	arrive.pack()
	arrive.grid(row = 5, column = 3)

	#Blank Space
	blank = StringVar()
	blank.set(" ")
	blankLabel = Label(root1, textvariable = blank)
	blankLabel.grid(row = 6, column = 0)
	
	#Adding the word "Date of Depart"
	wordDepart = StringVar()
	wordDepart.set("Date of Departure (mm/dd/yy):")
	wordDepartLabel = Label(root1, textvariable = wordDepart)
	wordDepartLabel.grid(row = 7, column = 1)

	#Adding the input date box
	Date_departing = StringVar()
	Date_departing_Entry = Entry(root1, textvariable = Date_departing)
	Date_departing_Entry.grid(row = 8, column = 1)
	
	#Blank Space
	blank = StringVar()
	blank.set(" ")
	blankLabel = Label(root1, textvariable = blank)
	blankLabel.grid(row = 9, column = 0)
	
	continueButton = Button(root1, text = "Check Available Seats", command = lambda: kill(var_depart.get(), var_arrive.get(), Name_entry.get(), Date_departing_Entry.get()))
	continueButton.grid(row = 9, column = 5)

	root1.mainloop()
	
while clicks == 1:
	
	root2 = Tk()
	root2.title("Seat Selection")

	seat_letters = ["A", "B", "C", "D", "E", "F"]
	button_list = []

	img = ImageTk.PhotoImage(Image.open("nose.jpg"))
	imglabel = Label(root2, image=img).grid(row = 0, columnspan = 6)        

	img2 = ImageTk.PhotoImage(Image.open("tail.jpg"))
	img2label = Label(root2, image=img2).grid(row=30, columnspan = 6)    
	
	for i in range(number_seats):
		text_list.append(StringVar())

	for i in range(number_seats):
		text_list[i].set(str(i + 1))
	global row
	
	for i in range(number_seats):
		button_name(i)
				
	for i in range(number_seats):
		seat = number_seats
		
			
		button_list.append(Button(root2, textvariable = text_list[i]))

	for i in range(number_seats):
		button_list[i].grid(row = i // 6 + 3, column = i % 6)
		button_list[i].bind("<Button-1>", button_click)
	
	button_dictionary = {}
	for i in range(number_seats):
		button = button_list[i]
		text = text_list[i]
		button_dictionary[button] = text

	root2.mainloop()	
	

root3 = Tk()
root3.title("Ticket")

header = ImageTk.PhotoImage(Image.open("header.png"))
headerlabel = Label(root3, image=header).grid(row=0, columnspan=4)     

barcode = ImageTk.PhotoImage(Image.open("barcode.jpg"))
barcodelabel = Label(root3, image=barcode).grid(row=1, column = 4, rowspan=3)    


blank = StringVar()
blank.set(name + "                                " + date_departing)
blankLabel = Label(root3, textvariable = blank)
blankLabel.config(font = ("TKDefaultFont Bold", 15))
blankLabel.grid(row = 1, column = 0) 


blank = StringVar()
blank.set(depart + " → " + arrive)
blankLabel = Label(root3, textvariable = blank)
blankLabel.config(font = ("TKDefaultFont Bold", 25))
blankLabel.grid(row = 2, column = 0) 


gate_number = int(random.randrange(1, 81))
hour = int(random.randrange(1, 13))
minute = int(random.randrange(10, 61))
am_pm = ["AM", "PM"]
choose = int(random.randrange(0, 2))
am_or_pm = am_pm[choose]

blank = StringVar()
blank.set("Gate " + str(gate_number))
blankLabel = Label(root3, textvariable = blank)
blankLabel.config(font = ("TKDefaultFont Bold", 15))
blankLabel.grid(row = 2, column = 1)

blank = StringVar()
blank.set("Depart at " + str(hour) + ":" + str(minute) + " " + str(am_or_pm))
blankLabel = Label(root3, textvariable = blank)
blankLabel.config(font = ("TKDefaultFont Bold", 15))
blankLabel.grid(row = 2, column = 2)

blank = StringVar()
blank.set("Seat " + str(number))
blankLabel = Label(root3, textvariable = blank)
blankLabel.config(font = ("TKDefaultFont Bold", 15))
blankLabel.grid(row = 2, column = 3)

ticket_number = int(random.randrange(999999999999, 9999999999999))

blank = StringVar()
blank.set("Ticket: " + str(ticket_number))
blankLabel = Label(root3, textvariable = blank)
blankLabel.config(font = ("TKDefaultFont Bold", 10))
blankLabel.grid(row = 3, column = 0)

root3.mainloop()
