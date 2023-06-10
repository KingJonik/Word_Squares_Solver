import unittest

from main import FindSolution
from test_helpers import TestHelpers
from word_square_finder import WordSquareFinder


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Helper Classes
        cls.test_helpers = TestHelpers()

    def test_word_square_finder(self):
        """
        A shorter test case to help with stepping through WordSquareFinder whilst debugging.
        """
        # Test Scenario
        words = ["aced", "moan", "acme", "once", "demo", "made", "caca", "mean", "need", "omen"]
        length = 4
        singles = ["d"]
        input_string = "aaccdeeeemmnnnoo"
        expected_result = ["moan", "once", "acme", "need"]

        # Run Case
        result = WordSquareFinder(words, length, singles, input_string).run()

        # Assert
        self.assertEqual(expected_result, result)

    def test_case_1(self):
        # Test Scenario
        case = "4 eeeeddoonnnsssrv"
        expected_case_length = 4
        expected_case_string = "".join(sorted("eeeeddoonnnsssrv"))

        # Run Case
        actual_result = FindSolution(case).run()

        # Evaluate Results
        same_string = self.test_helpers.evaluate_character_strings(actual_result, expected_case_string)
        symmetrical = self.test_helpers.evaluate_symmetry(actual_result, expected_case_length)

        # Assertions
        self.assertTrue(same_string)
        self.assertTrue(symmetrical)

    def test_case_2(self):
        # Test Scenario
        case = "4 aaccdeeeemmnnnoo"
        expected_case_length = 4
        expected_case_string = "".join(sorted("aaccdeeeemmnnnoo"))

        # Run Case
        actual_result = FindSolution(case).run()

        # Evaluate Results
        same_string = self.test_helpers.evaluate_character_strings(actual_result, expected_case_string)
        symmetrical = self.test_helpers.evaluate_symmetry(actual_result, expected_case_length)

        # Assertions
        self.assertTrue(same_string)
        self.assertTrue(symmetrical)

    def test_case_3(self):
        # Test Scenario
        case = "5 aaaeeeefhhmoonssrrrrttttw"
        expected_case_length = 5
        expected_case_string = "".join(sorted("aaaeeeefhhmoonssrrrrttttw"))

        # Run Case
        actual_result = FindSolution(case).run()

        # Evaluate Results
        same_string = self.test_helpers.evaluate_character_strings(actual_result, expected_case_string)
        symmetrical = self.test_helpers.evaluate_symmetry(actual_result, expected_case_length)

        # Assertions
        self.assertTrue(same_string)
        self.assertTrue(symmetrical)

    def test_case_4(self):
        # Test Scenario
        case = "5 aabbeeeeeeeehmosrrrruttvv"
        expected_case_length = 5
        expected_case_string = "".join(sorted("aabbeeeeeeeehmosrrrruttvv"))

        # Run Case
        actual_result = FindSolution(case).run()

        # Evaluate Results
        same_string = self.test_helpers.evaluate_character_strings(actual_result, expected_case_string)
        symmetrical = self.test_helpers.evaluate_symmetry(actual_result, expected_case_length)

        # Assertions
        self.assertTrue(same_string)
        self.assertTrue(symmetrical)

    def test_case_5(self):
        # Test Scenario
        case = "7 aaaaaaaaabbeeeeeeedddddggmmlloooonnssssrrrruvvyyy"
        expected_case_length = 7
        expected_case_string = "".join(sorted("aaaaaaaaabbeeeeeeedddddggmmlloooonnssssrrrruvvyyy"))

        # Run Case
        actual_result = FindSolution(case).run()

        # Evaluate Results
        same_string = self.test_helpers.evaluate_character_strings(actual_result, expected_case_string)
        symmetrical = self.test_helpers.evaluate_symmetry(actual_result, expected_case_length)

        # Assertions
        self.assertTrue(same_string)
        self.assertTrue(symmetrical)


if __name__ == '__main__':
    unittest.main()
