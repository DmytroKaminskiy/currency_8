from decimal import Decimal


def to_decimal(value: str, precision: int = 4) -> Decimal:
    """
    TODO
    """
    return round(Decimal(value), precision)
