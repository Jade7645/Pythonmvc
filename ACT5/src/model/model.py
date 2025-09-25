def padovan(n: int) -> int:
    if n == 0 or n == 1 or n == 2:
        return 1
    return padovan(n - 2) + padovan(n - 3)
