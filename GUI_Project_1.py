import tkinter as tk

def greet(): label.config(text=f"Hello, {entry.get()}!")

root = tk.Tk()
tk.Label(root, text="Enter your name:").pack()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Greet", command=greet).pack()
label = tk.Label(root)
label.pack()
root.mainloop()