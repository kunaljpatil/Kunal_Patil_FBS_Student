from tkinter import *

def add():
    result.set(float(num1.get()) + float(num2.get()))

def subtract():
    result.set(float(num1.get()) - float(num2.get()))

def multiply():
    result.set(float(num1.get()) * float(num2.get()))

def divide():
    try:
        result.set(float(num1.get()) / float(num2.get()))
    except ZeroDivisionError:
        result.set("Error")

window = Tk()
window.title("Basic Calculator")
window.geometry("300x300")

Label(window, text="Number 1").pack()
num1 = Entry(window)
num1.pack()

Label(window, text="Number 2").pack()
num2 = Entry(window)
num2.pack()

Button(window, text="+", command=add).pack(pady=5)
Button(window, text="-", command=subtract).pack(pady=5)
Button(window, text="*", command=multiply).pack(pady=5)
Button(window, text="/", command=divide).pack(pady=5)

result = StringVar()
Label(window, text="Result").pack()
Entry(window, textvariable=result).pack()

window.mainloop()
