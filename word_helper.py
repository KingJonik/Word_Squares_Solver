import requests


class ObtainWords:
    def __init__(self):
        pass

    @staticmethod
    def request_and_save_words():
        """
        Uses a GET request to get all english dictionary words from the given url.
        Then saves them to all_words.txt to be used in the program.

        This is run prior just in case the url doesn't work on the day.
        """
        words = requests.get("http://norvig.com/ngrams/enable1.txt").text.split('\n')
        with open("all_words.txt", "w") as output:
            for word in words:
                output.write(word + '\n')

    @staticmethod
    def open_words_from_text_file():
        """
        Opens the all_words.txt file and parses into a list ready for the program to use.
        :return: List of all english dictionary words.
        """
        with open("all_words.txt") as file:
            lines = file.readlines()
            lines_cleaned = [line.strip("\n") for line in lines]

        return lines_cleaned


# if __name__ == "__main__":
#     # Run GET request to get all words (use if all_words.txt gets deleted)
#     ObtainWords().request_and_save_words()
#
#     # Runs open and parse function to test words in all_words.txt parse correctly
#     test_words_parsed_correctly = ObtainWords().open_words_from_text_file()

