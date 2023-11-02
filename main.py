import tkinter
from tkinter import *


BORDER = "#3C2C3E"
BG = "#4B5D67"
FG = "khaki"
BUTTON_FG = "black"

FONT_FAMILY1 = "KaiTi"
FONT_FAMILY2 = "Calibri"
FONT_FAMILY3 = "Helvetica"

FONT_SIZE1 = 14
FONT_SIZE2 = 18
FONT_SIZE3 = 40

FONT_STYLE1 = "normal"
FONT_STYLE2 = "italic"
FONT_STYLE3 = "bold"

HEADER_FONT = (FONT_FAMILY3, FONT_SIZE3, FONT_STYLE1)
INSTRUCTION_FONT = (FONT_FAMILY1, FONT_SIZE1, FONT_STYLE2)
TYPE_FONT = (FONT_FAMILY2, FONT_SIZE2, FONT_STYLE1)


def delete_text():
    text_writing_widget.delete("1.0", "end")


def reset_timer(event):
    global timer, timer_running
    if timer_running:
        window.after_cancel(timer)
    timer = window.after(5000, delete_text)
    timer_running = True


def save_work():
    text_to_save = text_writing_widget.get("1.0", "end")
    if text_to_save == "":
        return
    try:
        file = open("saved_text.txt", "r")
    except FileNotFoundError:
        file = open("saved_text.txt", "w")
        file.write(text_to_save)
    else:
        if file.read() == "":
            text_to_write = text_to_save
        else:
            text_to_write = f"\n{text_to_save}"
        with open("saved_text.txt", "a") as file:
            file.write(text_to_write)


def load_work():
    try:
        file = open("saved_text.txt", "r")
    except FileNotFoundError:
        return
    else:
        text_writing_widget.delete("1.0", "end")
        text_writing_widget.insert(tkinter.END, file.readlines()[-1])
        

window = Tk()
window.title("Disappearing Text Writing App")
window.config(padx=100, pady=10, background=BG)

header_label = Label(text="Write Anything",
                     foreground=FG,
                     font=HEADER_FONT,
                     background=BG,
                     pady=10)
header_label.grid(column=0, row=0, columnspan=3)

instruction_label = Label(text="Take longer than 5 seconds to type and your work will be undone.",
                          foreground=FG,
                          background=BG,
                          font=INSTRUCTION_FONT,
                          pady=10)
instruction_label.grid(column=0, row=1, columnspan=3)

text_writing_widget = Text(window,
                           height=5,
                           width=100,
                           font=TYPE_FONT,
                           padx=5,
                           wrap=WORD,
                           background=BG)
text_writing_widget.config(foreground=FG,
                           insertbackground=BORDER,
                           highlightthickness=2,
                           highlightcolor=BORDER)
text_writing_widget.grid(column=0, row=2, columnspan=3)
text_writing_widget.focus_set()

save_btn = Button(text="Save", width=59, fg=BUTTON_FG, bg=BG,
                  highlightthickness=0,
                  highlightbackground=BG,
                  highlightcolor=BG,
                  border=3,
                  command=save_work)
save_btn.grid(column=0, row=3, columnspan=2)

load_save_btn = Button(text="Load Save", width=58, foreground=BUTTON_FG, background=BG,
                       highlightcolor=BG,
                       highlightbackground=BG,
                       highlightthickness=0,
                       border=3,
                       command=load_work)
load_save_btn.grid(column=2, row=3)

timer = None
timer_running = False

text_writing_widget.bind("<KeyRelease>", reset_timer)

window.mainloop()
