import tkinter as tk

root = tk.Tk()
entry = tk.Entry(root)

tk.Label(root, text = "This is text").grid(row = 1)
tk.Entry(root).grid(row = 2)
tk.mainloop()