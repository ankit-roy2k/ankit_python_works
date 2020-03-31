from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.title("Tic Tac toe")
turn=True
n = 9
btns = []
board=[i for i in range(9)]
count=0
player=1
Game=False

def onclick(button):
    global count
    global turn
    global player
    button.config(state="disabled")
    
    if turn:
        player=1
        sign="X"
        button.config(text=sign,bg='yellow',fg='white')
        board[btns.index(button)]=sign
        #print(board)
        
    else:
        player=2
        sign="O"
        button.config(text=sign,bg='cyan',fg='white')
        board[btns.index(button)]=sign
        #print(board)

    if count<=8 and check_win()[-1]:
        a,b,c,d=check_win()
        btns[a].config(bg='red',fg='white')
        btns[b].config(bg='red',fg='white')
        btns[c].config(bg='red',fg='white')
        messagebox.showinfo("Game Over!!",f"Player{player} won!!")
        tk.destroy()
    elif count>=8 and not(check_win()[-1]):
        messagebox.showinfo("Game Over!!",f"It's a Tie!!")
        tk.destroy()
    else:
        count+=1
    turn=not(turn)


def check_win():
    global Game
    #Horizontal Winning Condition
    if(board[0] == board[1] and board[1] == board[2]):    
        Game=0,1,2,True    #tuple
    elif(board[3] == board[4] and board[4] == board[5]):    
        Game=3,4,5,True    #tuple
    elif(board[6] == board[7] and board[7] == board[8]):    
        Game=6,7,8,True    #tuple
    #Vertical Winning Condition    
    elif(board[0] == board[3] and board[3] == board[6]):    
        Game=0,3,6,True    #tuple
    elif(board[1] == board[4] and board[4] == board[7]):    
        Game=1,4,7,True    #tuple
    elif(board[2] == board[5] and board[5] == board[8]):    
        Game=2,5,8,True    #tuple
    #Diagonal Winning Condition    
    elif(board[0] == board[4] and board[4] == board[8]):    
        Game=0,4,8,True    #tuple
    elif(board[2] == board[4] and board[4] == board[6]):    
        Game=2,4,6,True    #tuple
    else:
        Game=[False]
    return Game 

def create_board():
    for i in range(9):
        btns.append(Button(font=('Times 20 bold'),bg='white', fg='white', padx=25, pady=25, height=2, width=4))
    
    row = 1
    column = 0
    index = 1
    for i in range(9):
        btns[i].grid(row=row, column=column)
        btns[i].config(command=lambda current_button=btns[i]: onclick(current_button))
        column += 1
        if index % 3 == 0:
            row += 1
            column = 0
        index += 1

def start_game():
    create_board()
    tk.mainloop()

start_game()
