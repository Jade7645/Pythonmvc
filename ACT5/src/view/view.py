class View:
    @staticmethod
    def show_result(n: int, result: int):
        print(f"El término {n} de la serie de Padovan es: {result}")

    @staticmethod
    def get_input() -> int:
        try:
            return int(input("Ingrese el valor de n: "))
        except ValueError:
            print("Debe ingresar un número entero.")
            return None
