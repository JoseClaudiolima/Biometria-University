import tkinter as tk
import ttkbootstrap as ttk

class interface():

    def __init__(self, dimensions, titleName):
        self.window = ttk.Window()
        self.window.title(titleName)
        self.setWindowSize(dimensions)


    def setWindowSize(self, dimensions):
        x = y = 0
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 400) // 2

        self.window.geometry(f'{dimensions}+{x}+{y}')


    def Start(self):
        box = tk.Frame(self.window)
        login_btn = ttk.Button(box, text='Login', command=lambda:print('Login'), width=20)
        register_btn = ttk.Button(box, text='Register', command=lambda:print('Register'), width=20)

        box.pack()
        login_btn.pack(pady=(25,15))
        register_btn.pack()

        self.window.protocol("WM_DELETE_WINDOW", lambda: self.window.quit())
        self.window.mainloop()


