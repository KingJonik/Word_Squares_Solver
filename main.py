"""
Main controller file for word square program
"""
import sys


from filter_words import FilterWords
from word_square_finder import WordSquareFinder
from word_helper import ObtainWords


class FindSolution:
    """
    Class that solves an input of a number, n, followed by a string of letters with length
    of n^2 into a valid word square should one exist.
    """
    def __init__(self, initial_input):
        self.all_words = ObtainWords.open_words_from_text_file()
        self.max_length = int(initial_input.split(" ")[0])
        self.letters = initial_input.split(" ")[1]

    def run(self):
        """
        Combines all the processing together to find and validate a valid word square from the input.
        :return: List of words that make a valid word square. (or empty list if one isn't found)
        """
        possible_words, singular_letters = FilterWords(self.all_words, self.max_length, self.letters).run()
        solution = WordSquareFinder(possible_words, self.max_length, singular_letters, self.letters).run()

        # Output word square:
        print("----------------")
        print("--- SOLUTION ---")
        print("----------------")
        for word in solution:
            print(" ".join(word))

        return solution


def print_help():
    """
    Prints help message if command line command run wrong
    """
    print("Please run correct command:")
    print("python main.py arg[1] arg[2]")
    print("arg[1] = word length (n)")
    print("arg[2] = letter string of length n^2")
    print()
    print("An example:")
    print("python main.py 4 eeeeddoonnnsssrv")


if __name__ == "__main__":
    if sys.argv:
        word_length = sys.argv[1]
        letters = sys.argv[2]
        if len(sys.argv[2]) == int(word_length)**2:
            FindSolution(word_length + " " + letters).run()
        else:
            print_help()
    else:
        print_help()

