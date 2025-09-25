from model.pal_model import DigitPalindromicModel
from view.pal_view import DigitPalindromicView

class DigitPalindromicController:
    def __init__(self, model: DigitPalindromicModel, view: DigitPalindromicView):
        self.model = model
        self.view = view

    def run(self):
        """
        Flujo principal: pide número, verifica y muestra resultado.
        """
        num = self.view.get_number()
        result = self.model.is_digit_palindromic(num)
        self.view.show_result(num, result)
