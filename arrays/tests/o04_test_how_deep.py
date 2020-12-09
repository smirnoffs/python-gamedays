import unittest
from o04_how_deep import how_deep

TESTS = {
    "Basics": [
        {
            "input": [[1,2,3]],
            "answer": 1
        },
        {
            "input": [[1,2, [3]]],
            "answer": 2
        },
        {
            "input": [[1,2,[3,[4]]]],
            "answer": 3
        },
        {
            "input": [[]],
            "answer": 1
        },
        {
            "input": [[[]]],
            "answer": 2
        },
        {
            "input": [[[[]]]],
            "answer": 3
        },
        {
            "input": [[1,[2],[3]]],
            "answer": 2
        },
        {
            "input": [[1,[[]],[3]]],
            "answer": 3
        },
        
    ],
    "Extra": [
        {
            "input": [[6, 3]],
            "answer": 1
        },
        {
            "input": [[6, 7]],
            "answer": 1
        },
        {
            "input": [[1,2,3]],
            "answer": 1
        },
        {
            "input": [[5, 2, [3]]],
            "answer": 2
        },
        {
            "input": [[1,2,[[3],[4]]]],
            "answer": 3
        },
        {
            "input": [[[],[]]],
            "answer": 2
        },
        {
            "input": [[[[],[],[]]]],
            "answer": 3
        },
        {
            "input": [[[1],[5],[3]]],
            "answer": 2
        },
        {
            "input": [[1, [2], [2, [3]]]],
            "answer": 3
        }
    ]
}

class TestMajority(unittest.TestCase):
    def test_replays_last(self):
        for level in TESTS:
            for test_case in TESTS[level]:
                test_input = test_case["input"][0]
                actual = how_deep(test_input)
                assert actual == test_case["answer"], f'Expected how_deep({test_input}) to be {test_case["answer"]}, got {actual}'
        

if __name__ == '__main__':
    unittest.main()