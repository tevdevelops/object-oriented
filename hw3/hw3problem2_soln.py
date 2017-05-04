"""
Author: Tevin Rivera
Solution module for Homework 3, Problem 2
Object Oriented Programming (50:198:113), Spring 2016

This module implements a class for two-dimensional straight lines.
"""

class StraightLine:
    """
    A class for two-dimensional straight lines represented
    in standard form: ax + by = c
    """
    def __init__(self, inita=0, initb=1, initc=0):
        """
        Constructor creates a straight line with x-coefficient
        inita, y-coefficient initb, and constant coefficient initc
        """
        self.a = inita
        self.b = initb
        if self.a == 0 and self.b == 0:
            raise Exception("Invalid straight line equation")
        self.c = initc

    def __str__(self):
        """
        Return a printable representation of the straight line
        """
        lstr = ""

        # String for x term
        if self.a != 0:
            if self.a == 1:
                lstr += "x"
            elif self.a == -1:
                lstr += "-x"
            else:
                lstr += str(self.a) + "x"

        # String for y term
        if lstr != "":  # This means that the x-coefficient is not 0
            if self.b > 0:
                if self.b == 1:
                    lstr += " + y"
                else:
                    lstr += " + " + str(abs(self.b)) + "y"
            elif self.b < 0:
                if self.b == -1:
                    lstr += " - y"
                else:
                    lstr += " - " + str(abs(self.b)) + "y"
        else:
            if self.b == 1:
                lstr += "y"
            elif self.b == -1:
                lstr += "-y"
            else:
                lstr += str(self.b) + "y"

        # String for constant term
        lstr += " = " + str(self.c)

        return lstr

    def __repr__(self):
        """
        Return a printable representation of the straight line
        """
        return str(self)

    def slope(self):
        """
        Return the slope of the straight line.
        If the line is vertical, None is returned.
        """
        if self.b == 0:
            return None
        else:
            return (-1) * self.a/self.b

    def yintercept(self):
        """
        Return the y-intercept of the straight line
        If the line is vertical, None is returned
        """
        if self.slope() is None:
            return None
        else:
            return self.c/self.b

    def xintercept(self):
        """
        Return the x-intercept of the straight line
        If the line is horizontal, None is returned
        """
        if self.slope() == 0:
            return None
        else:
            return self.c/self.a

    def parallel(self, L):
        """
        Return True if L is parallel to the straight line,
        and False otherwise
        """
        return self.slope() == L.slope()

    def perpendicular(self, L):
        """
        Return True if L is perpendicular to the straight line,
        and False otherwise
        """
        if self.slope() is None:  # if the line is vertical, L must be horizontal
            return L.slope() == 0
        elif self.slope() == 0:   # if the line is horizontal, L must be vertical
            return L.slope() is None
        else:
            return self.slope() * L.slope() == -1

    def intersection(self, L):
        """
        Return the intersection point (a 2-tuple) of L with the straight line.
        If the line is parallel to L, None is returned.
        """
        if self.slope() == L.slope():
            return None
        intpt_xcood = (self.c * L.b - L.c * self.b)/(self.a * L.b - L.a * self.b)
        intpt_ycood = (self.c * L.a - L.c * self.a)/(self.b * L.a - L.b * self.a)

        return (intpt_xcood, intpt_ycood)

    def __eq__(self, other):
        """
        Return True if the line is exactly the same as other, and
        False otherwise
        """
        if self.slope() == None:
            return other.slope() == None and self.xintercept() == other.xintercept()
        return self.slope() == other.slope() and self.yintercept() == other.yintercept()

    def __ne__(self, other):
        """
        Return True if the line and other are not equal,
        and False otherwise
        """
        return not self == other
