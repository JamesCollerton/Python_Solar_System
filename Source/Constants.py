# ------------------------------------------------------------------------------

# Constants Class.

# This holds all of the constants for the program and makes them accessible
# using CONST.CONSTANT NAME.

# ------------------------------------------------------------------------------

def constant(f):

    def fset(self, value):
        raise TypeError

    def fget(self):
        return f()

    return property(fget, fset)

class _Const(object):

    @constant
    def CANVAS_WIDTH():
        return 800

    @constant
    def CANVAS_HEIGHT():
        return 500

CONST = _Const()