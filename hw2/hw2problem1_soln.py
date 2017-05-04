"""
Author: Tevin Rivera
Solution module for Homework 2, Problem 1
Object Oriented Programming (50:198:113), Spring 2016

This module contains functions about calendar dates. It
contains a function that can print monthly calendars for
any month after (and including) January 1754 AD.
"""


def is_leap(yr):
    """
    Returns True if yr is a leap year and False otherwise

    yr: A positive integer
    """
    if yr%4 == 0 and yr%100 != 0:
        return True
    elif yr%400 == 0:
        return True
    else:
        return False

def monthdays(yr, mon):
    """
    Returns the number of days in the month mon of year yr

    yr: A positive integer
    mon: A positive integer between 1 and 12 (inclusive)
    """
    if mon == 2 and is_leap(yr):
        return 29
    elif mon == 2:
        return 28
    elif mon == 4 or mon == 6 or mon == 9 or mon == 11:
        return 30
    else:
        return 31

def yeardays(yr):
    """
    Returns the number of days in the year yr

    yr: A positive integer
    """
    if is_leap(yr):
        return 366
    else:
        return 365

def wkday_on_first(yr, mon):
    """
    Returns the day of the week (a string) of the first day of month mon of year yr

    yr: A positive integer greater than or equal to 1754
    mon: A positive integer between 1 and 12 (inclusive)
    """
    totaldays = 0
    for y in range(1754, yr):
        totaldays = totaldays + yeardays(y)
    for m in range(1, mon):
        totaldays = totaldays + monthdays(yr, m)
    wkday = totaldays%7
    wkday_names = ["tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "monday"]
    return wkday_names[wkday]

def print_calendar(yr, mon):
    """
    Prints the calendar for month mon of year yr

    yr: A positive integer greater than or equal to 1754
    mon: A positive integer between 1 and 12 (inclusive)
    """

    if yr < 1754 or mon < 1 or mon > 12:
        print("Error: Invalid parameters!")
    else:
        monthnames = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"]
        mname = monthnames[mon-1]

        print("")
        print(str(yr).center(62))  # Field width for centering year is 62
        print(mname.center(62))    # (my choice; yours need not be identical)
        print("")
        print("Su Mo Tu We Th Fr Sa".center(62))

        daysofweek = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
        wkday = wkday_on_first(yr, mon)

        dayofwk = daysofweek.index(wkday) + 1 # returns the day of the week as an integer in range 1-7
        emptyspaces = dayofwk - 1 # number of empty spaces needed on the first line of the calendar.

        print(" "*20, end="")
        for i in range(emptyspaces):
            print(" ".rjust(3), end="")

        # dayofwk keeps track of which day of the week we are currently
        # printing, where sunday is the first day of the week (dayofwk = 1)
        # and saturday is the last day of the week (dayofwk = 7)

        days_in_month = monthdays(yr, mon)
        for i in range(1, days_in_month+1):
            print(str(i).rjust(3), end="")
            if dayofwk == 7:  # If we are at the end of the week, move to the next line
                print("")
                print(" "*20, end="")
                dayofwk = 1
            else:
                dayofwk = dayofwk + 1
        print(" ")
        print(" ")
