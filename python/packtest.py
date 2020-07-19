import tkinter as tk

#root is the top level widget Tk
root = tk.Tk()

#Three objects, no pack options, pack choose to lay vertically with different 
# length, aligned to the center
w = tk.Label(root, text="Red Sun", bg="red", fg="white")
w.pack(padx = 5, pady = 10, side = tk.LEFT)
w = tk.Label(root, text="Dead Grass", bg="orange", fg="black")
w.pack(padx = 5, pady = 10, side = tk.LEFT)
w = tk.Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(padx = 5, pady = 10, side = tk.LEFT)

w = tk.Label(root, text="Red Sun", bg="red", fg="white")
w.pack(padx = 5, pady = 10)
w = tk.Label(root, text="Dead Grass", bg="orange", fg="black")
w.pack(padx = 5, pady = 10, side = tk.LEFT)
w = tk.Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(padx = 5, pady = 10, side = tk.LEFT)

tk.mainloop()

