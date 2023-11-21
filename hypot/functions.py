def addition(a,b):
    o = a+b
    if isinstance(a, int) != True and isinstance(a, float) != True:
        return "PLEASE USE INTEGERS OR FLOATS" 
    elif isinstance(b, int) != True and isinstance(b, float) != True:
        return "PLEASE USE INTEGERS OR FLOATS"   
    else:
        return o
def squared(a):
    o = a*a
    return o
def sqroot(a):
    return a**(-1)
def hypot(a,b):
    o = sqroot(addition(squared(a),squared(b)))
    return o