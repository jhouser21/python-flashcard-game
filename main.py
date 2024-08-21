from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    orig_data = pandas.read_csv("french_words.csv")
    to_learn = orig_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=back_img)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="card_front.png")
back_img = PhotoImage(file="card_back.png")
card_bg = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

x_img = PhotoImage(file="wrong.png")
x_button = Button(image=x_img, highlightthickness=0, command=next_card)
x_button.grid(column=0, row=1)

y_img = PhotoImage(file="right.png")
y_button = Button(image=y_img, highlightthickness=0, command=is_known)
y_button.grid(column=1, row=1)

next_card()

window.mainloop()