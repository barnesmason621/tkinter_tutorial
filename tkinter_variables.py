# Tkinter has built in variables that are designed to work with widgets
# They are automatically updated by a widget, and they update a widget
# Although they still store basic data like strings, integers, and bools

import tkinter as tk
from tkinter import ttk


def button_func():
    print(string_var.get())
    string_var.set('button pressed')

# window
window = tk.Tk()
window.title('Tkinter Variables')

# tkinter variable
string_var = tk.StringVar()
# tk.IntVar
# tk.DoubleVar
# tk.BooleanVar

# widgets
label = ttk.Label(master=window, text='label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

button = ttk.Button(master=window, text='Button', command=button_func)
button.pack()

# run
window.mainloop()


