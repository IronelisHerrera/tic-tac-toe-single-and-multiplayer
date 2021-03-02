import socket
import threading
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

gui_tkinter= Tk() 
cell = " "
turn=False
host = '127.0.0.1'  # Standard loopback interface address (localhost)
port = 65432 

gui_tkinter.title('Tic-Tac-Toe: Player 2')
gui_tkinter.geometry("1000x540+0+0")

tops = Frame(gui_tkinter,pady = 2, width = 1350, heigh=100, relief= FLAT)
tops.grid(row=0, column=0)

label_title = Label(tops, font = ("Century Gothic", 20, 'bold'), text ="Player 2: O", fg="#EDAA7C", justify =CENTER)
label_title.grid(row=0, column=0)


principal_frame = Frame(gui_tkinter, bg = "#ffffff", pady= 2, width = 1200, height=900, relief=FLAT)
principal_frame.grid(row=1, column=0)

left_frame = Frame(principal_frame, bd=10, width=750, height= 600, pady=2, padx=10, bg="#ffffff",relief=FLAT)
left_frame.pack(side=LEFT)

right_frame = Frame(principal_frame, bd=10, width=560, height= 500, pady=2, padx=10, bg="#ffffff", relief=FLAT)
right_frame.pack(side=RIGHT)

right_frame_= Frame(right_frame, bd=10, width=560, height= 200, pady=2, padx=10, bg="#ffffff", relief=FLAT)
right_frame_.grid(row=0, column=0)

right_frame__= Frame(right_frame, bd=10, width=560, height= 200, pady=2, padx=10, bg="#ffffff", relief=FLAT)
right_frame__.grid(row=1, column=0)



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

def update():
    if cell == 'A':
        btn_clicked1()
    elif cell == 'B':
        btn_clicked2()
    elif cell == 'C':
        btn_clicked3()
    elif cell == 'D':
        btn_clicked4()
    elif cell == 'E':
        btn_clicked5()
    elif cell == 'F':
        btn_clicked6()
    elif cell == 'G':
        btn_clicked7()
    elif cell == 'H':
        btn_clicked8()
    elif cell == 'I':
        btn_clicked9()
    else:
        print("No matching char detected")  

def create_thread(targett):
    thread = threading.Thread(target=targett)
    thread.daemon = True
    thread.start()

def recieveData():
    global turn
    global cell
    while True:
        data, addr = s.recvfrom(1024)
        data2 = data.decode()
        dataa = data2.split('-')
        cell = dataa[0]
        update()
        if dataa[1] == 'YourTurn':
            print(cell+ "client turn")
            turn = True
            print("client turn ="+ str(turn))

create_thread(recieveData)



host= '127.0.0.1'
port = 65535


print(cell)

print("client turn = "+ str(turn))

#Por ahi

def btn_clicked1():
    global turn
    global cell
    if turn == True and btn1["text"] == " ":
        btn1["text"]="O"
        send_data = '{}-{}'.format('A', 'YourTurn').encode()
        s.send(send_data)
        print(send_data)
        turn=False
        check()
    elif turn == False and btn1["text"]==" " and cell == 'A':
        btn1["text"] = "X"
        turn = True
        check()

def btn_clicked2():
    global turn
    global cell
    if turn == True and btn2["text"] == " ":
        btn2["text"]="O"
        send_data = '{}-{}'.format('B', 'YourTurn').encode()
        s.send(send_data)
        print(send_data)
        turn=False
        check()
    elif turn == False and btn2["text"]== " " and cell == 'B':
        btn2["text"] = "X"
        turn = True
        check()

def btn_clicked3():
    global turn
    global cell
    if turn and btn3["text"] == " ":
        btn3["text"]="O"
        send_data = '{}-{}'.format('C', 'YourTurn').encode()
        s.send(send_data)
        print(send_data)
        turn=False
        check()
    elif turn == False and btn3["text"]== " " and cell == 'C':
        btn3["text"] = "X"
        turn = True
        check()

def btn_clicked4():
    global turn
    global cell
    if turn and btn4["text"] == " ":
        btn4["text"]="O"
        send_data = '{}-{}'.format('D', 'YourTurn').encode()
        s.send(send_data)
        print(send_data)
        turn=False
        check()
    elif turn == False and btn4["text"]== " " and cell == 'D':
        btn4["text"] = "X"
        turn = True
        check()

def btn_clicked5():
    global turn
    global cell
    if turn and btn5["text"] == " ":
        btn5["text"]="O"
        send_data = '{}-{}'.format('E', 'YourTurn').encode()
        s.send(send_data)
        print(send_data)
        turn=False
        check()
    elif turn == False and btn5["text"]== " " and cell == 'E':
        btn5["text"] = "X"
        turn = True
        check()


def btn_clicked6():
    global turn
    global cell
    if turn and btn6["text"] == " ":
        btn6["text"]="O"
        send_data = '{}-{}'.format('F', 'YourTurn').encode()
        s.send(send_data)
        print(send_data)
        turn=False
        check()
    elif turn == False and btn6["text"]== " " and cell == 'F':
        btn6["text"] = "X"
        turn = True
        check()

def btn_clicked7():
    global turn
    global cell
    if turn and btn7["text"] == " ":
        btn7["text"]="O"
        send_data = '{}-{}'.format('G', 'YourTurn').encode()
        s.send(send_data)
        print(send_data)
        turn=False
        check()
    elif turn == False and btn7["text"]== " " and cell == 'G':
        btn7["text"] = "X"
        turn = True
        check()

def btn_clicked8():
    global turn
    global cell
    if turn and btn8["text"] == " ":
        btn8["text"]="O"
        send_data = '{}-{}'.format('H', 'YourTurn').encode()
        s.send(send_data)
        print(send_data)
        turn=False
        check()
    elif turn == False and btn8["text"]== " " and cell == 'H':
        btn8["text"] = "X"
        turn = True
        check()

def btn_clicked9():
    global turn
    global cell
    if turn == True and btn9["text"] == " ":
        btn9["text"]="O"
        send_data = '{}-{}'.format('I', 'YourTurn').encode()
        s.send(send_data)
        print(send_data)
        turn=False
        check()
    elif turn == False and btn9["text"]== " " and cell == 'I':
        btn9["text"] = "X"
        turn = True
        check()

def reset():
    pass

def new_game():
    pass



#Labels for player X and O score
label_for_player_x = Label(right_frame_, font=("Century Gothic", 16, 'bold'),text="Player X - score: ", fg="#000000", padx=2, pady=2, bg="#ffffff" )
label_for_player_x.grid(row=0,column=0, sticky=W)
entry_for_player_x= ttk.Entry(right_frame_, font=("Century Gothic", 16, 'bold'),foreground='black', width =10, justify=LEFT).grid(row=0,column=1)

label_for_player_o = Label(right_frame_, font=("Century Gothic", 16, 'bold'),text="Player O - score: ",fg="#000000", padx=2, pady=2, bg="#ffffff" )
label_for_player_o.grid(row=1,column=0, sticky=W)
entry_for_player_o= ttk.Entry(right_frame_, font=("Century Gothic", 16, 'bold'), foreground='black', width =10, justify=LEFT).grid(row=1,column=1)

#Buttons for reset and new game
btn_reset= Button(right_frame__, text="Reset game", font=("Century Gothic", 16, 'bold'), height = 2, width=20, bg="#7D7F7D", fg = "#ffffff", command=reset)
btn_reset.grid(row=2,column=0, pady=11, sticky=S+N+E+W)

btn_new_game= Button(right_frame__, text="New game", font=("Century Gothic", 16, 'bold'), height = 2, width=20, bg="#7D7F7D",fg = "#ffffff", command=new_game )
btn_new_game.grid(row=3,column=0, pady=11, sticky=S+N+E+W)


flag = 1

def check():
    global flag
    btn1_2= btn1["text"]
    btn2_2= btn2["text"]
    btn3_2= btn3["text"]
    btn4_2= btn4["text"]
    btn5_2= btn5["text"]
    btn6_2= btn6["text"]
    btn7_2= btn7["text"]
    btn8_2= btn8["text"]
    btn9_2= btn9["text"]
    flag+=1
    if  btn1_2 == btn2_2 and btn1_2==btn3_2 and btn1_2=="O" or btn1_2 == btn2_2 and btn1_2==btn3_2 and btn1_2 == "X":
        win(btn1["text"])
    if  btn4_2 == btn5_2 and btn4_2==btn6_2 and btn4_2=="O" or btn4_2 == btn5_2 and btn4_2==btn6_2 and btn4_2 == "X":
        win(btn4["text"])
    if  btn7_2 == btn8_2 and btn7_2== btn9_2 and btn7_2 == "O" or btn7_2 == btn8_2 and btn7_2 == btn9_2 and btn7_2 == "X":
        win(btn7["text"])

    if  btn1_2 == btn4_2 and btn1_2== btn7_2 and btn1_2 == "O" or btn1_2 == btn4_2 and btn1_2 == btn7_2 and btn1_2 == "X":
        win(btn1["text"])
    if  btn2_2 == btn5_2 and btn2_2== btn8_2 and btn2_2 == "O" or btn2_2 == btn5_2 and btn2_2 == btn8_2 and btn2_2 == "X":
        win(btn2["text"])
    if  btn3_2 == btn6_2 and btn3_2== btn9_2 and btn3_2 == "O" or btn3_2 == btn6_2 and btn3_2 == btn9_2 and btn3_2 == "X":
        win(btn3["text"])

    if  btn1_2 == btn5_2 and btn1_2== btn9_2 and btn1_2 == "O" or btn1_2 == btn5_2 and btn1_2 == btn9_2 and btn1_2 == "X":
        win(btn1["text"])
    if  btn7_2 == btn5_2 and btn7_2== btn3_2 and btn7_2 == "O" or btn7_2 == btn5_2 and btn7_2 == btn3_2 and btn7_2 == "X":
        win(btn7["text"])
    if flag == 10:
        messagebox.showinfo("Tie", "Match Tied!! Try Again :)")
        gui_tkinter.destroy()
    
def win(player):
    msj = ("The winner is:"+" "+player)
    messagebox.showinfo("Tic-Tac-Toe: Game information", msj) 
    gui_tkinter.destroy()   



btn1= Button(left_frame, text=" ", font=("Century Gothic", 40, 'bold'), height = 3, width=4,bg='gainsboro', command= btn_clicked1)
btn2= Button(left_frame, text=" ", font=("Century Gothic", 40, 'bold'), height = 3, width=4,bg='gainsboro', command= btn_clicked2)
btn3= Button(left_frame, text=" ", font=("Century Gothic", 40, 'bold'), height = 3, width=4,bg='gainsboro', command= btn_clicked3)

btn4= Button(left_frame, text=" ", font=("Century Gothic", 40, 'bold'), height = 3, width=4,bg='gainsboro', command= btn_clicked4)
btn5= Button(left_frame, text=" ", font=("Century Gothic", 40, 'bold'), height = 3, width=4,bg='gainsboro', command= btn_clicked5)
btn6= Button(left_frame, text=" ", font=("Century Gothic", 40, 'bold'), height = 3, width=4,bg='gainsboro', command= btn_clicked6)

btn7= Button(left_frame, text=" ", font=("Century Gothic", 40, 'bold'), height = 3, width=4,bg='gainsboro', command= btn_clicked7)
btn8= Button(left_frame, text=" ", font=("Century Gothic", 40, 'bold'), height = 3, width=4,bg='gainsboro', command= btn_clicked8)
btn9= Button(left_frame, text=" ", font=("Century Gothic", 40, 'bold'), height = 3, width=4,bg='gainsboro', command= btn_clicked9)


#Grid bottons
btn1.grid(row=0, column=0, sticky = E)
btn2.grid(row=0, column=1, sticky = E+W)
btn3.grid(row=0, column=2, sticky = E+W)

btn4.grid(row=1, column=0, sticky = E)
btn5.grid(row=1, column=1, sticky = E+W)
btn6.grid(row=1, column=2, sticky = E+W)

btn7.grid(row=2, column=0, sticky = E)
btn8.grid(row=2, column=1, sticky = E+W)
btn9.grid(row=2, column=2, sticky = E+W)


gui_tkinter.mainloop()