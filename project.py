from tkinter import *
from PIL import ImageTk, Image 
import random 
import tkinter.messagebox as tmsg 

app = Tk() 
count = 0


def generate(): 
	global comp 
	comp = random.randint(1, 101) 


def basic(): 
	# setup the window size, title, logo 
	app.title("Number Guessing game") 
	app.geometry("900x500") 
	app.minsize(500, 500) 
	app.maxsize(500, 500) 
	photo = PhotoImage(Image.open("guess.png")) 
	# app.iconphoto(False, photo) 
	heading = Label(text='Number Guessing game', font="Helvicta 18 bold", 
					bg='black', fg='tomato', padx=170).pack() 
	with open('score.txt', 'r') as f: 
		hg = f.read() 
	sc = Label(app, text=f'Previous score: {hg}', font='lucida 8 bold ').pack( 
		anchor=E, padx=25, pady=5) 

	# footer 
	footer = Label(text='Developed by Hrushikesh Bhise', font="Helvicta 8 bold", 
				bg='black', fg='tomato', padx=153).pack(side=BOTTOM) 

	# Setup Menu 
	mymenu = Menu(app) 
	filee = Menu(mymenu, tearoff=0) 
	mymenu.add_cascade(label='Start', menu=filee) 
	mymenu.add_cascade(label='Restart', command=restart) 
	mymenu.add_command(label='About', command=call1) 
	mymenu.add_command(label='Quit', command=quit) 
	app.config(menu=mymenu) 
	generate() 


def result(): 
	global count 
	number = userv.get() 
	if number == '': 
		tmsg.showerror('Error', "Please enter a value") 
	else: 
		n = int(number) 
		count += 1
		if count == 10: 
			a = tmsg.showinfo('Game over', 'You loose the Game!') 
		elif comp == n: 
			score = 11-count 
			a = tmsg.showinfo( 
				'Win', f'You guess right number!\nYour score {score}') 
			show.config(text='Winn!', fg='green') 
			with open('score.txt', 'w') as f: 
				f.write(str(score)) 
			generate() 
			tmsg.showinfo('Next number', f'click ok to Guess another number') 
		elif comp > n: 
			show.config(text='Select greater number', fg='red') 
		else: 
			show.config(text='Select smaller number', fg='red') 


def restart(): 
	tmsg.showerror('Reset', "Game reset!") 
	generate() 


def call1(): 
	str1 = 'This game is developed by XD\n\ncopyright@2021-22 '
	tmsg.showinfo('About', str1) 




basic() 

print(comp) 
userv = StringVar() 
user = Entry(app, textvariable=userv, justify=CENTER, relief=FLAT, 
			borderwidth=2, font='Helvicta 18 bold').pack(pady=10) 
i = Image.open('guess.png', mode='r')
resize = i.resize((250, 100))  
img = ImageTk.PhotoImage(resize) 
l = Label(image=img).pack(pady=30) 

i = Image.open('bt.png') 
resized_image = i.resize((150, 50)) 
new_image = ImageTk.PhotoImage(resized_image) 
submit = Button(app, image=new_image, command=result, 
				font='Helvicta 18 bold', relief=FLAT).pack(pady=10) 
show = Label(app, text='', font='Helvicta 12 bold') 
show.pack(pady=10) 
app.mainloop() 