def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            raise ZeroDivisionError
        else:
            result = numerator / denominator
            return f"The result of the division is {result:.1f}"
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."
    except ValueError:
            return f"Error: Please enter numeric values only."

