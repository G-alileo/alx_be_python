def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            return "Error: Can't divide by zero"
        result = numerator / denominator
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
    
    except Exception as e:
        return f"Error: An unexpected error occurred: {str(e)}"