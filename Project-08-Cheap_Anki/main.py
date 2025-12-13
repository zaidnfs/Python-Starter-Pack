from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
#words
try:
    df = pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/japanese.csv")
    words_data = df.to_dict(orient="records")
else:
    words_data = df.to_dict(orient="records")


def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(words_data)
    word = random_word["Japanese"]
    canvas.itemconfig(card_title, text="Japanese", fill="black")
    canvas.itemconfig(card_word, text=word, fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(15000, func=answer)

#Translation
def answer():
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_word, text=random_word["English"], fill="White")
    canvas.itemconfig(card_background, image=card_back)

def is_known():
    words_data.remove(random_word)
    to_learn = pandas.DataFrame(words_data)
    to_learn.to_csv("data/word_to_learn.csv", index=False)
    next_card()

#windows
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(15000, func=answer)

#Canvas
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


#Buttons
check_image = PhotoImage(file="images/right.png")
known_image = Button(image=check_image, highlightthickness=0, borderwidth=0, command=is_known)
known_image.grid(row=1, column=1)

cross_image = PhotoImage(file="images/wrong.png")
unknown_image = Button(image=cross_image, highlightthickness=0, borderwidth=0, command=next_card)
unknown_image.grid(row=1, column=0)

next_card()








window.mainloop()
