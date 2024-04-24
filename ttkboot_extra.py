import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter

# window
window = ttk.Window(themename='darkly')
window.title('extra widgets')

# scrollable frame
scroll_frame = ScrolledFrame(window)
scroll_frame.pack(expand=True, fill='both')

for i in range(100):
    ttk.Label(scroll_frame, text=f'Label: {i}').pack(fill='x')
    ttk.Button(scroll_frame, text=f'Button: {i}').pack(fill='x')

# toast
toast = ToastNotification(title='This is a message title',
                          message='This is the actual message',
                          bootstyle='warning',
                          duration=2000)  # 2 sec

ttk.Button(window, text='Show toast', command=toast.show_toast).pack()

# tooltip
button = ttk.Button(window, text='Tooltip Button', bootstyle='warning')
button.pack(pady=10)
ToolTip(button, text='This is a tooltip', bootstyle='light-inverse')

# calendar
calendar = DateEntry(window)
calendar.pack(pady=10)

ttk.Button(window, text='Get calendar date', command=lambda: print(calendar.entry.get())).pack()

# progress bar -> "flood gauge"
progress_int = tk.IntVar(value=50)
progress = ttk.Floodgauge(
    window,
    text='progress',
    variable=progress_int,
    bootstyle='danger',
    mask='progress: {}%')
progress.pack(pady=10, fill='x')
ttk.Scale(window, from_=0, to=100, variable=progress_int).pack()

# meter
meter = ttk.Meter(
    window,
    amounttotal=100,
    amountused=10,
    interactive=True,
    metertype='full',
    subtext='Some other text',
    bootstyle='danger'
)

meter.pack()

# run
window.mainloop()
