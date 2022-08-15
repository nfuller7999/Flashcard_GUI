from tkinter import *
import pandas as pd
import random
from os.path import exists

if exists("data/words_to_learn.csv") == True:
    data = pd.read_csv("data/words_to_learn.csv")
else:
    data = pd.read_csv("data/french_words.csv")
dict1 = data.to_dict(orient="records")
BACKGROUND_COLOR = "#B1DDC6"
rand_choice = {}

def check():
    dict1.remove(rand_choice)
    change_word()
  

def change_word():
    global rand_choice,flip_timer
    
    rand_choice = random.choice(dict1)
    
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image,image=card_front)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(word,text=rand_choice["French"],fill="black")
    flip_timer = window.after(3000, func=change)
    
    

def change():
    canvas.itemconfig(canvas_image,image=card_back)
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(word,text=rand_choice["English"],fill="white")



window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=change)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
x_box = PhotoImage(file="images/wrong.png")
check_box = PhotoImage(file="images/right.png")

canvas = Canvas(width=800,height=526,highlightthickness=0)
canvas_image = canvas.create_image(400,263,image=card_front)
canvas.config(bg=BACKGROUND_COLOR)
title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)
x_button = Button(window,image=x_box,highlightthickness=0,command=change_word)
x_button.grid(column=1,row=1)
check_button = Button(window,image=check_box,highlightthickness=0,command=check)
check_button.grid(column=0,row=1)

change_word()


window.mainloop()
df = pd.DataFrame.from_dict(dict1)
df.to_csv("data/words_to_learn.csv", index=False)






