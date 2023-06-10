class FilterWords:
    """
    Class to process a list of all words down to only those possible from the letter input.

    Criteria:
        - Meets the expected word character length.
        - Is a word that can be made from the input unique letters.
        - Word doesn't contain more than 1 singular letter
        - Word doesn't contain more than the existing counts per input letter.
    """

    def __init__(self, all_words, max_length, letters):
        self.all_words = all_words
        self.letters = letters
        self.max_length = max_length

    @staticmethod
    def get_unique_letters(letters):
        """
        Gets all unique letters from an input of letters.
        :param letters: a string of letters to reduce down to unique letters.
        :return: List of all unique letters
        """
        return set(letters)

    @staticmethod
    def get_singular_letters(letters, unique_letters):
        """
        Finds all singular letters (letters that appear only once) from input letters.
        :param letters: All letters to search through.
        :param unique_letters: Set of all unique letters to check through.
        :return: List of singular letters.
        """
        result = []
        for letter in unique_letters:
            if letters.count(letter) == 1:
                result.append(letter)
        return result

    @staticmethod
    def get_letter_counts(letters, unique_letters):
        """
        Creates dictionary of all letter counts.
        :param letters: String of letters to count through
        :param unique_letters: Set of unique letters to obtain appearance count for from letters.
        :return: Dictionary of { letter:count } pairs.
        """
        result = {}
        for letter in unique_letters:
            result[letter] = letters.count(letter)
        return result

    @staticmethod
    def find_possible_words(all_words, max_length, unique_letters, singular_letters, letter_counts):
        """
        Find possible words that meet the following criteria:
            - Meets the expected word character length.
            - Is a word that can be made from the input unique letters.
            - Word doesn't contain more than 1 singular letter
            - Word doesn't contain more than the existing counts per input letter.

        :param all_words: List of all dictionary words to be reduced down.
        :param max_length: Word length to filter for.
        :param unique_letters: Set of unique letters to check words against and filter down.
        :param singular_letters: List of singular letters to check against and filter down.
        :param letter_counts: Dict of letter counts to check against and filter down.
        :return: A reduced list of words to validate into a word square.
        """
        length_reduced = [word for word in all_words if len(word) == max_length]
        non_used_letter_reduced = [word for word in length_reduced if unique_letters.issuperset(word)]
        singular_counts_reduced = []
        for word in non_used_letter_reduced:
            add_word = True
            counts = 0
            for letter in singular_letters:
                counts += word.count(letter)
            if counts > 1:
                add_word = False
            if add_word:
                singular_counts_reduced.append(word)

        letter_counts_reduced = []
        for word in singular_counts_reduced:
            add_word = True
            for key, value in letter_counts.items():
                if word.count(key) > value:
                    add_word = False
                    break
            if add_word:
                letter_counts_reduced.append(word)

        return letter_counts_reduced

    def run(self):
        """
        Finds all possible words and key statistics, returns all needed words / statistics.
        :return: List of all possible words to be validated into a word square.
        :return: List of all singular letters.
        """
        if len(self.all_words) == 0:
            # Prevents iterating over an empty list error.
            possible_words = []
            singular_letters = []
        else:
            unique_letters = self.get_unique_letters(self.letters)
            singular_letters = self.get_singular_letters(self.letters, unique_letters)
            letter_counts = self.get_letter_counts(self.letters, unique_letters)
            possible_words = self.find_possible_words(self.all_words, self.max_length, unique_letters, singular_letters,
                                                      letter_counts)

        return possible_words, singular_letters
