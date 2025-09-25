class DigitPalindromicView:
    def get_number(self) -> int:
        """
        Pide al usuario un número entero por consola.
        """
        while True:
            try:
                return int(input("Ingrese un número para verificar si es palíndromo: "))
            except ValueError:
                print("Entrada inválida. Ingrese un número entero.")

    def show_result(self, num: int, result: int):
        """
        Muestra si el número es palíndromo o no.
        """
        if result == 1:
            print(f"{num} es un número digit-palindromic")
        else:
            print(f"{num} no es un número digit-palindromic")
