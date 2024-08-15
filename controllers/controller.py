# Handle interactions between view and controller

class Controller:
    def __init__(self, view):
        self.view = view


    def show_auth(self):
        self.view.create_auth_screen(self.login, self.register)


    def login(self):
        self.view.destroy_widgets()

        print('login')


    def register(self):
        self.view.destroy_widgets()

        print('register')

