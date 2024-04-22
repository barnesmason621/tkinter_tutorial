# Two ways to get data
#   variables
#   get()


import tkinter as tk
from tkinter import ttk


def button_func():
    # get content of the entry
    entry_text = entry.get()

    # update the label
    # label.configure(text='some other text')
    label['text'] = entry_text       # both lines do same thing
    entry.configure(state='disabled')
    # print(label.configure())    --- prints all parameters for configure


# window
window = tk.Tk()
window.title('Getting and setting widgets')

# widgets
label = ttk.Label(master=window, text='Some text')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='The button', command=button_func)
button.pack()

# run
window.mainloop()


# Widgets can be updated with configure method
