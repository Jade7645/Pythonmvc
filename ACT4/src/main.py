from model.padovan_model import PadovanModel
from view.padovan_view import PadovanView
from controller.padovan_controller import PadovanController

if __name__ == "__main__":
    model = PadovanModel()
    view = PadovanView()
    controller = PadovanController(model, view)

    controller.run()
