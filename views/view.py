# Code Visual, "Front-End"

import tkinter as tk
import ttkbootstrap as ttk

class Interface():

    def __init__(self, dimensions, titleName):
        self.window = ttk.Window()
        self.window.title(titleName)
        self.setWindowSize(dimensions)
        

    def create_auth_screen(self, login, register):
        box = tk.Frame(self.window)
        login_btn = ttk.Button(box, text='Login', command=login, width=20)
        register_btn = ttk.Button(box, text='Register', command=register, width=20)

        box.pack()
        login_btn.pack(pady=(25,15))
        register_btn.pack()

        self.window.protocol("WM_DELETE_WINDOW", lambda: self.window.quit())
        self.window.mainloop()


    def setWindowSize(self, dimensions):
        x = y = 0
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 400) // 2

        self.window.geometry(f'{dimensions}+{x}+{y}')

    def destroy_widgets(self):
        for widget in self.window.winfo_children():
            widget.destroy()