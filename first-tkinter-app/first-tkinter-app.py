import tkinter as tk
from tkinter import ttk


def greet():
    print('Hello World!')


root = tk.Tk()

ttk.Label(root, text="Hello World!", padding=(30, 10)).pack()
greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack()

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack()

root.mainloop()
