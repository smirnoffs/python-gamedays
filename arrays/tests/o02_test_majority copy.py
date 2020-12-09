import unittest
from o02_majority import is_majority

TESTS = {
    "Basics": [
        {
            "input": [[True, True, False, True, False]],
            "answer": True
        },
        {
            "input": [[True, True, False]],
            "answer": True
        },
        {
            "input": [[True, True, False, False]],
            "answer": False
        },
        {
            "input": [[True, True, False, False, False]],
            "answer": False
        },
        {
            "input": [[False]],
            "answer": False
        },
        {
            "input": [[True]],
            "answer": True
        },
        {
            "input": [[]],
            "answer": False
        },
    ],
    "Extra": [
        {
            "input": [[False, False, True]],
            "answer": False
        },
        {
            "input": [[False, False, False]],
            "answer": False
        },
        {
            "input": [[True, True, True]],
            "answer": True
        },
    ]
}

class TestMajority(unittest.TestCase):
    def test_replays_last(self):
        for level in TESTS:
            for test_case in TESTS[level]:
                test_input = test_case["input"][0]
                actual = is_majority(test_input)
                assert actual == test_case["answer"], f'Expected is_majority({test_input}) to be {test_case["answer"]}, got {actual}'
        

if __name__ == '__main__':
    unittest.main()