# you don't really have to hide/show
# instead you add and remove widgets

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Hide widgets')


# place
def toggle_label_place():
    global label_visibility
    if label_visibility:
        label.place_forget()
        label_visibility = False
    else:
        label_visibility = True
        label.place(relx=0.5, rely=0.5, anchor='center')


button = ttk.Button(window, text='toggle Label', command=toggle_label_place)
button.place(x=10, y=10)

label_visibility = True
label = ttk.Label(window, text='A label')
label.place(relx=0.5, rely=0.5, anchor='center')

# run
window.mainloop()


