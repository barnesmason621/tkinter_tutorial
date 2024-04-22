# we can change a lot of things

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400+250+200')
window.title('More on the window')
# window.iconbitmap('python.ico')

# window sizes
window.minsize(200, 100)
# window.maxsize(800, 700)
window.resizable(True, True)

# screen attributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# window attributes
window.attributes('-alpha', 0.9)  # sets transparency 0 - 1
# window.attributes('-topmost', True)  # puts the window on top

# security event
window.bind('<Escape>', lambda event: window.quit())  # close window with escape key

# window.attributes('-disable', True)
# window.attributes('-fullscreen', True)

# title bar
window.overrideredirect(True)  # hides title bar
grip = ttk.Sizegrip(window)
grip.place(relx=1.0, rely=1.0, anchor='se')  # puts grip handle in bottom right corner

# run
window.mainloop()

