class PadovanModel:
    def padovan(self, n: int) -> int:
        """
        Calcula el término n-ésimo de la serie de Padovan recursivamente.
        P(0) = 1, P(1) = 1, P(2) = 1
        P(n) = P(n-2) + P(n-3) para n > 2
        """
        if n == 0 or n == 1 or n == 2:
            return 1
        return self.padovan(n - 2) + self.padovan(n - 3)
