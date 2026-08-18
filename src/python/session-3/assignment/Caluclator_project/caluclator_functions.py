



def addition(x: float, y: float) -> float:
    """Compute the sum of two numerical values.

    Args:
        x (float): The first number (addend).
        y (float): The second number (addend).

    Returns:
        float: The arithmetic sum of x and y.

    Examples:
        >>> addition(5, 3.5)
        8.5
    """
    result: float = float(x + y)
    print(f"The addition of {x} and {y} equals {result}")
    return result


def subtraction(x: float, y: float) -> float:
    """Compute the difference between two numerical values.

    Args:
        x (float): The number to be subtracted from (minuend).
        y (float): The number to subtract (subtrahend).

    Returns:
        float: The result of subtracting y from x.

    Examples:
        >>> subtraction(10, 4)
        6.0
    """
    result=float(x - y)
    print(f"The subtraction of {x} and {y} equals {result}")
    return result


def multiplication(x: float, y: float) -> float:
    """Compute the product of two numerical values.

    Args:
        x (float): The first factor (multiplicand).
        y (float): The second factor (multiplier).

    Returns:
        float: The product of multiplying x by y.

    Examples:
        >>> multiplication(4, 2.5)
        10.0
    """
    result: float = float(x * y)
    print(f"The multiplication of {x} and {y} equals {result}")
    return result


def division(x: float, y: float) -> float:
    """Compute the quotient of dividing one number by another.

    Args:
        x (float): The dividend (numerator).
        y (float): The divisor (denominator). Must not be zero.

    Returns:
        Optional[float]: The quotient resulting from the division, or None
        if division by zero is attempted.

    Raises:
        ZeroDivisionError: Handled internally when y is 0.

    Examples:
        >>> division(10, 2)
        5.0
        >>> division(10, 0)
        None
    """
    if y == 0:
        print("Error: Cannot divide by zero! Please provide a non-zero divisor.")
        return None

    result: float = float(x / y)
    print(f"The division of {x} by {y} equals {result}")
    return result