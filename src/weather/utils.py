def celsius2kelvin(x):
    """Function to convert Celsius to Kelvin"""

    if not isinstance(x, (int, float)):
        raise TypeError("The input must be numeric.")

    return x + 273