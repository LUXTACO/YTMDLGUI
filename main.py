import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mBox
from ttkthemes import ThemedTk
from threading import *
import subprocess
import os
import time
from colored import fg

color = fg('red')
color2 = fg('white')

def title():
	print(color + """
			██╗   ██╗████████╗███╗   ███╗██████╗ ██╗     ██╗  ██╗██╗   ██╗██████╗ 
			╚██╗ ██╔╝╚══██╔══╝████╗ ████║██╔══██╗██║     ██║  ██║██║   ██║██╔══██╗
			 ╚████╔╝    ██║   ██╔████╔██║██║  ██║██║     ███████║██║   ██║██████╔╝
			  ╚██╔╝     ██║   ██║╚██╔╝██║██║  ██║██║     ██╔══██║██║   ██║██╔══██╗
			   ██║      ██║   ██║ ╚═╝ ██║██████╔╝███████╗██║  ██║╚██████╔╝██████╔╝
			   ╚═╝      ╚═╝   ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝                                                         
	""")
	print(color2 + "========================================================================================================================")

def dl():
	
	i = entry.get()
	os.system("ytmdl " + i)
	os.system("start C:/Users/%USERNAME%/Music")

def exp():
	print("")
	print("Opening...")
	time.sleep(1)
	os.system("start C:/Users/%USERNAME%/Music")
	print("Opened!")
	time.sleep(1)
	os.system("cls")
	title()

def sp():
	os.system("pip install ytmdl")
	os.system("cls")
	print("""
   ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗         ███████╗███╗   ███╗███╗   ███╗██████╗ ███████╗ ██████╗ 
   ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║         ██╔════╝████╗ ████║████╗ ████║██╔══██╗██╔════╝██╔════╝ 
   ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║         █████╗  ██╔████╔██║██╔████╔██║██████╔╝█████╗  ██║  ███╗
   ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║         ██╔══╝  ██║╚██╔╝██║██║╚██╔╝██║██╔═══╝ ██╔══╝  ██║   ██║
   ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗    ██║     ██║ ╚═╝ ██║██║ ╚═╝ ██║██║     ███████╗╚██████╔╝
   ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝     ╚═╝     ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝ ╚═════╝ 
	""")
	time.sleep(2)
	os.system("start https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/")
	time.sleep(5)
	os.system("cls")
	title()

def th():
    t1=Thread(target=dl)
    t1.start()

def th2():
    t2=Thread(target=exp)
    t2.start()

def th3():
    t3=Thread(target=sp)
    t3.start()

win = ThemedTk(theme="arc")
win.title("YTMDL HUB - [BETA]")
win.iconbitmap("icon.ico")
win.resizable(False, False)
win.geometry("400x200")
aLabel = ttk.Label(win ,text=">> YTMDLHUB <<" ,font=("Impact", 30))
aLabel.grid(column=0, row=0)
win.columnconfigure(0, weight=1)
win.rowconfigure(0, weight=0)
 
mainframe = tk.Frame(win)
mainframe.grid(column=0, row=0, sticky='new')
mainframe.grid_columnconfigure(0, weight=3)

sLabel = ttk.Label(win ,text = "Song to Download: " ,font=("Impact", 15))
sLabel.place(x=50 ,y= 90)
entry = ttk.Entry(width= 50)
entry.place(x= 50 ,y= 130)
action = ttk.Button(win, text="Download!", command=th)
action.place(x= 48 ,y= 160)
action = ttk.Button(win, text="Folder!", command=th2)
action.place(x= 279 ,y= 160)
action = ttk.Button(win, text="Setup!", command=th3)
action.place(x= 162 ,y= 160)
os.system("cls")
title()

win.mainloop()
