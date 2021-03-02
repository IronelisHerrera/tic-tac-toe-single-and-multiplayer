#!/usr/bin/python3.7
import sys
import os
from tkinter import *
from tkinter import messagebox
import subprocess




gui_tkinter = Tk()
gui_tkinter.geometry("1250x650+0+0")
gui_tkinter.title('Tic-Tac-Toe: Principal Menu')
label= Label(gui_tkinter, text = "MENU", font=("Century Gothic", 20, 'bold'), fg="#EDAA7C", justify =CENTER)
label.pack(padx=40, pady = 20)
scripts_paths = ("/home/ihv/Tic-tac-toe-Single-Multiple/server.py", "/home/ihv/Tic-tac-toe-Single-Multiple/client.py")


def OnButtonClick(btnid):
    gui_tkinter = Toplevel()
    if btnid == 1:
        os.system('python single-player.py')
        gui_tkinter.withdraw()
    if btnid == 2:
        proccesses = [subprocess.Popen(["python", script]) for script in scripts_paths]
        gui_tkinter.withdraw()
  



btn_single_player=Button(gui_tkinter, text="Single Player", font=("Century Gothic", 12, 'bold'),height = 3, width = 30,bg="#7D7F7D",fg = "#ffffff", command=lambda:OnButtonClick(1))
btn_single_player.pack(padx=20, pady=50) 

btn_single_player=Button(gui_tkinter, text="Multiple Player",font=("Century Gothic", 12, 'bold'),height = 3, width = 30,bg="#7D7F7D",fg = "#ffffff",command=lambda:OnButtonClick(2))
btn_single_player.pack(padx=20, pady=10) 


gui_tkinter.mainloop()  