import unittest
from o03_frequency_sorting import frequency_sorting

TESTS = {
    "Basics": [
        {
            "input": [1, 2, 3, 4, 5],
            "answer": [1, 2, 3, 4, 5]
        },
        {
            "input": [3, 4, 11, 13, 11, 4, 4, 7, 3],
            "answer": [4, 4, 4, 3, 3, 11, 11, 7, 13]
        }
    ],
    "Extra": [
        {
            "input": [99, 99, 55, 55, 21, 21, 10, 10],
            "answer": [10, 10, 21, 21, 55, 55, 99, 99]
        },
        {
            "input": [5, 6, 13, 99, 45, 34, 99, 6, 6, 45],
            "answer": [6, 6, 6, 45, 45, 99, 99, 5, 13, 34]
        }
    ]
}

class TestMajority(unittest.TestCase):
    def test_replays_last(self):
        for level in TESTS:
            for test_case in TESTS[level]:
                test_input = test_case["input"]
                actual = frequency_sorting(test_input)
                assert actual == test_case["answer"], f'Expected frequency_sorting({test_input}) to be {test_case["answer"]}, got {actual}'
        

if __name__ == '__main__':
    unittest.main()