# both need to get to a list of values
# both can be connected to tk vars

import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Combo and Spin')

# combobox
items = ('Ice cream', 'Pizza', 'Broccoli')
food_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, textvariable=food_string)
combo.config(values=items)
combo.pack()

# events for combobox
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.configure(f'Selected value: {food_string.get()}'))  # prints food_string.get() on every selection
combo_label = ttk.Label(window, text='a label')
combo_label.pack()

# spinbox
spin_int = tk.IntVar(value=12)
spin = ttk.Spinbox(
    window,
    from_=3,
    to=20,
    increment=3,
    command=lambda event: print(spin_int.get()),
    textvariable=spin_int)
spin.bind('<<Increment>>', lambda event: print('Up'))
spin.pack()

# run
window.mainloop()