from views import view
from controllers import controller as contr

if __name__ == "__main__":
    window = view.Interface('300x127', 'Inicio')

    controller = contr.Controller(window)
    controller.show_auth()
