import re
import exceptions

def dali(x):
    """
    For mapping the real numbers onto the surreals.

    This takes a real number and maps it to the surreals.
    """
    if x == 0:
        return Surreal(set(), set())
    elif x > 0:
        return dali(x-1)
    elif x < 0:
        return dali(x+1)

def shorthand(raw):
    """
    Converts the written shorthand for Surreals into
    a normal Surreal object
    """
    string = str(raw)

    # Check if input is integer
    if string.isdigit():
        return dali(int(string))

    # Check string for the {L|R} syntax
    m = re.match(r'^{(.*)\|(.*)}$', string)
    if m and len(m.groups()) == 2:
        leftSurreals = set()
        for symbol in m.group(1).split(","):
            if symbol != "":
                leftSurreals.add(shorthand(symbol))
        rightSurreals = set()
        for symbol in m.group(2).split(","):
            if symbol != "":
                rightSurreals.add(shorthand(symbol))
        return Surreal(leftSurreals, rightSurreals)

class BadlyFormed(exceptions.Exception):
    pass

class Surreal(object):
    """
    Surreal number
    """
    def __init__(self, leftSet, rightSet):
        """
        A Surreal number is initialised with a left and right
        set, which both contain Surreal numbers.
        """
        self._is_well_formed(leftSet, rightSet)
        self.leftSet = leftSet
        self.rightSet = rightSet

    def _is_well_formed(self, leftSet, rightSet):
        """
        A Surreal number is well-formed is no member of the right set
        is left-than or equal to a member of the left set.
        """
        for r in rightSet:
            for l in leftSet:
                if r <= l:
                    raise BadlyFormed, "Left %s, right %s not well-formed" % (leftSet, rightSet)
        
    def __le__(self, other):
        """
        A Surreal number x is less than or equal to a surreal number y
        if and only if y is less than or equal to no member of the left
        set of x, and no member of the right set of y is less than or equal
        to x.
        """
        for l in self.leftSet:               
            if other <= l: 
                return False
        for r in other.rightSet:
            if r <= self:
                return False
        return True


    def __eq__(self, other):
        return self <= other and other <= self

    def __repr__(self):
        return 'S{%s|%s}' % (self.leftSet, self.rightSet)

