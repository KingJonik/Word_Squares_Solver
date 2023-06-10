class TestHelpers:
    @staticmethod
    def evaluate_symmetry(result, expected_case_length):
        """
        Assesses the word square result is valid through symmetry.
        :param result: The word square result.
        :param expected_case_length: Number of rows/cols to iterate over.
        :return: True/False - Condition met or not
        """
        symmetrical_square = True
        for row in range(0, expected_case_length):
            for column in range(0, expected_case_length):
                if result[row][column] != result[column][row]:
                    symmetrical_square = False

        return symmetrical_square

    @staticmethod
    def evaluate_character_strings(result, input_string):
        """
        Checks word square stringifies to the same as the input string.
        :param result: The word square result.
        :param input_string: The string to compare against.
        :return: True/False - Condition met or not.
        """
        word_square_string = "".join(result)
        sorted_word_square_string = "".join(sorted(word_square_string))

        return sorted_word_square_string == input_string
