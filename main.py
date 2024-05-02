from tkinter import *
import pandas as pd
import random

try:
    df = pd.read_csv('./data/words_to_learn.csv')

except FileNotFoundError:
    df = pd.read_csv('./data/french_words.csv')

finally:
    words = df.to_dict(orient="records")
    word = {}


# ---------------------------- Words Generator ------------------------------- #
def card_back(word:str):
    canvas.itemconfig(card, image=img_card_back)
    canvas.itemconfig(lbl_language, text="English",fill='white')
    canvas.itemconfig(lbl_word, text=word,fill='white')

def next_word():
    global word, flip_timer

    try:
        window.after_cancel(flip_timer)
    except:
        pass

    word = random.choice(words)
    fr = word["French"]
    eng = word["English"]
    canvas.itemconfig(card, image=img_card_front)
    canvas.itemconfig(lbl_language, text="French",fill='black')
    canvas.itemconfig(lbl_word, text=fr,fill='black')
    window.update()
    flip_timer = window.after(3_000, card_back(eng))

def remove_word():
    words.remove(word)
    new_df = pd.DataFrame(words)
    new_df.to_csv("./data/words_to_learn.csv", index=False)
    next_word()


# ---------------------------- UI SETUP ------------------------------- #

#screen
color_bg = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=color_bg)


#images
img_card_back = PhotoImage(file="images/card_back.png")
img_card_front = PhotoImage(file="images/card_front.png")
img_right = PhotoImage(file="images/right.png")
img_wrong = PhotoImage(file="images/wrong.png")


#canvas configutarion
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=color_bg)
card = canvas.create_image(400, 263, image=img_card_front)
lbl_language = canvas.create_text(400, 150, text="", font=("Arial",40,"italic"), fill="black")
lbl_word = canvas.create_text(400, 263, text="", font=("Arial",40,"bold"), fill="black")


#buttons
btn_right = Button(image=img_right, highlightthickness=0, bg=color_bg, border=0, command=remove_word)
btn_wrong = Button(image=img_wrong, highlightthickness=0, bg=color_bg, border=0, command=next_word)


#positions
canvas.grid(row=0, column=0,columnspan=2)
btn_wrong.grid(row=1,column=0)
btn_right.grid(row=1,column=1)


#Start with First Word
flip_timer = window.after(0,next_word())

window.mainloop() 