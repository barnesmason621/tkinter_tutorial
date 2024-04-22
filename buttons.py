# multiple kinds of buttons

import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')


# button
def button_func():
    print('A basic button')
    print(radio_var.get())


string_var = tk.StringVar(value='A button with string var')
button = ttk.Button(master=window, text='A simple button', command=button_func, textvariable=string_var)
button.pack()

# check boxes
check_var = tk.IntVar()
check = ttk.Checkbutton(window,
                        text='chekbox1',
                        command=lambda: print(check_var.get()),
                        variable=check_var,
                        onvalue=10,
                        offvalue=5)
check.pack()

check2 = ttk.Checkbutton(
    window,
    text='checkbox 2',
    command= lambda: print('test'))
check2.pack()

# radio buttons, Have to have different values, or they work together
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window,
    text='RadioButton1',
    value='radio1',
    variable=radio_var,
    command= lambda: print(radio_var))
radio2 = ttk.Radiobutton(
    window,
    text='RadioButton2',
    value='radio2',
    variable=radio_var)
radio1.pack()
radio2.pack()

# run
window.mainloop()






