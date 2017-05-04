"""
Author: Tevin Rivera
Solution module for Homework 2, Problem 2
Object Oriented Programming (50:198:113), Spring 2016

This module computes the frequency distribution of modules in a text file.
"""

import string

def freq_distribution(infile, distfile):
    """
    In output file named distfile, write the frequency
    distribution of words in input file infile. Words
    are listed in alphabetical order.

    infile: a string
    distfile: a string
    """
    freq_dict = freq_dictionary(infile)
    dfile = open(distfile, 'w')
    keys = list(freq_dict.keys())
    keys.sort()
    max_wordlen = max([len(k) for k in keys])  # length of the longest word
    wordwidth = max_wordlen + 2 # field width for printing words in distfile
    for k in keys:
        dfile.write(k.ljust(wordwidth) + "%7d\n"%(freq_dict[k]))
    dfile.close()

def ordered_freq_distribution(infile, ordered_distfile):
    """
    In output file named ordered_distfile, write the frequency
    distribution of words in input file infile. The frequencies
    are listed in descending order.

    infile: a string
    ordered_distfile: a string
    """
    freq_dict = freq_dictionary(infile)
    ofile = open(ordered_distfile, 'w')

    dict_pairs = list(freq_dict.items()) #Make a list of key-value pairs from freq_dict
    rev_dict_pairs = [(p[1], p[0]) for p in dict_pairs]  #Reverse order of items in each pair,
                                                         # so the frequency is listed first


    # Sort the above list. Now frequencies are in increasing order. Furthermore,
    # words with the same frequency will appear in alphabetically sorted order as well.

    rev_dict_pairs.sort()
    rev_dict_pairs.reverse()

    # Now rev_dict_pairs has the frequencies in decreasing order, but words of
    # the same frequency are now in reverse alphabetical order. We put them
    # in correct alphabetical order in the list final_pairs

    final_pairs = []
    insert_idx = 0
    current_idx = 0
    current_freq = rev_dict_pairs[0][0]

    # In the following loop, all words with frequency current_freq
    # are inserted at index insert_idx. This puts all words with the
    # same frequency in correct alphabetical order.

    for p in rev_dict_pairs:
        if p[0] != current_freq:
            current_freq = p[0]
            insert_idx = current_idx
        final_pairs.insert(insert_idx, p)
        current_idx += 1

    # Now we are ready to write into the output file

    max_wordlen = max([len(p[1]) for p in final_pairs])  # length of the longest word
    wordwidth = max_wordlen + 2                          # field width for printing words

    for p in final_pairs:
        ofile.write(p[1].ljust(wordwidth) + "%7d\n"%(p[0]))
    ofile.close()

def freq_dictionary(infile):
    """
    Read in text from input text file called infile and return
    the dictionary containing key:value pairs where key is a word
    occuring in infile, and value as the frequency of that word
    in infile. A word is any consecutive sequence of letters of
    the alphabet.

    infile: a string
    """

    ifile = open(infile, 'r')
    freq_dict = {}
    for line in ifile:
        for punc in string.punctuation:     # remove all punctuation characters
            line = line.replace(punc, ' ')
        for d in "0123456789":              # remove all digits
            line = line.replace(d, ' ')
        line = line.lower()                 # make all characters lower case
        wordlist = line.split()
        for word in wordlist:
            freq_dict[word] = freq_dict.get(word, 0) + 1
    ifile.close()
    return freq_dict
