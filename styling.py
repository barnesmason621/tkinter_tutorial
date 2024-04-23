import tkinter as tk
from tkinter import ttk, font

# window
window = tk.Tk()
window.title('Styling')
window.geometry('400x300')

# widgets
label = ttk.Label(window,
                  text='A label\nAnd then type on another line',
                  background='red',
                  foreground='white',
                  font=('Jokerman', 18),
                  justify='center')
label.pack()

button = ttk.Button(window,
                    text='A button',
                    bg='yellow')
button.pack()

# run
window.mainloop()