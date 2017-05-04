"""
Module for Homework 4, Problem 2
Author: Suneeta Ramaswami
Object-Oriented Programming (50:198:113), Spring 2016

This module contains some functions that manipulate Date objects
"""

from problem1 import *

def weekend_dates(m, y):
    """
    Prints all the weekend dates in month m of year y

    m: an integer between 1 and 12 (inclusive)
    y: a year 
    """
    D = Date(m, 1, y)
    while D.month() == m:
        if D.day_of_week() == "Saturday" or D.day_of_week() == "Sunday":
            print(str(D) + "(" +  D.day_of_week() + ")")
        D = D.nextday()

def first_mondays(y):
    """
    Prints the dates of all the first Mondays of year y

    y: a year
    """
    print("First Mondays of " + str(y) + "\n")
    D = Date(1, 1, y)

    while D.year() == y:
        if D.day_of_week() == "Monday":
            print(D)
            if D.month() == 12:
                return
            else:
                D = Date(D.month() + 1, 1, y)
        else:
            D = D.nextday()

def interval_schedule(start_date, end_date, interval):
    """
    Returns a list of Dates that occur every interval days starting 
    at the date start_date and ending at or before end_date

    start_date: a Date instance
    end_date: a Date instance
    interval: a positive integer
    """

    L = []
    current_date = start_date
    while current_date <= end_date:
        L.append(current_date)
        current_date = current_date + interval
    return L
