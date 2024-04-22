# 3 major methods:
#   pack takes the window and lets you pack in a certain direction
#       by default, this is top to bottom
#       size can be altered
#       can stack widgets in different directions

#   grid creates a grid over the window
#       can be referenced for more precise control
#       widgets can overlap and can be different sizes

#   place
#       placed by pixel reference

# will rely heavily on parenting and frames

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Layout intro')
window.geometry('600x400')

# widgets
label1 = ttk.Label(window, text='Label 1', background='red')
label2 = ttk.Label(window, text='Label 2', background='blue')

# # pack
# label1.pack(side='left', expand=True, fill='y')
# label2.pack(side='right', expand=True, fill='both')

# grid
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=2)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)
#
# label1.grid(row=0, column=1, sticky='nsew')  # sticky uses compass directions
# label2.grid(row=1, column=1, columnspan=2, sticky='nsew')

# place
label1.place(x=100, y=200, width=200, height=100)  # increase y to go down
label2.place(relx=0.5, rely=0.5, relwidth=1, anchor='center')  # places based on a scale of 0-1

# run
window.mainloop()




