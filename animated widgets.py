import customtkinter as ctk
from random import choice

class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

        # general attributes
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = abs(start_pos - end_pos)

        # animation logic
        self.pos = start_pos
        self.in_start_pos = True

        # layout
        self.place(relx=self.start_pos, rely=0, relwidth=self.width, relheight=1)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0, relwidth=self.width, relheight=1)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos=False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx=self.pos, rely=0, relwidth=self.width, relheight=1)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos=True


def move_btn():
    global button_x
    button_x += 0.05
    button.place(relx=button_x, rely=0.5, relheight=button_x, anchor='center')

    # configure
    colors = ['red', 'yellow', 'pink', 'green']
    color = choice(colors)
    button.configure(fg_color=color)


def infinite_print():
    global button_x
    button_x += 0.5
    if button_x < 10:
        window.after(1000, infinite_print)
        print('infinite')


# window
window = ctk.CTk()
window.title('Animated widgets')
window.geometry('600x400')

# animated widget
animated_panel = SlidePanel(window, 0, -0.3)

# button
button_x = 0.5
button = ctk.CTkButton(window, text='toggle sidebar', command=animated_panel.animate)
button.place(relx=button_x, rely=0.5, relheight=button_x, anchor='center')

# run
window.mainloop()