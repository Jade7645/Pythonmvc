class PadovanView:
    def get_number(self) -> int:
        """
        Pide al usuario un número entero para calcular el término.
        """
        while True:
            try:
                return int(input("Ingrese la posición n de la serie de Padovan: "))
            except ValueError:
                print("Entrada inválida. Ingrese un número entero.")

    def show_result(self, n: int, value: int):
        """
        Muestra el resultado del cálculo.
        """
        print(f"El término P({n}) de la serie de Padovan es: {value}")
