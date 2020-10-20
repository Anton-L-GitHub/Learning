import tkinter as tk
from tkinter import ttk

root = tk.Tk()

main = ttk.Frame(root)
main.pack(side='left', fill='both', expand=True)

tk.Label(main, text='Label Top', bg='red').pack(side='top', fill='both', expand=True)
tk.Label(main, text='Label Top', bg='red').pack(side='top', fill='both', expand=True)


tk.Label(root, text='Label left')

root.mainloop()
