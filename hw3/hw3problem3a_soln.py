"""
Author: Tevin Rivera
Solution module for Homework 3, Problem 3
Object Oriented Programming (50:198:113), Spring 2016

This module implements a container class for an unordered collection
of items in which each item may appear multiple times.
"""

class Container:
    """
    An instance stores an unordered collection of items.
    An item may occur several times.
    """

    def __init__(self):
        """
        Initialize the container to an empty one.
        """
        self.contents = []

    def insert(self, item):
        """
        Insert item into container.
        """
        self.contents.append(item)

    def erase_one(self, item):
        """
        Remove one occurrence of item from container.
        """
        try:
            self.contents.remove(item)
        except:
            pass

    def erase_all(self, item):
        """
        Remove all occurrences of item from container.
        """
        try:
            while True:
                self.contents.remove(item)
        except:
            pass

    def count(self, item):
        """
        Return the number of occurrences of item in the container.
        """
        return self.contents.count(item)

    def items(self):
        """
        Return the list of distinct items in the container.
        """
        answer = []
        for item in self.contents:
            if item not in answer:
                answer.append(item)
        return answer

    def __str__(self):
        """
        Return a string representation of the container.
        """
        astr = ""
        for item in self.items():
            astr = astr + (str(item) + " ") * self.count(item)
        return astr[:-1]

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        """
        Returns the union of two containers.
        other: A Container instance.
        """
        U = Container()
        for item in self.contents + other.contents:
            U.insert(item)
        return U

    def __sub__(self, other):
        """
        Returns the difference of two containers. The
        difference of two containers A and B is a container
        that contains only those items in A that do not
        occur in B.
        other: A Container instance.
        """
        D = Container()
        for item in self.items():
            if other.count(item) == 0:
                for n in range(self.count(item)):
                    D.insert(item)
        return D

    def __mul__(self, other):
        """
        Returns the intersection of two containers. The count
        of an item in the intersection is the minimum of the
        count of that item in each of the two containers.
        other: A Container instance.
        """
        I = Container()
        common_items = [i for i in self.items() if i in other.items()]
        for item in common_items:
            for n in range(min(self.count(item), other.count(item))):
                I.insert(item)
        return I
