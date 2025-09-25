class GranjaModel:
    def __init__(self, cabezas, patas):
        self.cabezas = cabezas
        self.patas = patas

    def resolver(self, patos=0, conejos=0):
        # Caso base: si el número de cabezas y patas coincide, retorna la solución
        if patos + conejos == self.cabezas and patos * 2 + conejos * 4 == self.patas:
            return patos, conejos
        # Si el número de patos supera el de cabezas, no hay solución
        if patos > self.cabezas:
            return None
        # Llamada recursiva: prueba con un pato más y un conejo menos
        return self.resolver(patos + 1, conejos)