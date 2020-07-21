try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

TK_SILENCE_DEPRECATION = 1

mainwindow = tkinter.Tk()

mainwindow.title("Hello World")
mainwindow.geometry('640x480-8-200')

label = tkinter.Label(mainwindow, text = "Hello World")
label.grid(row = 0, column = 0)

leftFrame = tkinter.Frame(mainwindow,highlightcolor="green")
leftFrame.grid(row = 1, column = 1)

canvas = tkinter.Canvas(leftFrame, relief = "raised", borderwidth = 1)
canvas.grid(row = 1, column = 0)

rightframe = tkinter.Frame(mainwindow)
rightframe.grid(row = 1, column = 2, sticky = "n")

button1 = tkinter.Button(rightframe, text = "Button1")
button2 = tkinter.Button(rightframe, text = "Button2")
button3 = tkinter.Button(rightframe, text = "Button3")
button1.grid(row = 0, column = 0)
button2.grid(row = 1, column = 0)
button3.grid(row = 2, column = 0)

mainwindow.columnconfigure(0, weight = 1)
mainwindow.columnconfigure(1, weight = 1)
mainwindow.grid_columnconfigure(2, weight = 1)

leftFrame.config(relief = "sunken", borderwidth = 1)
rightframe.config(relief = "sunken", borderwidth = 1)
leftFrame.grid(sticky = "ns")
rightframe.grid(sticky = "new")

rightframe.columnconfigure(0, weight = 1)
button2.grid(sticky="ew")
mainwindow.mainloop()
