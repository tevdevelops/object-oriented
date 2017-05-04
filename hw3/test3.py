"""
Author: Suneeta Ramaswami
Test module for Homework 3, Problem 3
Object Oriented Programming (50:198:113), Spring 2016

This module tests the implementation of the Container class and
related functions in Problem #3 of Homework Assignment 3
"""

# from problem3a import Container
# from problem3b import *

from hw3problem3a_soln import Container
from hw3problem3b_soln import *

if __name__ == "__main__":

    print("----------------------------------------------------------------")
    print("Testing implementation for Container class and related functions")
    print("----------------------------------------------------------------")
    A = Container()
    A.insert(1)
    A.insert(2)
    A.insert("abc")
    A.insert(2)
    A.insert([4])

    B = Container()
    B.insert(3)
    B.insert(2)
    B.insert(4)
    B.insert("abcd")
    B.insert([4])
    B.insert("xy")

    print("Two containers, A and B, have been created.")
    print("Container A: ")
    print(A)
    print("\nContainer B: ")
    print(B)

    print("\nTesting erase_one: Erasing 'abc' from A\n")
    A.erase_one("abc")

    print("Now Container A is:")
    print(A)

    print("\nTesting erase_all: Erasing all 2 from A\n")
    A.erase_all(2)

    print("Now Container A:")
    print(A)

    print("\nInserting deleted items back into A, so it is the same as before...")
    A.insert("abc")
    A.insert(2)
    A.insert(2)

    print("\nTesting count:\n")
    print("Count of 2 in A: ", A.count(2))
    print("Count of 4 in B: ", B.count(4))

    print("\nTesting items: \n")
    print("items in A: ", A.items())
    print("items in B: ", B.items())

    S = A + B
    print("\nTesting + operator: S = A + B\n")
    print("S is: ", S)

    D = A - B
    print("\nTesting - operator: D = A - B\n")
    print("D is: ", D)

    I = A * B
    print("\nTesting * operator: I = A * B\n")
    print("I is: ", I)

    print("\n\n------------------------------\n")
    print("Testing functions in problem3b")
    print("------------------------------\n\n")

    C = symmetric_difference(A, B)
    print("The symmetric difference of A and B: ")
    print(C)

    print("\nTesting the function subcontainer: ")
    if subcontainer(A, S):
        print("A is a subcontainer of S. (CORRECT ANSWER)")
    else:
        print("A is NOT a subcontainer of S. (INCORRECT ANSWER)")

    print("\nTesting the function remove_repeats on Container S: ")
    remove_repeats(S)
    print("\nContainer S is now:")
    print(S)

    C1 = Container()
    C2 = Container()

    C1.insert(1)
    C1.insert(2)
    C1.insert(2)
    C1.insert(3)
    C1.insert(4)
    C1.insert(4)
    C1.insert(4)

    C2.insert(4)
    C2.insert(1)
    C2.insert(2)
    C2.insert(3)
    C2.insert(3)

    print("\nTesting the function similar: ")
    if similar(C1, C2):
        print("Containers C1 and C2 are similar. (CORRECT ANSWER).")
    else:
        print("Containers C1 and C2 are NOT similar. (INCORRECT ANSWER).")
    if similar(A, B):
        print("Containers A and B are similar. (INCORRECT ANSWER).")
    else:
        print("Containers A and B are NOT similar. (CORRECT ANSWER).")


    print("\nThat's all! Goodbye!\n")

    
