from filter_words import FilterWords


class WordSquareFinder:
    """
    Class to take a list of (pre-processed) words and methodically search over them to find
    an ordered list that make up a valid word square.

    """

    def __init__(self, words, max_length, singular_letters, input_string):
        """
        Setup given parameters and initialise a blank word square.
        """
        self.words = words
        self.max_length = max_length
        self.singular_letters = singular_letters
        self.input_string = "".join(sorted(input_string))
        self.solution = []

    def is_word_possible_for_given_index(self, word, index_j):
        """
        Efficiency Measure: Singular letters can only go on the negative diagonal since there's no duplicates to
                            'mirror' in another word. i.e. index of singular letter must equal word number, j.

        Say we have a singular letter 'd' and word_j = 'aced'.
        1. If this is under consideration for the first word in the square, then the letter 'd' in 'aced'
           would be an index of 3 for word_0, meaning it won't be on the negative diagonal.
        2. However, if we are looking at word_3, then an index od 3 would be on the leading diagonal.

        Applying this check allows a word under consideration to be removed 'now' instead of at the end of its
        iteration when no valid word square is found.

        :param word: word_j that is under consideration.
        :param index_j: The index a unique letter must be on for the word_j to be valid in index j.
        :return: True/False to indicate if word is in the right order.
        """
        result = False
        for letter in self.singular_letters:
            result = True
            if letter in word:
                result = False
                if index_j == word.index(letter):
                    result = True
                    break

        return result

    def cross_ref_partial_square(self, word, index_j):
        """
        To check the current word_j under consideration, it needs to be compared to the previous word(s).
        The rule for a word square is word_j[0 to j-1] == word[j] for each word in the existing partial square.

        Say we have 0 words, then the current word_0 automatically gets added as there's nothing to check it to.
        e.g. 'moan'

        For word_1: Can only be valid if word_1[0] = word_0[1] i.e. symmetry in the negative diagonal.
        e.g. 'once' has first letter that matches the 2nd letter of the first word.
        Creating: m o a n
                  o n c e

        For word_2: Can only be valid if word_2[0,1] = string(word_0[2], word_1[2]).
        e.g. 'acme' has first characters "ac" and string(word_0[2], word_1[2]) is also "ac"
        Creating: m o a n
                  o n c e
                  a c m e

        And so on.

        :param word: word_j that is under consideration to be added to the next 'level' of the partial word square.
        :param index_j: Used to index the partial strings to check for the required symmetry.
        :return: True/False to indicate if word is valid to be added or not.
        """
        horizontal_partial_string = word[0:index_j]
        vertical_partial_string = "".join([word[index_j] for word in self.solution])

        return horizontal_partial_string == vertical_partial_string

    def is_word_square_valid_with_input_string(self):
        """
        There is likely to be possible words that do make a valid word square, but don't 'stringify' into the same
        string as the given input. This checks this condition.
        :return: True/False to indicate if we should keep looking or not.
        """
        word_square_string = "".join(self.solution)
        sorted_word_square_string = "".join(sorted(word_square_string))

        return sorted_word_square_string == self.input_string

    @staticmethod
    def reduce_starts_with_words(words, word_0):
        """
        Efficiency Measure: word_j for j > 0 will start with the j-th index of word_0, so remove those that don't.

        Keeps each word that has a starting index that is in the 1:(max_length) index range of word_0.
        :return: List of words to keep.
        """
        start_letters = word_0[1:]
        check_list = [bit for bit in word_0[1:]]
        words_to_keep = []
        for word in words:
            if word[0] in start_letters:
                words_to_keep.append(word)
                # Tick off checklist to ensure we have words for every character
                if word[0] in check_list:
                    check_list.remove(word[0])

        if len(check_list) == 0:
            return words_to_keep
        else:
            return []

    def solve_word_j(self, words, j, word_0=""):
        """
        Recursive function to assess iterate over each word, asses validity to be added to the partial word square
        and if the word is added then self-call to add the next 'level' word.

        Has exit clauses to exit should a solution be found (max length equals number of words) or if a particular
        word has exhausted all of its next 'level' searches.
        """
        if (j > 0) and (j < self.max_length):
            # Obtains words that start with word_0[j]
            words = [word for word in self.words if word[0] == word_0[j] and word not in self.solution]
        try_count = 0
        total_tries = len(words)
        for word in words:
            try_count += 1

            # Exit condition 1: Possible solution found.
            if len(self.solution) == self.max_length:
                if self.is_word_square_valid_with_input_string():
                    # Solution confirmed
                    break
                else:
                    # Possible solution doesn't match input string
                    self.solution.pop()
                    break

            # Otherwise continue as a solution hasn't been found.
            else:
                words_to_pass = words.copy()
                found_word = False

                # Base case for word_0 (i.e. j == 0)
                if j == 0:
                    word_0 = word
                    if self.is_word_possible_for_given_index(word_0, 0):
                        # Reduce impossible words given word_0 selection.
                        words_to_pass = self.reduce_starts_with_words(words_to_pass, word_0)
                        if len(words_to_pass) > 0:
                            # i.e. there are words left to consider at the 'next' level then continue.
                            self.solution.append(word_0)
                            found_word = True

                # Recursive case for word_j (i.e. j != 0)
                else:
                    word_j = word
                    if self.is_word_possible_for_given_index(word_j, j):
                        if self.cross_ref_partial_square(word_j, j):
                            # Update possible words by checking the remaining letters should this word be accepted.
                            words_to_pass = [word for word in words_to_pass if word != word_j]
                            self.solution.append(word_j)
                            found_word = True

                """
                Recursively move to the next word if we have found a valid word for word_j.
                This will only trigger if all above checks have passed for a valid word and there being words left to
                consider for this current word_j.
                """
                if found_word:
                    self.solve_word_j(words_to_pass, j+1, word_0)

            # Exit condition 2: All search options exhausted so current word is not valid.
            if (len(self.solution) == j) and (j != 0) and (try_count == total_tries):
                """
                Resets back to the previous word level if no new words added and options exhausted.
                Protects against exiting to 'before' the base level since this can't be done.
                """
                self.solution.pop()
                break

    def run(self):
        self.solve_word_j(self.words, j=0)
        return self.solution
