"""
You are given a tuple that consists of integers and other tuples, which in turn can also contain tuples.

Your task is to find out how deep this structure is or how deep the nesting of these tuples is.

Taking from https://github.com/CheckiO-Missions/checkio-mission-how-deep
"""


def how_deep(structure) -> int:
    # your code here
    return 1


if __name__ == '__main__':
    print("Example:")
    print(how_deep((1, 2, 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert how_deep((1, 2, 3)) == 1
    assert how_deep((1, 2, (3,))) == 2
    assert how_deep((1, 2, (3, (4,)))) == 3
    assert how_deep(()) == 1
    assert how_deep(((),)) == 2
    assert how_deep((((),),)) == 3
    assert how_deep((1, (2,), (3,))) == 2
    assert how_deep((1, ((),), (3,))) == 3




