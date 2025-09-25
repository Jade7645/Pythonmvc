class DigitPalindromicModel:
    def is_digit_palindromic(self, num: int) -> int:
        """
        Verifica si un número es palíndromo (digit-palindromic).
        Retorna 1 si lo es, 0 si no.
        """
        num_str = str(num)
        if num_str == num_str[::-1]:
            return 1
        return 0
