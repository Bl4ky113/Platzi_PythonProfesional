#!/usr/bin/python3

def make_division_by (divisor: int):
    assert divisor != 0,ZeroDivisionError

    def divide_by (num: int):
        assert num != 0, ZeroDivisionError
        return num / divisor

    return divide_by

if __name__ == "__main__":
    divide_by_3 = make_division_by(3)
    print(divide_by_3(21))

    divide_by_0 = make_division_by(0)
    print(divide_by_0(0))
