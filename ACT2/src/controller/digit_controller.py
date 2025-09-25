from model.digit_model import DigitIncreasingModel
from view.digit_view import DigitIncreasingView

class DigitIncreasingController:
    def __init__(self, model: DigitIncreasingModel, view: DigitIncreasingView):
        self.model = model
        self.view = view

    def run(self):
        """
        Flujo principal: pide número, verifica y muestra resultado.
        """
        num = self.view.get_number()
        result = self.model.is_digit_increasing(num)
        self.view.show_result(num, result)
