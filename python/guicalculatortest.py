#A full calculator

import tkinter as tk
import tkinter.font as font
import math
import simpleaudio as sa

filename = 'baby.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()

display="0"

def update_display(key):
    global display
    wave_obj.play()
    if display=="0":
        display=""

    if key=='AC':
        display="0"
    elif key=='=':
        try:
            display=str(eval(display))
        except:
            display = "Error"
        #display="0"
    else:
        display=display+key

    answer.configure(text=display)

    if key=='=':
        display="0"




master = tk.Tk(className="Dad's Cool Baby Calculator")

answer=tk.Label(master, text=display, bg="grey", anchor='e',padx=4,pady=4)
answer.grid(row=0,column=0, sticky=tk.E+tk.W, padx=4, columnspan=4,pady=4)

button_font=font.Font(size=25)

tk.Button(master, text='AC', font=button_font, command=lambda: update_display('AC')).grid(row=1, column=0, sticky=tk.W)
#tk.Button(master, text='=', font=button_font, command=lambda: update_display('=')).grid(row=1, column=1,padx=4,pady=4)
tk.Button(master, text='Off',font=button_font, command=master.quit,fg='red').grid(row=1, column=3, sticky=tk.E)

tk.Button(master, text='1',font=button_font, command=lambda: update_display('1')).grid(row=2, column=0,padx=4,pady=4)
tk.Button(master, text='2',font=button_font, command=lambda: update_display('2')).grid(row=2, column=1,padx=4,pady=4)
tk.Button(master, text='3',font=button_font, command=lambda: update_display('3')).grid(row=2, column=2,padx=4,pady=4)
tk.Button(master, text='+',font=button_font, command=lambda: update_display('+')).grid(row=2, column=3,padx=4,pady=4)


tk.Button(master, text='4',font=button_font, command=lambda: update_display('4')).grid(row=3, column=0,padx=4,pady=4)
tk.Button(master, text='5',font=button_font, command=lambda: update_display('5')).grid(row=3, column=1,padx=4,pady=4)
tk.Button(master, text='6',font=button_font, command=lambda: update_display('6')).grid(row=3, column=2,padx=4,pady=4)
tk.Button(master, text='-',font=button_font, command=lambda: update_display('-')).grid(row=3, column=3,padx=4,pady=4)

tk.Button(master, text='7',font=button_font, command=lambda: update_display('7')).grid(row=4, column=0,padx=4,pady=4)
tk.Button(master, text='8',font=button_font, command=lambda: update_display('8')).grid(row=4, column=1,padx=4,pady=4)
tk.Button(master, text='9',font=button_font, command=lambda: update_display('9')).grid(row=4, column=2,padx=4,pady=4)
tk.Button(master, text='x',font=button_font, command=lambda: update_display('*')).grid(row=4, column=3,padx=4,pady=4)


tk.Button(master, text='0',font=button_font, command=lambda: update_display('0')).grid(row=5, column=0,padx=4,pady=4)
tk.Button(master, text='.',font=button_font, command=lambda: update_display('.')).grid(row=5, column=1,padx=4,pady=4)
tk.Button(master, text='=',font=button_font, command=lambda: update_display('=')).grid(row=5, column=2,padx=4,pady=4)
tk.Button(master, text='/',font=button_font, command=lambda: update_display('/')).grid(row=5, column=3,padx=4,pady=4)

tk.mainloop()