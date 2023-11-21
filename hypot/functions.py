def addition(a,b):
    """This function returns a plus b

    :param a: the first number
    :type a: int or float
    :param b: the second number
    :type b: int or float
    :return: The sum of the inputs
    :rtype: int or float
    """    
    o = a+b
    if isinstance(a, int) != True and isinstance(a, float) != True:
        return "PLEASE USE INTEGERS OR FLOATS" 
    elif isinstance(b, int) != True and isinstance(b, float) != True:
        return "PLEASE USE INTEGERS OR FLOATS"   
    else:
        return o
def squared(a):
    """Calculate the square of a number

    :param a: The number to be squared
    :type a: int or float
    :return: The square of input
    :rtype: int or float
    """    
    o = a*a
    return o
def sqroot(a):
    """Calculate the square root of a number

    :param a: The number to be rooted
    :type a: int or float
    :return: The squareroot of input
    :rtype: int or float
    """  
    return a**(0.5)
def hypot(a,b):
    """Calculate the hypotenuse

    :param a: First input
    :type a: int or float
    :param b: Second input
    :type b: int or float
    :return: The length of the hypotenuse of a right angled triangle, when the other side lengths are input a and b
    :rtype: int or float
    """    
    o = sqroot(addition(squared(a),squared(b)))
    return o