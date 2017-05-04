"""
Author: Tevin Rivera
Solution module for Homework 1, Problem 3
Object Oriented Programming (50:198:113), Spring 2016

This module implements a Pig Latin translator (from English to Pig Latin)
"""

def pig_latin_word(word):
    """
    Returns the Pig Latin translation of an English word.

    word: A string of letters (a single English word without any blank spaces)
    """
    pgword = ""
    if word[0] in "aeiouAEIOU":
        pgword = word + "way"
    else:
        i = 0

        # We use a while loop to get to the first
        # vowel in word
        while (i < len(word)) and (word[i] not in "aeiouAEIOU"):
            i = i + 1

        # i is the index of the first vowel. Hence the consonant
        # cluster at the beginning of word is simply word[:i],
        # which is moved to the end of the translated pig Latin
        # word, followed by "ay"

        pgword = word[i:] + word[:i] + "ay"

    return pgword

def pig_latin_sentence(eng_sentence):
    """
    Returns the Pig Latin translation of an English sentence.
    eng_sentence: A string of characters, composed of English words
                  separated by spaces. A word is a string of letters
                  without blanks, and may end in a punctuation mark
                  (.!?,)
    """
    pgsentence = ""

    # Split the sentence into its component words

    word_list = eng_sentence.split()

    # Translate each word after checking if the last character
    # is a punctuation mark

    for word in word_list:
        if word[-1] in ".!?,":
            pgword = pig_latin_word(word[:-1]) + word[-1]
        else:
            pgword = pig_latin_word(word)
        pgsentence = pgsentence + pgword + " "

    # Return the Pig Latin sentence without the extra
    # blank space at the end.

    return(pgsentence[:-1])

def pig_latin_translator():
    """
    Repeatedly asks the user to enter an English sentence.
    The Pig Latin translation of that sentence is then printed.
    """
    print("                -------------------------------")
    print("                English to Pig Latin Translator")
    print("                -------------------------------")
    answer = "y"
    while (answer[0].lower() == "y"):
        engSentence = input("Enter the English sentence: ")
        print(" ")
        print("In Pig Latin: ", end="")
        print(pig_latin_sentence(engSentence))
        print(" ")
        answer = input("Do another? [y/n] ")
        print(" ")

    print(" ")
    print("Goodbye!")
