#Tic-Tac-Toe Game

from tkinter import *
from tkinter import ttk

root = Tk()      
root.title("Tic-Tac-Toe")


player_turn = 0
click_count = 0

def button_click(num):
  global player_turn, click_count
  #1
  if(num == 1):
    if(player_turn % 2 == 0):
      button1.config(text="X", fg="#283c62", activeforeground="#283c62")
    else:
      button1.config(text="O", fg="#283c62", activeforeground="#283c62")
    player_turn += 1
    click_count += 1
  #2
  elif(num == 2):
    if(player_turn % 2 == 0):
      button2.config(text="X", fg="#283c62", activeforeground="#283c62")
    else:
      button2.config(text="O", fg="#283c62", activeforeground="#283c62")
    player_turn += 1
    click_count += 1
  #3
  elif(num == 3):
    if(player_turn % 2 == 0):
      button3.config(text="X", fg="#283c62", activeforeground="#283c62")
    else:
      button3.config(text="O", fg="#283c62", activeforeground="#283c62")
    player_turn += 1
    click_count += 1
  #4
  elif(num == 4):
    if(player_turn % 2 == 0):
      button4.config(text="X", fg="#283c62", activeforeground="#283c62")
    else:
      button4.config(text="O", fg="#283c62", activeforeground="#283c62")
    player_turn += 1
    click_count += 1
  #5
  elif(num == 5):
    if(player_turn % 2 == 0):
      button5.config(text="X", fg="#283c62", activeforeground="#283c62")
    else:
      button5.config(text="O", fg="#283c62", activeforeground="#283c62")
    player_turn += 1
    click_count += 1
  #6
  elif(num == 6):
    if(player_turn % 2 == 0):
      button6.config(text="X", fg="#283c62", activeforeground="#283c62")
    else:
      button6.config(text="O", fg="#283c62", activeforeground="#283c62")
    player_turn += 1
    click_count += 1
  #7
  elif(num == 7):
    if(player_turn % 2 == 0):
      button7.config(text="X", fg="#283c62", activeforeground="#283c62")
    else:
      button7.config(text="O", fg="#283c62", activeforeground="#283c62")
    player_turn += 1
    click_count += 1
  #8
  elif(num == 8):
    if(player_turn % 2 == 0):
      button8.config(text="X", fg="#283c62", activeforeground="#283c62")
    else:
      button8.config(text="O", fg="#283c62", activeforeground="#283c62")
    player_turn += 1
    click_count += 1
  #9
  elif(num == 9):
    if(player_turn % 2 == 0):
      button9.config(text="X", fg="#283c62", activeforeground="#283c62")
    else:
      button9.config(text="O", fg="#283c62", activeforeground="#283c62")
    player_turn += 1
    click_count += 1
  
  check_winner()

#board
button1 = Button(root, text="1", height=5, width=10, font=('Comic Sans MS', 19), background="#9bb1d2", foreground="#9bb1d2", activebackground="#9bb1d2", activeforeground="#9bb1d2", command=lambda: button_click(1))

button2 = Button(root, text="2", height=5, width=10, font=('Comic Sans MS', 19), background="#9bb1d2", foreground="#9bb1d2", activebackground="#9bb1d2", activeforeground="#9bb1d2", command=lambda: button_click(2))

button3 = Button(root, text="3", height=5, width=10, font=('Comic Sans MS', 19), background="#9bb1d2", foreground="#9bb1d2", activebackground="#9bb1d2", activeforeground="#9bb1d2", command=lambda: button_click(3))

button4 = Button(root, text="4", height=5, width=10, font=('Comic Sans MS', 19), background="#9bb1d2", foreground="#9bb1d2", activebackground="#9bb1d2", activeforeground="#9bb1d2", command=lambda: button_click(4))

button5 = Button(root, text="5", height=5, width=10, font=('Comic Sans MS', 19), background="#9bb1d2", foreground="#9bb1d2", activebackground="#9bb1d2", activeforeground="#9bb1d2", command=lambda: button_click(5))

button6 = Button(root, text="6", height=5, width=10, font=('Comic Sans MS', 19), background="#9bb1d2", foreground="#9bb1d2", activebackground="#9bb1d2", activeforeground="#9bb1d2", command=lambda: button_click(6))

button7 = Button(root, text="7", height=5, width=10, font=('Comic Sans MS', 19), background="#9bb1d2", foreground="#9bb1d2", activebackground="#9bb1d2", activeforeground="#9bb1d2", command=lambda: button_click(7))

button8 = Button(root, text="8", height=5, width=10, font=('Comic Sans MS', 19), background="#9bb1d2", foreground="#9bb1d2", activebackground="#9bb1d2", activeforeground="#9bb1d2", command=lambda: button_click(8))

button9 = Button(root, text="9", height=5, width=10, font=('Comic Sans MS', 19), background="#9bb1d2", foreground="#9bb1d2", activebackground="#9bb1d2", activeforeground="#9bb1d2", command=lambda: button_click(9))



#display board
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
#play game
#handle trun
#check win
  #check rows
  #check columns
  #check diagonals
#check tie
#flip player


def player_x_wins():
  win = Tk()
  win.title("Winner!")
  win.geometry("565x495")
  canvas1 = Canvas(win, bg="#283c62", height=500, width=565)
  banner = Label(win, text="Player X wins!", font=('Comic Sans MS', 25), fg="#9bb1d2", bg="#283c62")
  canvas1.grid(row=0, column=0)
  banner.grid(row=0, column=0)
  print("Player X wins!")
  

def player_o_wins():
  win = Tk()
  win.title("Winner!")
  win.geometry("565x495")
  canvas1 = Canvas(win, bg="#283c62", height=500, width=565)
  banner = Label(win, text="Player O wins!", font=('Comic Sans MS', 25), fg="#9bb1d2", bg="#283c62")
  canvas1.grid(row=0, column=0)
  banner.grid(row=0, column=0)
  print("Player O wins!")


def cat_game():
  win = Tk()
  win.title("Winner!")
  win.geometry("565x495")
  canvas1 = Canvas(win, bg="#283c62", height=500, width=565)
  banner = Label(win, text="Cat Game!", font=('Comic Sans MS', 25), fg="#9bb1d2", bg="#283c62")
  canvas1.grid(row=0, column=0)
  banner.grid(row=0, column=0)
  print("Cat Game!")


def check_winner():
  global click_count
  #across the top
  if(button1.cget('text') == button2.cget('text') and button2.cget('text') == button3.cget('text')):
    if(button1.cget('text') == "X"):
      player_x_wins()
    else:
      player_o_wins()

  #across the middle
  elif(button4.cget('text') == button5.cget('text') and button5.cget('text') == button6.cget('text')):
    if(button4.cget('text') == "X"):
      player_x_wins()
    else:
      player_o_wins()

  #across the bottom
  elif(button7.cget('text') == button8.cget('text') and button8.cget('text') == button9.cget('text')):
    if(button7.cget('text') == "X"):
      player_x_wins()
    else:
      player_o_wins()

  #left up and down
  elif(button1.cget('text') == button4.cget('text') and button4.cget('text') == button7.cget('text')):
    if(button1.cget('text') == "X"):
      player_x_wins()
    else:
      player_o_wins()

  #middle up and down
  elif(button2.cget('text') == button5.cget('text') and button5.cget('text') == button8.cget('text')):
    if(button2.cget('text') == "X"):
      player_x_wins()
    else:
      player_o_wins()

  #right up and down
  elif(button3.cget('text') == button6.cget('text') and button6.cget('text') == button9.cget('text')):
    if(button3.cget('text') == "X"):
      player_x_wins()
    else:
      player_o_wins()
  
  #diagnal -->
  elif(button1.cget('text') == button5.cget('text') and button5.cget('text') == button9.cget('text')):
    if(button1.cget('text') == "X"):
      player_x_wins()
    else:
      player_o_wins()

  #diagnol <--
  elif(button3.cget('text') == button5.cget('text') and button5.cget('text') == button7.cget('text')):
    if(button3.cget('text') == "X"):
      player_x_wins()
    else:
      player_o_wins()

  elif(click_count == 9):
    cat_game()

root.mainloop()