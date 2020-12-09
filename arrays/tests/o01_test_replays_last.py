import unittest
from o01_replays_last import replace_last

TESTS = {
    "Basics": [
        {
            "input": [[2,3,4,1]],
            "answer": [1,2,3,4],
        },
        {
            "input": [[1,2,3,4]],
            "answer": [4,1,2,3],
        },
        {
            "input": [[1]],
            "answer": [1],
        },
        {
            "input": [[]],
            "answer": [],
        },
    ],
    "Extra": [
        {
            "input": [[10, 10]],
            "answer": [10, 10],
        },
        {
            "input": [[2,2,2,1]],
            "answer": [1,2,2,2],
        },
        {
            "input": [[100]],
            "answer": [100],
        },
    ]
}

class TestReplaysLast(unittest.TestCase):
    def test_replays_last(self):
        for level in TESTS:
            for test_case in TESTS[level]:
                actual = replace_last(test_case["input"][0])
                assert actual == test_case["answer"], f'Expected replace_last({test_case["input"]}) to be {test_case["answer"]}, got {actual}'
        

if __name__ == '__main__':
    unittest.main()