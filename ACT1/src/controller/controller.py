from src.model import GranjaModel
from src.view import GranjaView

class GranjaController:
    def __init__(self, cabezas, patas):
        self.model = GranjaModel(cabezas, patas)
        self.view = GranjaView()

    def resolver_problema(self):
        resultado = self.model.resolver(0, self.model.cabezas)
        if resultado:
            patos, conejos = resultado
            self.view.mostrar_resultado(patos, conejos)
        else:
            self.view.mostrar_error()