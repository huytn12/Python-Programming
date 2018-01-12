# Mab Libs
# A program that reads in text files and lets the user add their own text anywhere the word
# ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

import shelve, sys

with shelve.open('madLibs') as myFile:
    for word in ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']:
        myFile[word] = input('Enter an %s' % word)

    