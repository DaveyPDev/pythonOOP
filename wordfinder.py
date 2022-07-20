"""Word Finder: finds random words from a dictionary."""

import random 

class WordFinder:
    ...
    def __init__(self,list):
        """ reads from dictionary and returns items read """
        dict_file = open(list)
        self.words = self.parse(dict_file)

        print(f" {len(self.words)} words read")

    def parse(self, dict_file):
        """ parse dictionary file into list of words """
        return [w.strip() for w in dict_file]

    def random(self):
        """ returns a random word """
        return random.choice(self.words)

class SpecialWordFinder:
    """ replaces blank lines and comments with words """

    def parse(self, dict_file):
        """ parse dict_file into list of words skipping over blanks and comments"""
        return [w.strip() for w in dict_file
                    if w.strip() and not w.startswith("#")]

    
