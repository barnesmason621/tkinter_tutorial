import tkinter as tk
from tkinter import ttk

# pack becomes a lot easier when used in conjunction with frames

# window
window = tk.Tk()
window.title('Pack parenting')
window.geometry('400x600')

# top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text='First label', background='red')
label2 = ttk.Label(top_frame, text='Label 2', background='blue')

# middle widget
label3 = ttk.Label(window, text='Another label', background='green')

# bottom frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text='Last of the labels', background='orange')
button = ttk.Button(bottom_frame, text='A button')
button2 = ttk.Button(bottom_frame, text='Another button')

# top layout
label1.pack(fill='both', expand=True)
label2.pack(fill='both', expand=True)
top_frame.pack(fill='both', expand=True)

# middle layout
label3.pack(expand=True)

# bottom layout
button.pack(side='left', expand=True, fill='both')
label4.pack(side='left', expand=True, fill='both')
button2.pack(side='left', expand=True, fill='both')
bottom_frame.pack(expand=True, fill='both', padx=20, pady=20)

br_frame = ttk.Frame(bottom_frame)
button3 = ttk.Button(br_frame, text='Button 3')
button4 = ttk.Button(br_frame, text='Button 4')
button5 = ttk.Button(br_frame, text='Button 5')
button3.pack(expand=True, fill='both')
button4.pack(expand=True, fill='both')
button5.pack(expand=True, fill='both')
br_frame.pack(side='left', expand=True, fill='both')

# run
window.mainloop()


