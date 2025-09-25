class DigitIncreasingView:
    def get_number(self) -> int:
        """
        Pide al usuario un número por consola.
        """
        while True:
            try:
                return int(input("Ingrese un número para verificar: "))
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

    def show_result(self, num: int, result: int):
        """
        Muestra el resultado de la verificación.
        """
        if result == 1:
            print(f"{num} es un número digit-increasing ")
        else:
            print(f"{num} NO es un número digit-increasing ")
