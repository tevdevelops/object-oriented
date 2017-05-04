"""
Module for Homework 4, Problem 1
Author: Suneeta Ramaswami
Object-Oriented Programming (50:198:113), Spring 2016

Class and methods have not been documented by the instructor
due to time constraints!
"""

class Date:
    min_year = 1800

    def __init__(self, init_m = 1, init_d = 1, init_y = min_year):
        if init_m < 1 or init_m > 12:
            raise AritmeticError("Invalid Date assignment")
        if init_y < self.min_year:
            raise AritmeticError("Invalid Date assignment")
        self.__m = init_m
        self.__y= init_y
        monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.year_is_leap():
            monthdays[1] = 29
        if init_d < 1 or init_d > monthdays[self.__m-1]:
            raise ArithmeticError("Invalid Date assignment")
        self.__d = init_d

    def month(self):
        return self.__m

    def day(self):
        return self.__d

    def year(self):
        return self.__y

    def year_is_leap(self):
        if self.__y%100 != 0 and self.__y%4 == 0:
            return True
        elif self.__y%400 == 0:
            return True
        else:
            return False

    def daycount(self):
        monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.year_is_leap():
            monthdays[1] = 29
        total = 0
        d = Date(1, 1, self.min_year)
        while d.year() < self.year():  # This loop counts number of days in whole years
            total += 365
            if d.year_is_leap():
                total += 1
            d = Date(1, 1, d.year() + 1)
        while d.month() < self.month():  # This loop counts number of days in whole months
            total += monthdays[d.month() - 1]
            d = Date(d.month() + 1, 1, d.year())
        total += self.day()
        return total

    def day_of_week(self):
        numdays = self.daycount()
        if numdays%7 == 0:
            return "Tuesday"
        elif numdays%7 == 1:
            return "Wednesday"
        elif numdays%7 == 2:
            return "Thursday"
        elif numdays%7 == 3:
            return "Friday"
        elif numdays%7 == 4:
            return "Saturday"
        elif numdays%7 == 5:
            return "Sunday"
        else:
            return "Monday"

    def nextday(self):
        """
        Return the date of the following day.
        Instance remains unchanged.
        """
        monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.year_is_leap():
            monthdays[1] = 29
        if self.day() == monthdays[self.month() - 1]:
            if self.month() == 12:
                return Date(1, 1, self.year() + 1)
            else:
                return Date(self.month() + 1, 1, self.year())
        else:
            return Date(self.month(), self.day() + 1, self.year())

    def prevday(self):
        """
        Return the date of the previous day.
        Instance remains unchanged
        """
        monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.year_is_leap():
            monthdays[1] = 29
        if self.day() == 1:
            if self.month() == 1:
                if self.year() == self.min_year:
                    raise ArithmeticError("Invalid use of prevday")
                else:
                    return Date(12, 31, self.year() - 1)
            else:
                return Date(self.month() - 1, monthdays[self.month() - 2], self.year())
        else:
            return Date(self.month(), self.day() - 1, self.year())

    def __add__(self, n):
        add_day = Date(self.month(), self.day(), self.year())
        for i in range(n):
            add_day = add_day.nextday()
        return add_day

    def __sub__(self, n):
        sub_day = Date(self.month(), self.day(), self.year())
        for i in range(n):
            sub_day = sub_day.prevday()
        return sub_day

    def __lt__(self, other):
        if self.year() < other.year():
            return True
        elif self.year() == other.year():
            if self.month() < other.month():
                return True
            elif self.month() == other.month():
                return self.day() < other.day()
        return False
        
    def __eq__(self, other):
        return ((self.year() == other.year()) and
                (self.month() == other.month()) and
                (self.day() == other.day()))

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return self > other or self == other

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        monthnames = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"]
        return "%s %d, %d"%(monthnames[self.month() - 1], self.day(), self.year())

    def __repr__(self):
        return str(self)
