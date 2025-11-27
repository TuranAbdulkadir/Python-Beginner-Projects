import tkinter as tk
from time import strftime
root = tk.Tk()
lbl = tk.Label(root, font=('arial', 40, 'bold'), bg='black', fg='cyan')
lbl.pack(anchor='center')
def time():
    lbl.config(text=strftime('%H:%M:%S'))
    lbl.after(1000, time)
time()
root.mainloop()