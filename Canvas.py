# canvas is a widget that allows for drawing shapes
# much like paint

import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')

# canvas
canvas = tk.Canvas(window, bg = 'white')
canvas.pack()

canvas.create_rectangle(
    (50, 20, 100, 200),
    fill='red',
    width=10,
    dash=(1, 2),
    outline='green')

canvas.create_line(
    (0, 0, 100, 150),
    fill='blue')

canvas.create_oval((0, 0, 100, 100), fill='green')
canvas.create_polygon((0, 0, 100, 200, 300, 50), fill='gray')
canvas.create_arc((200, 0, 300, 150), fill='red', start=45)

canvas.create_window((50, 100), window=ttk.Label(window, text='this is a text in canvas'))

# run
window.mainloop()
