import tkinter
from tkinter import ttk


def greet():
    print(f'Hello {username.get() or "world"}!')


root = tkinter.Tk()

username = tkinter.StringVar()

ttk.Label(root, text="Hello World!", padding=(30, 10)).pack()

name_label = ttk.Label(root, text="用户名: ")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(root, width=15, textvariable=username)
name_entry.pack(side="left")
name_entry.focus()

greet_button = ttk.Button(root, text="你好", command=greet)
greet_button.pack(side="left")

quit_button = ttk.Button(root, text="退出", command=root.destroy)
quit_button.pack(side="right")

root.mainloop()
