import socket
import threading
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

gui_tkinter= Tk() 
gui_tkinter.title('Tic-Tac-Toe: Player 2')
gui_tkinter.geometry("1000x540+0+0")



host = '127.0.0.1'  # Standard loopback interface address (localhost)
port = 65432 


points_client = IntVar()
points_client_o= IntVar()
points_client.set(0)
points_client_o.set(0)

cell = " "
turn=False




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



#Labels for player X and O score
label_for_player_x = Label(right_frame_, font=("Century Gothic", 16, 'bold'),text="Player X - score: ", fg="#000000", padx=2, pady=2, bg="#ffffff" )
label_for_player_x.grid(row=0,column=0, sticky=W)
entry_for_player_x= ttk.Entry(right_frame_, font=("Century Gothic", 16, 'bold'),foreground='black', width =10, textvariable=points_client, justify=LEFT).grid(row=0,column=1)

label_for_player_o = Label(right_frame_, font=("Century Gothic", 16, 'bold'),text="Player O - score: ",fg="#000000", padx=2, pady=2, bg="#ffffff" )
label_for_player_o.grid(row=1,column=0, sticky=W)
entry_for_player_o= ttk.Entry(right_frame_, font=("Century Gothic", 16, 'bold'), foreground='black', width =10,textvariable=points_client_o, justify=LEFT).grid(row=1,column=1)



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))


def create_thread(targett):
    thread = threading.Thread(target=targett)
    thread.daemon = True
    thread.start()

def update():
    if cell == '1':
        btn_clicked1()
    elif cell == '2':
        btn_clicked2()
    elif cell == '3':
        btn_clicked3()
    elif cell == '4':
        btn_clicked4()
    elif cell == '5':
        btn_clicked5()
    elif cell == '6':
        btn_clicked6()
    elif cell == '7':
        btn_clicked7()
    elif cell == '8':
        btn_clicked8()
    elif cell == '9':
        btn_clicked9()
    else:
        print("No matching char detected")  


def recieve_info():
    global turn
    global cell
    while True:
        data, addr = s.recvfrom(1024)
        data2 = data.decode()
        dataa = data2.split('-')
        cell = dataa[0]
        update()
        if dataa[1] == 'playerturn':
            print(cell+" "+"client turn")
            turn = True
            print("client turn ="+" "+ str(turn))
        if not dataa:
            s.close 
            break     

create_thread(recieve_info)


print(cell)
print("client turn = "+ str(turn))


def btn_clicked1():
    global turn
    global cell
    if turn == True and btn1["text"] == " ":
        btn1["text"]="O"
        send_data = '{}-{}'.format('1', 'playerturn').encode()
        s.send(send_data)
        print(send_data)
        turn=False
        check()
    elif turn == False and btn1["text"]==" " and cell == '1':
        btn1["text"] = "X"
        turn = True
        check()

def btn_clicked2():
    global turn
    global cell
    if turn == True and btn2["text"] == " ":
        btn2["text"]="O"
        send_data = '{}-{}'.format('2', 'playerturn').encode()
        s.send(send_data)
        print(send_data)
        turn=False
        check()
    elif turn == False and btn2["text"]== " " and cell == '2':
        btn2["text"] = "X"
        turn = True
        check()

def btn_clicked3():
    global turn
    global cell
    if turn and btn3["text"] == " ":
        btn3["text"]="O"
        send_data = '{}-{}'.format('3', 'playerturn').encode()
        s.send(send_data)
        print(send_data)
        turn=False
        check()
    elif turn == False and btn3["text"]== " " and cell == '3':
        btn3["text"] = "X"
        turn = True
        check()

def btn_clicked4():
    global turn
    global cell
    if turn and btn4["text"] == " ":
        btn4["text"]="O"
        send_data = '{}-{}'.format('4', 'playerturn').encode()
        s.send(send_data)
        print(send_data)
        turn=False
        check()
    elif turn == False and btn4["text"]== " " and cell == '4':
        btn4["text"] = "X"
        turn = True
        check()

def btn_clicked5():
    global turn
    global cell
    if turn and btn5["text"] == " ":
        btn5["text"]="O"
        send_data = '{}-{}'.format('5', 'playerturn').encode()
        s.send(send_data)
        print(send_data)
        turn=False
        check()
    elif turn == False and btn5["text"]== " " and cell == '5':
        btn5["text"] = "X"
        turn = True
        check()

def btn_clicked6():
    global turn
    global cell
    if turn and btn6["text"] == " ":
        btn6["text"]="O"
        send_data = '{}-{}'.format('6', 'playerturn').encode()
        s.send(send_data)
        print(send_data)
        turn=False
        check()
    elif turn == False and btn6["text"]== " " and cell == '6':
        btn6["text"] = "X"
        turn = True
        check()

def btn_clicked7():
    global turn
    global cell
    if turn and btn7["text"] == " ":
        btn7["text"]="O"
        send_data = '{}-{}'.format('7', 'playerturn').encode()
        s.send(send_data)
        print(send_data)
        turn=False
        check()
    elif turn == False and btn7["text"]== " " and cell == '7':
        btn7["text"] = "X"
        turn = True
        check()

def btn_clicked8():
    global turn
    global cell
    if turn and btn8["text"] == " ":
        btn8["text"]="O"
        send_data = '{}-{}'.format('8', 'playerturn').encode()
        s.send(send_data)
        print(send_data)
        turn=False
        check()
    elif turn == False and btn8["text"]== " " and cell == '8':
        btn8["text"] = "X"
        turn = True
        check()

def btn_clicked9():
    global turn
    global cell
    if turn == True and btn9["text"] == " ":
        btn9["text"]="O"
        send_data = '{}-{}'.format('9', 'playerturn').encode()
        s.send(send_data)
        print(send_data)
        turn=False
        check()
    elif turn == False and btn9["text"]== " " and cell == '9':
        btn9["text"] = "X"
        turn = True
        check()


def reset():
    global flag
    flag = 0
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


flag = 0

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

    #rows
    if  btn1_2 == btn2_2 and btn1_2==btn3_2 and btn1_2=="O" or btn1_2 == btn2_2 and btn1_2==btn3_2 and btn1_2 == "X":
        win(btn1["text"])
    elif  btn4_2 == btn5_2 and btn4_2==btn6_2 and btn4_2=="O" or btn4_2 == btn5_2 and btn4_2==btn6_2 and btn4_2 == "X":
        win(btn4["text"])
    elif  btn7_2 == btn8_2 and btn7_2== btn9_2 and btn7_2 == "O" or btn7_2 == btn8_2 and btn7_2 == btn9_2 and btn7_2 == "X":
        win(btn7["text"])
    #columns     
    elif  btn1_2 == btn4_2 and btn1_2== btn7_2 and btn1_2 == "O" or btn1_2 == btn4_2 and btn1_2 == btn7_2 and btn1_2 == "X":
        win(btn1["text"])    
    elif  btn2_2 == btn5_2 and btn2_2== btn8_2 and btn2_2 == "O" or btn2_2 == btn5_2 and btn2_2 == btn8_2 and btn2_2 == "X":
        win(btn2["text"])  
    elif  btn3_2 == btn6_2 and btn3_2== btn9_2 and btn3_2 == "O" or btn3_2 == btn6_2 and btn3_2 == btn9_2 and btn3_2 == "X":
        win(btn3["text"])
    #Diagonal buttons      
    elif  btn1_2 == btn5_2 and btn1_2== btn9_2 and btn1_2 == "O" or btn1_2 == btn5_2 and btn1_2 == btn9_2 and btn1_2 == "X":
        win(btn1["text"])
    #Diagonal buttons    
    elif  btn7_2 == btn5_2 and btn7_2== btn3_2 and btn7_2 == "O" or btn7_2 == btn5_2 and btn7_2 == btn3_2 and btn7_2 == "X":
        win(btn7["text"])
    else:
        if flag > 9:
            messagebox.showinfo("Tic-Tac-Toe: Game information", "Nobody won. Try Again. ")
            gui_tkinter.destroy()
    
def win(player):
    if player =="X":
        score = float(points_client.get())
        total_score= (score+1)
        points_client.set(total_score)

    elif player =="O":
        score = float(points_client_o.get())
        total_score= (score+1)
        points_client_o.set(total_score)
    
    desable_move()
    msj = ("The winner is:"+" "+player)
    messagebox.showinfo("Tic-Tac-Toe: Game information", msj)
    reset()  

def desable_move():
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
    check()
    

btn1= Button(left_frame, text=" ", font=("Century Gothic", 30, 'bold'), height = 3, width=4,bg='gainsboro', command= btn_clicked1)
btn2= Button(left_frame, text=" ", font=("Century Gothic", 30, 'bold'), height = 3, width=4,bg='gainsboro', command= btn_clicked2)
btn3= Button(left_frame, text=" ", font=("Century Gothic", 30, 'bold'), height = 3, width=4,bg='gainsboro', command= btn_clicked3)

btn4= Button(left_frame, text=" ", font=("Century Gothic", 30, 'bold'), height = 3, width=4,bg='gainsboro', command= btn_clicked4)
btn5= Button(left_frame, text=" ", font=("Century Gothic", 30, 'bold'), height = 3, width=4,bg='gainsboro', command= btn_clicked5)
btn6= Button(left_frame, text=" ", font=("Century Gothic", 30, 'bold'), height = 3, width=4,bg='gainsboro', command= btn_clicked6)

btn7= Button(left_frame, text=" ", font=("Century Gothic", 30, 'bold'), height = 3, width=4,bg='gainsboro', command= btn_clicked7)
btn8= Button(left_frame, text=" ", font=("Century Gothic", 30, 'bold'), height = 3, width=4,bg='gainsboro', command= btn_clicked8)
btn9= Button(left_frame, text=" ", font=("Century Gothic", 30, 'bold'), height = 3, width=4,bg='gainsboro', command= btn_clicked9)


btn1.grid(row=0, column=0, sticky = S+N+E+W)
btn2.grid(row=0, column=1, sticky = S+N+E+W)
btn3.grid(row=0, column=2, sticky = S+N+E+W)

btn4.grid(row=1, column=0, sticky = S+N+E+W)
btn5.grid(row=1, column=1, sticky = S+N+E+W)
btn6.grid(row=1, column=2, sticky = S+N+E+W)

btn7.grid(row=2, column=0, sticky = S+N+E+W)
btn8.grid(row=2, column=1, sticky = S+N+E+W)
btn9.grid(row=2, column=2, sticky = S+N+E+W)


gui_tkinter.mainloop()