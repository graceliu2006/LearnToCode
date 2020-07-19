import tkinter

def parabola(x):
    y = x * x / 100
    return y

def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="green")
    canvas.create_line(0, y_origin, 0, -y_origin, fill="orange")

def plot(canvas, x, y):
    canvas.create_line(x, y, x+1, y+1, fill="red")

main = tkinter.Tk()
main.title("Parabolola")
main.geometry("640x480")


canvas = tkinter.Canvas(main, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)

for x in range(-100,100):
    y = parabola(x)
    plot(canvas, x, -y)

main.mainloop()
