#!/usr/bin/python3

def fibonacci_generator (max_num:int=None):
    num_iterations: int = 0

    num_1: int = 0
    num_2: int = 1

    while not max_num or num_iterations <= max_num:
        num_iterations += 1

        if num_iterations == 1:
            yield num_1
        elif num_iterations == 2:
            yield num_2

        result_sum: int = num_1 + num_2
        num_1, num_2 = num_2, result_sum
        yield result_sum

if __name__ == "__main__":
    fibonacci = fibonacci_generator(10)

    for number in fibonacci:
        print(number)
