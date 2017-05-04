"""
Author: Tevin Rivera
Solution module for Homework 1, Problem 2
Object Oriented Programming (50:198:113), Spring 2016

This module contains three functions that allow the
user to play multiple games of craps.
"""

import random

def roll_dice():
    """
    Returns the total face value resulting from
    rolling two dice (a number between 2 and 12)
    """
    return (random.randint(1, 6) + random.randint(1, 6))


def play_one_game():
    """
    Plays one game of Craps. Returns a 0 if the game
    is won, and 1 if the game is lost.
    """
    sum = roll_dice()
    print("You rolled ", sum)
    if (sum == 7 or sum == 11):
        return 1
    elif (sum == 2 or sum == 3 or sum == 12):
        return 0
    else:
        point = sum
        print("Your point is ", point)
        print(" ")
        newsum = 0
        while (newsum != point and newsum != 7):
            newsum = roll_dice()
            print("You rolled", newsum)
        if (newsum == point):
            return 1
        else:
            return 0


def craps():
    """
    Allows the player to repeatedly play a game of Craps. The player
    has an initial bank amount of $1000. S/he must wager a dollar amount
    prior to the start of the game. The bank balance is increased or
    decreased by the wager amount when the player wins or loses the game,
    respectively.
    """
    print("                ----------------------------")
    print("                Welcome to the Craps program")
    print("                ----------------------------")
    print(" ")

    balance = 1000
    print("Your initial bank balance is $1000.")
    print(" ")
    playagain = "y"

    while (playagain[0].lower() == "y"):
        wagerstr = input("What is your wager? ")
        wager = int(wagerstr)
        while (wager > balance):
            print("Cannot wager more than $", balance, end="")
            wagerstr = input("Re-enter wager: ")
            wager = int(wagerstr)
        print("Okay, let's play.")
        print(" ")

        winorlose = play_one_game()
        if (winorlose == 1):
            print("You win!!")
            balance = balance + wager
        else:
            print("Sorry, you lose!")
            balance = balance - wager

        print(" ")
        print("Your new bank balance is $", balance)
        print(" ")
        playagain = input("Do you want to play again? [y/n] ")

    print(" ")
    if (balance < 1000):
        print("Sorry you lost money. Better luck next time!")
    elif (balance > 1000):
        print("Hey, you made some money! Congratulations!")
    else:
        print("At least you broke even....")

    print(" ")

if __name__ == "__main__":
    craps()
