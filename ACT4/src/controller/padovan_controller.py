from model.padovan_model import PadovanModel
from view.padovan_view import PadovanView

class PadovanController:
    def __init__(self, model: PadovanModel, view: PadovanView):
        self.model = model
        self.view = view

    def run(self):
        """
        Flujo principal: pide n, calcula y muestra resultado.
        """
        n = self.view.get_number()
        value = self.model.padovan(n)
        self.view.show_result(n, value)
