def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError
            return f"Error: Cannot divide by zero."
        else:
            result = numerator / denominator
            print(f"The result of the division is {result:.1f}")
    except ValueError:
        if not isinstance(numerator, int) && isinstance(denominator, int):
            return f"Error: Please enter numeric values only."

