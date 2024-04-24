import tkinter as tk
from tkinter import ttk, font

# window
window = tk.Tk()
window.title('Styling')
window.geometry('400x300')

# print(font.families())

# style
style = ttk.Style()
# print(style.theme_names())
# style.theme_use('classic')

style.configure('new.TButton', background='green', foreground='black', font=('Jokerman', 20))
style.map('new.TButton', foreground=[('pressed', 'red'),('disabled','yellow')],
          background=[('pressed', 'green'), ('active', 'blue')])

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
                    style='new.TButton')
button.pack()

# run
window.mainloop()