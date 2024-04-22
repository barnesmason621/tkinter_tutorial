# 3 widgets can be scrolled: Canvas, text, and treeview

import tkinter as tk
from tkinter import ttk
from random import randint, choice

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Scrolling')

# # canvas
# canvas = tk.Canvas(window, bg='white', scrollregion=(0, 0, 2000, 5000))
# canvas.create_line(0, 0, 2000, 5000, fill='green', width=10)
# for i in range(100):
#     l = randint(0, 2000)
#     t = randint(0, 5000)
#     r = l + randint(0, 2000)
#     b = t + randint(0, 2000)
#     color = choice(('red', 'green', 'blue', 'yellow', 'orange'))
#     canvas.create_rectangle(l, t, r, b, fill=color)
# canvas.pack(expand=True, fill='both')
#
# # mouse wheel scrolling
# canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta / 60), 'units'))
# canvas.bind('<Control MouseWheel>', lambda event: canvas.xview_scroll(-int(event.delta / 60), 'units'))
#
# # scrollbar
# scrollbar = ttk.Scrollbar(window, orient='vertical', command=canvas.yview)
# canvas.configure(yscrollcommand=scrollbar.set)
# scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
#
# # horizontal scrollbar
# h_scrollbar = ttk.Scrollbar(window, orient='horizontal', command=canvas.xview)
# canvas.configure(xscrollcommand=h_scrollbar.set)
# h_scrollbar.place(relx=0, rely=1, relwidth=1, anchor='sw')

# # text
# text = tk.Text(window)
# for i in range(1, 200):
#     text.insert(f'{i}.0', f'text: {i}')
# text.pack(expand=True, fill='both')
#
# scrollbar_text = ttk.Scrollbar(window, orient='vertical', command=canvas.yview)
# text.configure(yscrollcommand=scrollbar_text.set)
# scrollbar_text.place(relx=1, rely=0, relheight=1, anchor='ne')

# Treeview
table = ttk.Treeview(window, columns=(1, 2), show='headings')
table.heading(1, text='First Name')
table.heading(2, text='Last Name')
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']
for i in range(100):
    table.insert(parent='', index=tk.END, values=(choice(first_names), choice(last_names)))
table.pack(expand=True, fill='both')

scrollbar_table = ttk.Scrollbar(window, orient='vertical', command=canvas.yview)
table.configure(yscrollcommand=scrollbar_table.set)
scrollbar_table.place(relx=1, rely=0, relheight=1, anchor='ne')

# run
window.mainloop()