from tkinter import *
from tkinter import messagebox 

def log():
    uid = user_entry.get()
    passw = pass_entry.get()
    
    if (uid == 'admin' and passw == '1234'):
        window.config(bg= "#ff9393")
        messagebox.showinfo('Successful', 'LOGIN SUCCESSFUL!!!!!!!!!!')
    else:
        messagebox.showerror('ERROR', '"INVALID CREDENTIALS"')


def main():
    user_txt = Label(window, text='USER NAME:')
    global user_entry
    user_entry = Entry(window)
    pass_txt = Label(window, text = 'PASSWORD:')
    global pass_entry
    pass_entry = Entry(window, show="*")
    btn = Button(window, text='LOGIN', command=log)
    
    user_txt.pack(pady=10, padx=10)
    user_entry.pack()
    pass_txt.pack(pady=10, padx=10)
    pass_entry.pack()
    btn.pack(pady=10, padx=10)
    

window = Tk()
main()

window.config(bg= "#e18585")

window.title('LOGIN PAGE')
window.geometry('600x400')

window.mainloop()