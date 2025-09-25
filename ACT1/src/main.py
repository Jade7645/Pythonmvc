from controller.controller import GranjaController

if __name__ == "__main__":
    cabezas = 35
    patas = 94
    controller = GranjaController(cabezas, patas)
    controller.resolver_problema()