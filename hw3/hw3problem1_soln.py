"""
Author: Tevin Rivera
Solution module for Homework 3, Problem 1
Object Oriented Programming (50:198:113), Spring 2016

This module implements some recursive functions. Function documentation
omitted by instructor.
"""

def replace_element(L, oldel, newel):
    if L == []:
        return []
    elif L[0] == oldel:
        return [newel] + replace_element(L[1:], oldel, newel)
    else:
        return [L[0]] + replace_element(L[1:], oldel, newel)


def inverse_pair(L):
    if len(L) < 2:
        raise Exception("list must have at least two elements")
    elif len(L) == 2:
        return L[0] + L[1] == 0
    elif L[0] + L[-1] == 0:
        return True
    else:
        return inverse_pair(L[1:]) or inverse_pair(L[:-1])


def occurrences(astr, substr):
    if len(astr) < len(substr):
        return 0
    elif astr[:len(substr)] == substr:
        return 1 + occurrences(astr[len(substr):], substr)
    else:
        return occurrences(astr[1:], substr)
