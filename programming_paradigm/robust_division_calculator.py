def safe_divide(numerator: float, denominator: float):
    try:
        if denominator == 0:
            raise ZeroDivisionError
        else:
            result = numerator / denominator
            print(f"The result of the division is {result: .1f}")
    except ValueError:
        if not isinstance(numerator, (int, float)) and isinstance(denominator, (int, float)):
            return f"Error: Please enter numeric values only."

