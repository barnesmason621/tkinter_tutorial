# so far, the master has always been the window
# This isn't always ideal
# a menu should have a menu as the master
# a tab entry should have a tab widget as the master
# For complex layouts, you can also create a container widget to organize the window

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Frames and parenting')

# frame
frame = ttk.Frame(window, width=200, height=200, borderwidth=10, relief=tk.GROOVE)
# frame.pack_propagate(False)
frame.pack(side='left')

# master setting
label = ttk.Label(frame, text='Label in frame')
label.pack()

button = ttk.Button(frame, text='Button in a frame')
button.pack()

# example
label2 = ttk.Label(window, text='Label outside frame')
label2.pack(side='left')


# run
window.mainloop()

