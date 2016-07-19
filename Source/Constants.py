# ------------------------------------------------------------------------------

# Constants Class.

# This holds all of the constants for the program and makes them accessible
# using CONST.CONSTANT NAME.

# ------------------------------------------------------------------------------

""" 
Function: 
    constant

Description:
    This creates the properties of a constant value and makes it a read only
    variable.

Args:
    f: The variable to be set/ got.

Returns:
    The properties fget and fset that make the variable read only.
""" 
def constant(f):

    def fset(self, value):
        raise TypeError

    def fget(self):
        return f()

    return property(fget, fset)

""" 
Function: 
    _Const

Description:
    This class allows us to access read only constant values

Args:
    object: 

Returns:
    The read only value at CONST.CONSTANT_NAME
""" 
class _Const(object):

    @constant
    def CANVAS_WIDTH():
        return 800

    @constant
    def CANVAS_HEIGHT():
        return 500

CONST = _Const()