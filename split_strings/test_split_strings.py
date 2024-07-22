import unittest
from split_strings import solution

class TestSolution(unittest.TestCase):
    def test_basic_cases(self):
        tests = [
            ("asdfadsf", ['as', 'df', 'ad', 'sf']),
            ("asdfads", ['as', 'df', 'ad', 's_']),
            ("", []),
            ("x", ["x_"]),
        ]

        for inp, exp in tests:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(solution(inp), exp)

if __name__ == "__main__":
    unittest.main()
