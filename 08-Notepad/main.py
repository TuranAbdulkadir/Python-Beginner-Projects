import tkinter as tk
from tkinter import filedialog
def save():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f: f.write(t.get("1.0", tk.END)); f.close()
root = tk.Tk()
tk.Button(root, text="Save File", command=save).pack()
t = tk.Text(root); t.pack()
root.mainloop()