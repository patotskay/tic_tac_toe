import tkinter as tk
from tkinter import PhotoImage 

root = tk.Tk()
#root.geometry('400x400')
root.title('Крестики-нолики')
icon = PhotoImage(file='misc/images/icon.png')
root.iconphoto(False, icon)

buttons = []
current_player = 'X' # первый ходит X

def check_winner():

    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # горизонтальные линии
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # вертикальные линии
        [0, 4, 8], [2, 4, 6]             # диагонали
    ]

    for combo in winning_combinations:
        a, b, c = combo
        if buttons[a]['text'] == buttons[b]['text'] == buttons[c]['text'] != '':
            buttons[a].config(bg='lightgreen')
            buttons[b].config(bg='lightgreen')
            buttons[c].config(bg='lightgreen')
            return True
    return False
    
def on_click(index):
    global current_player
    if buttons[index]['text'] == '':
        buttons[index]['text'] = current_player

        if check_winner():
            print(f"Победил {current_player}!")
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
        command=lambda idx=i: on_click(idx) # при клике вызовет on_click(i) 
    )
    button.grid(row=i//3, column=i%3)
    buttons.append(button)


root.mainloop()