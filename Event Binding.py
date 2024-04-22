# Events can be lots of things: Keyboard input, Widgets changing
#   widgets selected or unselected, or mouse click/motion/wheel

# These can be observed and used

# You need to bind events to widgets

# list of events
# pythontutorial.net/tkinter/tkinter-event-binding

import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x: {event.x} y: {event.y}')


# window
window = tk.Tk()
window.geometry('600x500')
window.title('Event Binding')

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text='A button')
button.pack()

# events
# .bind('<modifier-action-detail>', function)
button.bind('<Alt-KeyPress-a>', lambda event: print(event))  # only works after button press
window.bind('<Motion>', get_pos)  # gives mouse position within "window"

window.bind('<KeyPress>', lambda event: print(f'a button was pressed({event.char})'))

entry.bind('<FocusIn>', lambda event: print('entry field was selected'))  # prints when
#   clicking into entry field

# run
window.mainloop()

