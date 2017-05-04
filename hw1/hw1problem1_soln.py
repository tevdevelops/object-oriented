"""
Author: Tevin Rivera
Solution module for Homework 1, Problem 1
Object Oriented Programming (50:198:113), Spring 2016

This module contains functions about magic numbers. A
magic number m is a number greater than 1 whose divisors
(other than m) add up to m.
"""

def magic(n):
    """
    Returns True if n is a magic number and False otherwise

    n: An integer greater than or equal to 1
    """
    sumdivisors = 0
    for i in range(1,n):
        if n%i == 0:
            sumdivisors = sumdivisors + i
    return (sumdivisors == n)

def magic_list(num):
    """
    Returns a list of all magic numbers between 2 and num (inclusive)

    num: A positive integer
    """
    L = []
    for i in range(2, num+1):
        if magic(i):
            L.append(i)
    return L
