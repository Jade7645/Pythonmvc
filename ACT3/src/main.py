from model.pal_model import DigitPalindromicModel
from view.pal_view import DigitPalindromicView
from controller.pal_controller import DigitPalindromicController

if __name__ == "__main__":
    model = DigitPalindromicModel()
    view = DigitPalindromicView()
    controller = DigitPalindromicController(model, view)

    # Inicia la aplicación
    controller.run()
