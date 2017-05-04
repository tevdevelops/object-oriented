"""
Module for Homework 4, Problem 3
Author: Suneeta Ramaswami
Object-Oriented Programming (50:198:113), Spring 2016

"""

class ChangeJar:
    """
    A class for change jars. A change jar contains an arbitrary collection
    of coins i.e., quarters, dimes, nickels, and pennies. There are no dollar
    bills of any denomination in a change jar.
    """
    def __init__(self, init_jar = {}):
        """
        Initialize the change jar with an intial number
        of quarters, dimes, nickels, and pennies.

        init_jar: A dictionary whose keys are from 25, 10, 5, and 1.
        The value associated with a key is the number of coins of that
        denomination.
        """
        self.changedict = {25:0, 10:0, 5:0, 1:0}
        for key in init_jar:
            if key not in [25, 10, 5, 1]:
                raise Exception("Invalid coin denomination in __init__")
            self.changedict[key] = init_jar[key]

    def get_change(self, dollar_amt):
        """
        Return a ChangeJar containing the number of quarters, dimes,
        nickels, and pennies required to create exact change for
        dollar_amt.

        dollar_amt: A real value representing dollars and cents.
        """
        cent_amt = int(dollar_amt * 100)
        leftover_amt = cent_amt
        return_jar = ChangeJar()
        for coinvalue in [25, 10, 5, 1]:
            while leftover_amt >= coinvalue and self[coinvalue] > 0:
                self.changedict[coinvalue] -= 1
                return_jar.insert(coinvalue, 1)
                leftover_amt -= coinvalue

        # If we couldn't make change with quarters, dimes, nickels, and pennies,
        # we will try to make change with just dimes, nickels, and pennies.
        # First, we put back the change we removed from self, and reset return_jar.

        if leftover_amt > 0:
            for coinvalue in [25, 10, 5, 1]:
                self.insert(coinvalue, return_jar[coinvalue])
            return_jar = ChangeJar()
            leftover_amt = cent_amt
            for coinvalue in [10, 5, 1]:
                while leftover_amt >= coinvalue and self[coinvalue] > 0:
                    self.changedict[coinvalue] -= 1
                    return_jar.insert(coinvalue, 1)
                    leftover_amt -= coinvalue

        # If we couldn't make exact change with dimes, nickels, and pennies,
        # then it means that we cannot make exact change from this change
        # jar. This is because if there is exact change with the smallest number
        # of coins made entirely of nickels and pennies, then it must mean that 
        # there are no dimes in the change jar because otherwise either a pair of 
        # nickels can be replaced by a dime (thus using fewer coins), or, if only one
        # nickel is used to make change, ten pennies can be replaced by a dime, or 
        # if fewer than ten pennies are used, the nickel and five pennies can be
        # replaced by a dime.
            
        if leftover_amt > 0:
            print("Cannot make exact change.")
            for coinvalue in [10, 5, 1]:
                self.insert(coinvalue, return_jar[coinvalue])
            return ChangeJar()
        else:
            return return_jar

    def __getitem__(self, idx):
        """
        Return the number of quarters, dimes, nickels, or pennies
        when index is 25, 10, 5, or 1, respectively.
        """
        if idx not in [25, 10, 5, 1]:
            raise IndexError
        return self.changedict[idx]
            
    def insert(self, coin_value, num_coins):
        """
        Add num_coins number of coins of denomination coin_value
        into the change jar.

        coin_value: One of 25, 10, 5, or 1
        num_coins: An integer reprsenting the number of coins
        """
        if coin_value not in [25, 10, 5, 1]:
            raise Exception("Invalid coin denomination in insert")
        self.changedict[coin_value] += num_coins

    def total_value(self):
        """
        Return the total dollar value in the change jar (as a real number)
        """
        tot = 0
        for k in self.changedict:
            tot += k * self.changedict[k]
        return tot/100

    def __str__(self):
        """
        Return a string representation of the change jar
        """
        astr = "ChangeJar: %d Quarters. %d Dimes. %d Nickels. %d Pennies.\n"%(self.changedict[25],self.changedict[10],self.changedict[5],self.changedict[1])
        astr += "          Total value: $%.2f\n"%(self.total_value())
        return astr

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        """
        Return a change jar containing all the coins from the two
        change jars that are operands to the + operator.
        """
        sumjar = ChangeJar()
        for coinvalue in [25, 10, 5, 1]:
            sumjar.insert(coinvalue, self[coinvalue] + other[coinvalue])
        return sumjar

    def __eq__(self, other):
        """
        Return True if the operand change jars have exactly the same
        number of coins of each denomination, and False otherwise.
        """
        for coinvalue in [25, 10, 5, 1]:
            if self[coinvalue] != other[coinvalue]:
                return False
        return True

    def __ne__(self, other):
        """
        Return True if and only if the operand change jars are not equal
        to each other.
        """
        return not self == other
        
