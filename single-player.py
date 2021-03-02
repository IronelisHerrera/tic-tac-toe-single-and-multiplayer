from tkinter import *
from tkinter import messagebox
from tkinter import ttk

gui_tkinter = Tk()
gui_tkinter.geometry("1350x750+0+0")
gui_tkinter.title('Tic-Tac-Toe: Single Player')

tops = Frame(gui_tkinter,pady = 2, width = 1350, heigh=100, relief= FLAT)
tops.grid(row=0, column=0)

label_title = Label(tops, font = ("Century Gothic", 26, 'bold'), text ="Tic-Tac-Toe: Single Player", fg="#EDAA7C", justify =CENTER)
label_title.grid(row=0, column=0)

principal_frame = Frame(gui_tkinter, bg = "#ffffff", pady= 2, width = 1350, height=600, relief=FLAT)
principal_frame.grid(row=1, column=0)

left_frame = Frame(principal_frame, bd=10, width=750, height= 500, pady=2, padx=10, bg="#ffffff",relief=FLAT)
left_frame.pack(side=LEFT)

right_frame = Frame(principal_frame, bd=10, width=560, height= 500, pady=2, padx=10, bg="#ffffff", relief=FLAT)
right_frame.pack(side=RIGHT)

right_frame_= Frame(right_frame, bd=10, width=560, height= 200, pady=2, padx=10, bg="#ffffff", relief=FLAT)
right_frame_.grid(row=0, column=0)

right_frame__= Frame(right_frame, bd=10, width=560, height= 200, pady=2, padx=10, bg="#ffffff", relief=FLAT)
right_frame__.grid(row=1, column=0)

points_player_x = IntVar()
points_player_o = IntVar()

points_player_o.set(0)
points_player_x.set(0)

buttons = StringVar()

clicked = True

def reset():
    btn1["text"]= " "
    btn2["text"]= " "
    btn3["text"]= " "
    btn4["text"]= " "
    btn5["text"]= " "
    btn6["text"]= " "
    btn7["text"]= " "
    btn8["text"]= " "
    btn9["text"]= " "
    enable_move()
    

def new_game():
    reset()
    points_player_o.set(0)
    points_player_x.set(0)

def btn_clicked(btn):
    global clicked, counter
    counter=0
    if btn["text"] == " " and clicked == True: # X starts
        btn["text"] = "X"
        clicked = False
        counter+=1
        who_won()

    elif btn["text"] == " " and clicked == False:
        btn["text"] = "O"
        clicked = True
        counter+=1
        who_won()
    else:
        messagebox.showinfo("Tic-Tac-Toe: Game information", "Choose another cell")

#Labels for player X and O score
label_for_player_x = Label(right_frame_, font=("Century Gothic", 20, 'bold'),text="Player X - score: ", fg="#000000", padx=2, pady=2, bg="#ffffff" )
label_for_player_x.grid(row=0,column=0, sticky=W)
entry_for_player_x= ttk.Entry(right_frame_, font=("Century Gothic", 20, 'bold'),foreground='black', textvariable=points_player_x, width =14, justify=LEFT).grid(row=0,column=1)

label_for_player_o = Label(right_frame_, font=("Century Gothic", 20, 'bold'),text="Player O - score: ",fg="#000000", padx=2, pady=2, bg="#ffffff" )
label_for_player_o.grid(row=1,column=0, sticky=W)
entry_for_player_o= ttk.Entry(right_frame_, font=("Century Gothic", 20, 'bold'), foreground='black', textvariable=points_player_o, width =14, justify=LEFT).grid(row=1,column=1)

#Buttons for reset and new game
btn_reset= Button(right_frame__, text="Reset game", font=("Century Gothic", 16, 'bold'), height = 2, width=20, bg="#7D7F7D", fg = "#ffffff", command=reset)
btn_reset.grid(row=2,column=0, pady=11, sticky=S+N+E+W)

btn_new_game= Button(right_frame__, text="New game", font=("Century Gothic", 16, 'bold'), height = 2, width=20, bg="#7D7F7D",fg = "#ffffff", command=new_game )
btn_new_game.grid(row=3,column=0, pady=11, sticky=S+N+E+W)



btn1= Button(left_frame, text=" ", font=("Century Gothic", 40, 'bold'), height = 3, width=6,bg='gainsboro', command= lambda: btn_clicked(btn1))
btn2= Button(left_frame, text=" ", font=("Century Gothic", 40, 'bold'), height = 3, width=6,bg='gainsboro', command= lambda: btn_clicked(btn2))
btn3= Button(left_frame, text=" ", font=("Century Gothic", 40, 'bold'), height = 3, width=6,bg='gainsboro', command= lambda: btn_clicked(btn3))

btn4= Button(left_frame, text=" ", font=("Century Gothic", 40, 'bold'), height = 3, width=6,bg='gainsboro', command= lambda: btn_clicked(btn4))
btn5= Button(left_frame, text=" ", font=("Century Gothic", 40, 'bold'), height = 3, width=6,bg='gainsboro', command= lambda: btn_clicked(btn5))
btn6= Button(left_frame, text=" ", font=("Century Gothic", 40, 'bold'), height = 3, width=6,bg='gainsboro', command= lambda: btn_clicked(btn6))

btn7= Button(left_frame, text=" ", font=("Century Gothic", 40, 'bold'), height = 3, width=6,bg='gainsboro', command= lambda: btn_clicked(btn7))
btn8= Button(left_frame, text=" ", font=("Century Gothic", 40, 'bold'), height = 3, width=6,bg='gainsboro', command= lambda: btn_clicked(btn8))
btn9= Button(left_frame, text=" ", font=("Century Gothic", 40, 'bold'), height = 3, width=6,bg='gainsboro', command= lambda: btn_clicked(btn9))


#Grid bottons
btn1.grid(row=0, column=0, sticky = S+N+E+W)
btn2.grid(row=0, column=1, sticky = S+N+E+W)
btn3.grid(row=0, column=2, sticky = S+N+E+W)

btn4.grid(row=1, column=0, sticky = S+N+E+W)
btn5.grid(row=1, column=1, sticky = S+N+E+W)
btn6.grid(row=1, column=2, sticky = S+N+E+W)

btn7.grid(row=2, column=0, sticky = S+N+E+W)
btn8.grid(row=2, column=1, sticky = S+N+E+W)
btn9.grid(row=2, column=2, sticky = S+N+E+W)




#desable all buttons if someone won
def desable_move():
    if winner == True:
        btn1.config(state=DISABLED)
        btn2.config(state=DISABLED)
        btn3.config(state=DISABLED)
        btn4.config(state=DISABLED)
        btn5.config(state=DISABLED)
        btn6.config(state=DISABLED)
        btn7.config(state=DISABLED)
        btn8.config(state=DISABLED)
        btn9.config(state=DISABLED)

def enable_move():
    btn1.config(state=ACTIVE)
    btn2.config(state=ACTIVE)
    btn3.config(state=ACTIVE)
    btn4.config(state=ACTIVE)
    btn5.config(state=ACTIVE)
    btn6.config(state=ACTIVE)
    btn7.config(state=ACTIVE)
    btn8.config(state=ACTIVE)
    btn9.config(state=ACTIVE)
#Check who has won

def who_won():
    global winner, points_x, points_o, its_x, its_o
    winner = False
    points_o = 0

    #check values in each row
    
    if btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X":
        btn1.config(bg="#ffffff")
        btn2.config(bg="#ffffff")
        btn3.config(bg="#ffffff")
        score = float(points_player_x.get())
        total_score= (score+1)
        points_player_x.set(total_score)
        winner = True
        messagebox.showinfo("Tic-Tac-Toe: Game information", "X wins!")
        desable_move() 

    elif btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X":
        btn4.config(bg="#ffffff")
        btn5.config(bg="#ffffff")
        btn6.config(bg="#ffffff")
        score = float(points_player_x.get())
        total_score= (score+1)
        points_player_x.set(total_score)
        winner = True
        
        messagebox.showinfo("Tic-Tac-Toe: Game information", "X wins!")
        desable_move()

    elif btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X":
        btn7.config(bg="#ffffff")
        btn8.config(bg="#ffffff")
        btn9.config(bg="#ffffff")
        score = float(points_player_x.get())
        total_score= (score+1)
        points_player_x.set(total_score)
        winner = True
        
        messagebox.showinfo("Tic-Tac-Toe: Game information", "X wins!")
        desable_move() 
    #check values in each column

    elif btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X":
        btn1.config(bg="#ffffff")
        btn4.config(bg="#ffffff")
        btn7.config(bg="#ffffff")
        score = float(points_player_x.get())
        total_score= (score+1)
        points_player_x.set(total_score)
        winner = True
        
        messagebox.showinfo("Tic-Tac-Toe: Game information", "X wins!")
        desable_move() 

    elif btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X":
        btn2.config(bg="#ffffff")
        btn5.config(bg="#ffffff")
        btn8.config(bg="#ffffff")
        score = float(points_player_x.get())
        total_score= (score+1)
        points_player_x.set(total_score)
        winner = True
        
        messagebox.showinfo("Tic-Tac-Toe: Game information", "X wins!")
        desable_move() 
    
    elif btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X":
        btn3.config(bg="#ffffff")
        btn6.config(bg="#ffffff")
        btn9.config(bg="#ffffff")
        score = float(points_player_x.get())
        total_score= (score+1)
        points_player_x.set(total_score)
        winner = True
        
        messagebox.showinfo("Tic-Tac-Toe: Game information", "X wins!")
        desable_move() 
    
    #Check diagonals
    elif btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X":
        btn1.config(bg="#ffffff")
        btn5.config(bg="#ffffff")
        btn9.config(bg="#ffffff")
        score = float(points_player_x.get())
        total_score= (score+1)
        points_player_x.set(total_score)
        winner = True
        
        messagebox.showinfo("Tic-Tac-Toe: Game information", "X wins!")
        desable_move() 

    elif btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X":
        btn3.config(bg="#ffffff")
        btn5.config(bg="#ffffff")
        btn7.config(bg="#ffffff")
        score = float(points_player_x.get())
        total_score= (score+1)
        points_player_x.set(total_score)
        winner = True
        
        messagebox.showinfo("Tic-Tac-Toe: Game information", "X wins!")
        desable_move() 

    #The same for o's

    elif btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O":
        btn1.config(bg="#ffffff")
        btn2.config(bg="#ffffff")
        btn3.config(bg="#ffffff")
        score = float(points_player_o.get())
        total_score= (score+1)
        points_player_o.set(total_score)
        winner = True
        
        messagebox.showinfo("Tic-Tac-Toe: Game information", "O wins!")
        desable_move() 

    elif btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O":
        btn4.config(bg="#ffffff")
        btn5.config(bg="#ffffff")
        btn6.config(bg="#ffffff")
        score = float(points_player_o.get())
        total_score= (score+1)
        points_player_o.set(total_score)
        winner = True
        
        messagebox.showinfo("Tic-Tac-Toe: Game information", "O wins!")
        desable_move() 

    elif btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O":
        btn7.config(bg="#ffffff")
        btn8.config(bg="#ffffff")
        btn9.config(bg="#ffffff")
        score = float(points_player_o.get())
        total_score= (score+1)
        points_player_o.set(total_score)
        winner = True
        
        messagebox.showinfo("Tic-Tac-Toe: Game information", "O wins!")
        desable_move() 

    #check values in each column

    elif btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O":
        btn1.config(bg="#ffffff")
        btn4.config(bg="#ffffff")
        btn7.config(bg="#ffffff")
        score = float(points_player_o.get())
        total_score= (score+1)
        points_player_o.set(total_score)
        winner = True
        
        messagebox.showinfo("Tic-Tac-Toe: Game information", "O wins!")
        desable_move() 

    elif btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"] == "O":
        btn2.config(bg="#ffffff")
        btn5.config(bg="#ffffff")
        btn8.config(bg="#ffffff")
        score = float(points_player_o.get())
        total_score= (score+1)
        points_player_o.set(total_score)
        winner = True
        
        messagebox.showinfo("Tic-Tac-Toe: Game information", "O wins!")
        desable_move()
    
    elif btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O":
        btn3.config(bg="#ffffff")
        btn6.config(bg="#ffffff")
        btn9.config(bg="#ffffff")
        score = float(points_player_o.get())
        total_score= (score+1)
        points_player_o.set(total_score)
        winner = True
        
        messagebox.showinfo("Tic-Tac-Toe: Game information", "O wins!")
        desable_move()
    
    #Check diagonals
    elif btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O":
        btn1.config(bg="#ffffff")
        btn5.config(bg="#ffffff")
        btn9.config(bg="#ffffff")
        score = float(points_player_o.get())
        total_score= (score+1)
        points_player_o.set(total_score)
        winner = True
        
        messagebox.showinfo("Tic-Tac-Toe: Game information", "O wins!")
        desable_move()

    elif btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O":
        btn3.config(bg="#ffffff")
        btn5.config(bg="#ffffff")
        btn7.config(bg="#ffffff")
        score = float(points_player_o.get())
        total_score= (score+1)
        points_player_o.set(total_score)
        winner = True
        
        messagebox.showinfo("Tic-Tac-Toe: Game information", "O wins!")
        desable_move()
    
    else:
        if counter == 9:
            messagebox.showinfo("Tic-Tac-Toe: Game information", "Nobody won. Try again.")
            desable_move()







#Menu
#top_bar_menu = tk.Menu(gui_tkinter)
#gui_tkinter.config(menu = top_bar_menu)

#Menu options

#menu_options = tk.Menu(top_bar_menu, tearoff = False)
#top_bar_menu.add_cascade(label= "Opciones", menu= menu_options)
#top_bar_menu.add_separator()
#menu_options.add_command(label="Reiniciar Juego", command = reset)


#Menu options

#player_x = tk.Menu(top_bar_menu, tearoff = False)
#top_bar_menu.add_command(label= "Jugador X", command = lambda: calculate_points())
#player_x.add_command(label="Puntaje Acumulado", command = lambda: calculate_points())

#reset()
gui_tkinter.mainloop()