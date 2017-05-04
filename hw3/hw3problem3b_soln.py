"""
Author: Suneeta Ramaswami
Solution module for Homework 3, Problem 3
Object Oriented Programming (50:198:113), Spring 2016

This module some functions to manipulate Container objects.
"""



from hw3problem3a_soln import Container

def symmetric_difference(c1, c2):
    """
    Return a container that is the symmetric difference
    of c1 and c2.

    c1, c2: Containers
    """

    return (c1 - c2) + (c2 - c1)
    
def subcontainer(c1, c2):
    """
    Return True if c1 is a subcontainer of c2 and
    False otherwise. A container c1 is said to be
    a subcontainer of c2 if every item in c1 is also
    in c2.

    c1, c2: Containers
    """
    for item in c1.items():
        if c1.count(item) > c2.count(item):
            return False
    return True

def remove_repeats(C):
    """
    Remove all repetitions of each item in C (one
    copy is retained)

    C: A Container 
    """
    distinct_items = C.items()
    for item in distinct_items:
        C.erase_all(item)
    for item in distinct_items:
        C.insert(item)

def similar(A, B):
    """
    Return True if A and B contain exactly the
    same items (their counts may differ).

    A, B: Containers
    """
    for item in A.items():
        if item not in B.items():
            return False
    for item in B.items():
        if item not in A.items():
            return False
    return True

