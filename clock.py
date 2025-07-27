import tkinter as tk
import time
from tkinter import PhotoImage


def check_window_state(event=None):
    if root.state() == 'zoomed':
        clock_label.config(font=('sf digital readout', 200, 'bold'))
        date_label.config(font=('sf digital readout', 100, 'bold'))
    else:
        clock_label.config(font=('sf digital readout', 80, 'bold'))
        date_label.config(font=('sf digital readout', 35, 'bold'))


def update_clock():
    current_time = time.strftime('%I:%M:%S %p')
    clock_label.config(text=current_time)

    root.after(1000, update_clock)


def update_date():
    current_date = time.strftime('%A, %B %d, %Y')
    date_label.config(text=current_date)

    root.after(86400000, update_date)


root = tk.Tk()
root.title('Digital Clock')
root.configure(bg='black')
root.geometry('500x300')
icon = PhotoImage(file='clock.png')
root.iconphoto(True, icon)

clock_label = tk.Label(root, font=('sf digital readout', 80, 'bold'), fg='#E6D5B8', bg='black',
                       width=12, anchor='center', justify='center', )
clock_label.pack(expand=True, fill='both')

date_label = tk.Label(root, font=('sf digital readout', 35, 'bold'), fg='#E6D5B8', bg='black',
                      anchor='center')
date_label.pack(expand=True, fill='both')

root.bind('<Configure>', check_window_state)

update_clock()
update_date()

root.mainloop()
