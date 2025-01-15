from tkinter import *
from tkinter import colorchooser

def click():
    window.config(bg = colorchooser.askcolor()[1] )

def numbers(value):
    current = enter.get()
    if current == "enter numbers":
        enter.delete(0, END)
        current = ""
    enter.insert(END, value)

def backspace():
        enter.delete(0, END)

def calculate():
    try:
        expression = enter.get()
        result = eval(expression)
        rslt.delete(0, END)
        rslt.insert(0, str(result))
    except Exception as e:
        rslt.delete(0, END)
        rslt.insert(0, "Error")


window = Tk()

window.geometry("500x500")
window.title("Basic Calculator")
window.config(background="beige")
icon = PhotoImage(file="calcicon.png")
window.iconphoto(True,icon)

cb = Button(text="change color", command=click)
cb.pack(pady=15)

label = Label(window,
              text= "Perform basic calculations.",
              font= ('Arial',20,"bold"),
              fg = "#4b1e1e",
              bd=10,
              padx=8, pady=8
              )
label.pack(pady=15)

enter = Entry(window,
              font=("Arial",14),
              fg="beige",
              bg="#4b1e1e")
enter.insert(0,"enter numbers")
enter.pack(pady=15)

window_f = Frame(window)
window_f.pack(pady=15)

buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
    ('C', 4, 0),
]

for (text, row, col) in buttons:
    if text == '=':
        Button(window_f, text=text, font=("Consolas", 20), width=3, command = calculate).grid(row=row, column=col)
    elif text == 'C':
        Button(window_f, text=text, font=("Consolas", 20), width=3, command= backspace).grid(row=row, column=col)
    else:
        Button(window_f, text=text, font=("Consolas", 20), width=3, command=lambda t=text: numbers(t)).grid(row=row, column=col)


rslt = Entry(window,
              font=("Arial",14),
              fg="beige",
              bg="#4b1e1e")
rslt.pack(pady=15)

window.mainloop()