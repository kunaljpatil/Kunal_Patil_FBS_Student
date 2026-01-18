from tkinter import *
from tkinter import messagebox

def apply_theme():
    text = entry.get()
    choice = theme.get()
    
    if choice == 1:
        window.config(bg = 'skyblue')
        Label.config(text = text, fg = 'grey')
        
    elif choice == 2:
        window.config(bg = 'maroon')
        Label.config(text= text , fg = 'white')
        
    elif choice == 3:
        window.config(bg = 'grey')
        Label.config(text = text, fg = 'white')
        
window = Tk()
window.geometry('500x400')

entry = Entry(window)
label = Label(window, text='CHANGE YOUR WINDOW THEME', font=('times new roman', 19))
label.pack(pady=10)

theme = IntVar()

Radiobutton(window, text= 'SkyBlue & Grey Theme', variable = theme, value = 1).pack(pady=15, padx=15)
Radiobutton(window, text= 'Maroon & Grey Theme', variable=theme, value= 2).pack(pady=15, padx=15)
Radiobutton(window, text= 'Grey & White Theme', variable=theme, value= 3).pack(pady=15, padx=15)

Button(window, text = 'APPLY THEME', command=apply_theme).pack(pady=15, padx=15)



window.title('THEME CHANGER')
window.mainloop()