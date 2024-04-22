# to use tkinter (or any GUI framework) efficiently, you need to be able to create your own components

import tkinter as tk
from tkinter import ttk


def create_segment(parent, label_text, button_text):
    frame = ttk.Frame(parent)

    # grid layout
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure((0, 1, 2), weight=1, uniform='a')

    # widgets
    ttk.Label(frame, text=label_text).grid(row=0, column=0, sticky='nsew')
    ttk.Button(frame, text=button_text).grid(row=0, column=1, sticky='nsew')

    return frame


class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text, button2_text):
        super().__init__(master=parent)

        # grid layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1, uniform='a')
        ttk.Label(self, text=label_text).grid(row=0, column=0, sticky='nsew')
        ttk.Button(self, text=button_text).grid(row=0, column=1, sticky='nsew')
        frame = ttk.Frame(self)
        ttk.Entry(frame).pack(side='top', expand=True, fill='both')
        ttk.Button(frame, text=button2_text).pack(side='top', expand=True, fill='both')
        frame.grid(row=0, column=2, sticky='nsew')

        self.pack(expand=True, fill='both', padx=10, pady=10)


# window
window = tk.Tk()
window.title('Widgets and return')
window.geometry('400x600')

# widgets
Segment(window, 'label', 'button', 'Exercise')
Segment(window, 'test', 'click', 'Exercise')
Segment(window, 'hello', 'test', 'Loser')
Segment(window, 'bye', 'launch', 'Exercise')
Segment(window, 'last one', 'exit', 'Exercise')

# create_segment(window, 'label', 'button').pack(expand=True, fill='both', padx=10, pady=10)
# create_segment(window, 'test', 'click').pack(expand=True, fill='both', padx=10, pady=10)
# create_segment(window, 'hello', 'TEST').pack(expand=True, fill='both', padx=10, pady=10)
# create_segment(window, 'bye', 'launch').pack(expand=True, fill='both', padx=10, pady=10)
# create_segment(window, 'last one', 'exit').pack(expand=True, fill='both', padx=10, pady=10)



# run
window.mainloop()

