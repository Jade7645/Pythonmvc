from model.model import padovan
from view.view import View

class Controller:
    def __init__(self):
        self.view = View()

    def run(self):
        n = self.view.get_input()
        if n is not None and n >= 0:
            result = padovan(n)
            self.view.show_result(n, result)
        else:
            print("El valor debe ser un número entero mayor o igual a 0.")
