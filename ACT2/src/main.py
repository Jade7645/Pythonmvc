from model.digit_model import DigitIncreasingModel
from view.digit_view import DigitIncreasingView
from controller.digit_controller import DigitIncreasingController

if __name__ == "__main__":
    model = DigitIncreasingModel()
    view = DigitIncreasingView()
    controller = DigitIncreasingController(model, view)

    controller.run()
