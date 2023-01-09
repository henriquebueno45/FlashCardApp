from tkinter import *
import pandas as pd
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import time

BACKGROUND_COLOR = "#B1DDC6"


def abreArquivo(path_arquivo):
    file = pd.read_csv(path_arquivo)
    return file


words_base = abreArquivo(path_arquivo="data/french_words.csv")
to_learn = words_base.to_dict(orient="records")


# Know the answer
def newWord():
    randWord = choice(to_learn)
    canvas.itemconfig(card_title, text=words_base.keys()[0])
    canvas.itemconfig(card_word, text=randWord["French"])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("FlashCard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=newWord)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=newWord)
check_button.grid(row=1, column=1)

newWord()

window.mainloop()
