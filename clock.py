from datetime import datetime
import tkinter as tk


def update_clock() -> None:
    now = datetime.now()
    time_label.config(text=now.strftime("%H:%M:%S"))
    date_label.config(text=now.strftime("%A, %B %d, %Y"))
    root.after(1000, update_clock)


root = tk.Tk()
root.title("Python Clock")
root.configure(bg="#101820")
root.resizable(False, False)

time_label = tk.Label(
    root,
    font=("Consolas", 48, "bold"),
    fg="#65E572",
    bg="#101820",
    padx=32,
)
time_label.pack(pady=(28, 4))

date_label = tk.Label(
    root,
    font=("Segoe UI", 13),
    fg="#D6DEE5",
    bg="#101820",
)
date_label.pack(pady=(0, 24))

update_clock()
root.mainloop()