#!/usr/bin/env python3

# FILE:     Calculator.py
# NAME:     GUI Calculator using tkinter module
# AUTHOR:   Josue Torres
# PURPOSE:  Perform basic arithmetic operations

from tkinter import *
from tkinter.font import Font

# Create GUI
root = Tk()
root.title("Python Calculator")

# Display the Header
header = Label(root, text="Calculator", font="arial 15 bold")
header.grid(row=0, column=0, columnspan=4)

# Create the input box
entry = Entry(root, width=45, borderwidth=8, font="arial 10")
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Define Font
myFont = Font(
    family="Seoge",
    size=12,
    weight="bold",
    slant="roman",
    underline=0,
    overstrike=0
)

def button_ent(num):
    entry.insert(END, num)

def equal():
    # global fNumber
    sNumber = int(entry.get())
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, fNumber + sNumber)
    elif math == "subtraction":
        entry.insert(0, fNumber - sNumber)
    elif math == "multiplication":
        entry.insert(0, fNumber * sNumber)
    elif math == "division":
        entry.insert(0, fNumber / sNumber)

def clear():
    entry.delete(0, END)

def add():
    global fNumber, math
    math = "addition"
    fNumber = int(entry.get())
    entry.delete(0, END)

def subtract():
    global fNumber, math
    math = "subtraction"
    fNumber = int(entry.get())
    entry.delete(0, END)

def divide():
    global fNumber, math
    math = "division"
    fNumber = int(entry.get())
    entry.delete(0, END)

def multiply():
    global fNumber, math
    math = "multiplication"
    fNumber = int(entry.get())
    entry.delete(0, END)

# Define the buttons
button7 = Button(root, text="7", font = myFont, padx=40, pady=20, command=lambda: button_ent(7))
button8 = Button(root, text="8", font = myFont, padx=40, pady=20, command=lambda: button_ent(8))
button9 = Button(root, text="9", font = myFont, padx=40, pady=20, command=lambda: button_ent(9))
button4 = Button(root, text="4", font = myFont, padx=40, pady=20, command=lambda: button_ent(4))
button5 = Button(root, text="5", font = myFont, padx=40, pady=20, command=lambda: button_ent(5))
button6 = Button(root, text="6", font = myFont, padx=40, pady=20, command=lambda: button_ent(6))
button1 = Button(root, text="1", font = myFont, padx=40, pady=20, command=lambda: button_ent(1))
button2 = Button(root, text="2", font = myFont, padx=40, pady=20, command=lambda: button_ent(2))
button3 = Button(root, text="3", font = myFont, padx=40, pady=20, command=lambda: button_ent(3))
button0 = Button(root, text="0", font = myFont, padx=40, pady=20, command=lambda: button_ent(0))

buttonClear    = Button(root, text="AC", font = myFont, padx=33, pady=20, command=clear)
buttonEqual    = Button(root, text="=", font = myFont, padx=85, pady=20, command=equal)
buttonAdd      = Button(root, text="+", font = myFont, padx=37, pady=20, command=add)
buttonSubtract = Button(root, text="-", font = myFont, padx=39, pady=20, command=subtract)
buttonMultiply = Button(root, text="*", font = myFont, padx=39, pady=20, command=multiply)
buttonDivide   = Button(root, text="÷", font = myFont, padx=38, pady=20, command=divide)
buttonPlusMinus= Button(root, text="±", font = myFont, padx=39, pady=20, command=divide)

# Put buttons on the screen
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
buttonDivide.grid(row=2, column=3)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
buttonMultiply.grid(row=3, column=3)

button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
buttonSubtract.grid(row=4, column=3)

buttonPlusMinus.grid(row=5, column=0)
button0.grid(row=5, column=1)
buttonClear.grid(row=5, column=2)
buttonAdd.grid(row=5, column=3)

buttonEqual.grid(row=6, column=1, columnspan=2)

if __name__ == "__main__":
    root.mainloop()
