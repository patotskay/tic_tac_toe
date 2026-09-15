import tkinter as tk
from tkinter import PhotoImage 

root = tk.Tk()
#root.geometry('400x400')
root.title('Крестики-нолики')
icon = PhotoImage(file='misc/images/icon.png')
root.iconphoto(False, icon)

buttons = []
current_player = 'X' #Первый ходит X

def on_click(index):
    global current_player
    if buttons[index]['text'] == '':
        buttons[index]['text'] = current_player

    if current_player == 'X':
        current_player = '0'
    else:
        current_player = 'X'

for i in range(9):
    button = tk.Button(
        root,
        text='',
        font=("Arial", 30),
        width=5,
        height=2,
        command=lambda idx=i: on_click(idx) # При клике вызовет on_click(i) 
    )
    button.grid(row=i//3, column=i%3)
    buttons.append(button)


root.mainloop()