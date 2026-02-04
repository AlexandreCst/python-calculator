"""This module contain all of the operations available to realize some operation
on different numbers like addition, subtraction, multiplication and division"""

def operation(a: float, b: float, operator) -> float:
    """
    Docstring for operation

    This function does basic operations like addition, subtraction, multiplicat-
    ion and division
    
    :param a: First number
    :type a: float
    :param b: Second number
    :type b: float
    :param operator: Operation had to be done
    :return: Result of the operation
    :rtype: float
    """
    #Addition
    if operator == '+':
        return a + b
    
    #Subtraction
    elif operator == '-':
        return a - b
    
    #Multiplication
    elif operator == "*":
        return a * b
    
    #Division
    else:
        return a / b