class DigitIncreasingModel:
    def is_digit_increasing(self, num: int) -> int:
        """
        Verifica si un número es 'digit-increasing'.
        Retorna 1 si cumple, 0 si no.
        """
        for d in range(1, 10):
            total = 0
            term = ""
            while total < num:
                term += str(d)            # concatenar dígito
                total += int(term)        # convertir y sumar
                if total == num:
                    return 1
        return 0
