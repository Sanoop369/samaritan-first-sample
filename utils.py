# utils.py

def format_currency(value: float) -> str:
    """
    Formats a raw float value into a readable currency string.
    """
    if value < 0:
        return "$0.00"
    return f"${value:,.2f}"