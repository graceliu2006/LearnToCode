import tkinter as tk
import math

# # The first geometry manager of Tk had been pack. The algorithmic behaviour of pack is not easy to understand and it can be difficult to change an existing design. Grid was introduced in 1996 as an alternative to pack. Though grid is easier to learn and to use and produces nicer layouts, lots of developers keep using pack. 

# # Grid is in many cases the best choice for general use. While pack is sometimes not sufficient for changing details in the layout, place gives you complete control of positioning each element, but this makes it a lot more complex than pack and grid. 

# # The Grid geometry manager places the widgets in a 2-dimensional table, which consists of a number of rows and columns. The position of a widget is defined by a row and a column number. Widgets with the same column number and different row numbers will be above or below each other. Correspondingly, widgets with the same row number but different column numbers will be on the same "line" and will be beside of each other, i.e. to the left or the right. 

# # Using the grid manager means that you create a widget, and use the grid method to tell the manager in which row and column to place them. The size of the grid doesn't have to be defined, because the manager automatically determines the best dimensions for the widgets used.

# #Create a 6-by-2 grid, and take input
# colours = ['red','green','orange','white','yellow','blue']
# r = 0
# for colorname in colours:
#     tk.Label(text=colorname, relief=tk.RIDGE, width=15).grid(row=r,column=0)
#     tk.Entry(bg=colorname, relief=tk.SUNKEN, width=10).grid(row=r,column=1)
#     r = r + 1

# tk.mainloop()




def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    if e1.get() and e2.get() != "":
        answer.configure(text=e2.get()+", "+e1.get(),fg = "Black")
    else: 
        answer.configure(text="Error: No Input",fg = "Red")
master = tk.Tk()
tk.Label(master, 
         text="First Name").grid(row=0)
tk.Label(master, 
         text="Last Name").grid(row=1)
tk.Label(master, 
         text="Your full name is:").grid(row=2)
answer=tk.Label(master, 
         text="")
# Don't put grid on the same line, otherwise got None type for answer
answer.grid(row=2,column=1,sticky=tk.W, padx=4)


def return_entry_fields(event):
    show_entry_fields()

# Don't put grid on the same line, otherwise got None type for answer
answer.grid(row=2,column=1,sticky=tk.W, padx=4)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.bind("<Return>", return_entry_fields)
e2.bind("<Return>", return_entry_fields)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

#sticky − What to do if the cell is larger than widget. By default, with sticky='', widget is centered in its cell. sticky may be the string concatenation of zero or more of N, E, S, W, NE, NW, SE, and SW, compass directions indicating the sides and corners of the cell to which widget sticks.
tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=1, sticky=tk.E, pady=4)
tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.mainloop()




# #A simple calculator
# def evaluate(event):
#     res.configure(text = "Result: " + str(eval(entry.get())))
    
# w = tk.Tk()
# tk.Label(w, text="Your Expression:").pack()
# entry = tk.Entry(w)
# entry.bind("<Return>", evaluate)
# entry.pack()
# res = tk.Label(w)
# res.pack()
# w.mainloop()