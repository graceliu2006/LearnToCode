try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainwindow = tkinter.Tk()

mainwindow.title("Hello World")
mainwindow.geometry('640x480+8+400')
mainwindow.mainloop()
