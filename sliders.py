# sliders
# Tkinter has a slider and a progress bar, both show progress in one dimension
# The slider can be moved by the user or set independently
# The progress bar can only be set independently

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# window
window = tk.Tk()
window.title('Sliders')

# slider
scale_int = tk.IntVar(value=15)
scale = ttk.Scale(
    window,
    command=lambda value: print(value),
    from_=0,
    to=25,
    length=300,
    orient='vertical',
    variable=scale_int)
scale.pack()

# progress bar
progress = ttk.Progressbar(
    window,
    variable=scale_int,
    maximum=25,
    orient='horizontal',
    mode='determinate',
    length=400)
progress.pack()

# ScrolledText
scrolled_text = scrolledtext.ScrolledText(window, width=100, height=10)
scrolled_text.pack()

# run
window.mainloop()


