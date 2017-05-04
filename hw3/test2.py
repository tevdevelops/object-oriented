"""
Author: Suneeta Ramaswami
Test module for Homework 3, Problem 2
Object Oriented Programming (50:198:113), Spring 2016

This module tests the implementation of the StraightLine
class for Problem #2 of Homework Assignment 3
"""

from problem2 import StraightLine

if __name__ == "__main__":
    print("\n-------------------------------------------------------")
    print("Testing StraigtLine class implementation in problem2.py")
    print("-------------------------------------------------------\n")

    line1 = StraightLine(2, 0, 3)
    line2 = StraightLine(0, 3, 2)
    line3 = StraightLine(2, 5, 4)
    line4 = StraightLine(1, 2, -3)

    print("Four StraightLine objects have been created. Testing __str__ method:")
    print("--------------------------------------------------------------------\n")

    print("line1: ", line1)
    print("line2: ", line2)
    print("line3: ", line3)
    print("line4: ", line4)

    L = [line1, line2, line3, line4]

    print("\nTesting slope() method")
    print("----------------------\n")

    for i in range(len(L)):
        if L[i].slope() is None:
            print("The slope of ", L[i], " is undefined (it is vertical)")
        else:
            print("The slope of ", L[i], " is %.2f"%(L[i].slope()))

    print("\nTesting yintercept() and xintercept() methods")
    print("---------------------------------------------\n")

    for i in range(len(L)):
        if L[i].yintercept() is None:
            print("The y-intercept of ", L[i], " is undefined (it is vertical)")
        else:
            print("The y-intercept of ", L[i], " is %.2f"%(L[i].yintercept()))
        if L[i].xintercept() is None:
            print("The x-intercept of ", L[i], " is undefined (it is horizontal)")
        else:
            print("The x-intercept of ", L[i], " is %.2f"%(L[i].xintercept()))
        print(" ")

    line5 = StraightLine(-2, 1, 3)        # perpendicular to line4
    line6 = StraightLine(4, 10, -10)      # parallel to line3
    line7 = StraightLine(1, 0, -1)        

    print("\nTesting parallel() method")
    print("-------------------------\n")

    if line1.parallel(line7):
        print("Lines ", line1, " and ", line7, " are parallel. (CORRECT ANSWER)")
    else: 
        print("Lines ", line1, " and ", line7, " are NOT parallel. (INCORRECT ANSWER)")
    
    if line6.parallel(line3):
        print("Lines ", line6, " and ", line3, " are parallel. (CORRECT ANSWER)")
    else: 
        print("Lines ", line6, " and ", line3, " are NOT parallel. (INCORRECT ANSWER)")

    if line3.parallel(line4):
        print("Lines ", line3, " and ", line4, " are parallel. (INCORRECT ANSWER)")
    else: 
        print("Lines ", line3, " and ", line4, " are NOT parallel. (CORRECT ANSWER)")
    
    print("\nTesting perpendicular() method")
    print("------------------------------\n")

    if line1.perpendicular(line2):
        print("Lines ", line1, " and ", line2, " are perpendicular. (CORRECT ANSWER)")
    else: 
        print("Lines ", line1, " and ", line2, " are NOT perpendicular. (INCORRECT ANSWER)")
    
    if line5.perpendicular(line4):
        print("Lines ", line5, " and ", line4, " are perpendicular. (CORRECT ANSWER)")
    else: 
        print("Lines ", line5, " and ", line4, " are NOT perpendicular. (INCORRECT ANSWER)")

    if line3.perpendicular(line4):
        print("Lines ", line3, " and ", line4, " are perpendicular. (INCORRECT ANSWER)")
    else: 
        print("Lines ", line3, " and ", line4, " are NOT perpendicular. (CORRECT ANSWER)")


    print("\nTesting intersection() method")
    print("-----------------------------\n")

    print("Intersection of lines ", line1, " and ", line7, " is ", line1.intersection(line7))
    print("Intersection of lines ", line3, " and ", line6, " is ", line3.intersection(line6))
    print("Intersection of lines ", line1, " and ", line2, " is ", line1.intersection(line2))
    print("Intersection of lines ", line4, " and ", line5, " is ", line4.intersection(line5))
    print("Intersection of lines ", line3, " and ", line4, " is ", line3.intersection(line4))

    line8 = StraightLine(2, 4, -6)

    print("\nTesting equality and inequality operators")
    print("-----------------------------------------\n")

    if line4 == line8:
        print("Lines ", line4, " and ", line8, " are equal. (CORRECT ANSWER)")
    else: 
        print("Lines ", line4, " and ", line8, " are NOT equal. (INCORRECT ANSWER)")

    if line3 != line4: 
        print("Lines ", line3, " and ", line4, " are NOT equal. (CORRECT ANSWER)")
    else: 
        print("Lines ", line3, " and ", line4, " are equal. (INCORRECT ANSWER)")

    if line1 == line1:
        print("Lines ", line1, " and ", line1, " are equal. (CORRECT ANSWER)")
    else: 
        print("Lines ", line1, " and ", line1, " are NOT equal. (INCORRECT ANSWER)")

    print("\nThat's all, folks! Goodbye.\n")
