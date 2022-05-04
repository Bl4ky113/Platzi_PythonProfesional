#!/usr/bin/python3

class FibonacciSequence ():
    def __init__ (self, max_num: int=None):
        self.max: int = max_num

    def __iter__ (self):
        self.num_1: int = 0
        self.num_2: int = 1
        self.num_iterations: int = 0
        self.result_sum: int = 0
        return self

    def __next__ (self):
        self.num_iterations += 1

        if self.num_iterations == 1:
            return self.num_1
        elif self.num_iterations == 2:
            return self.num_2

        if not self.max or self.num_iterations <= self.max:
            self.result_sum = self.num_1 + self.num_2

            self.num_1, self.num_2 = self.num_2, self.result_sum
            return self.result_sum
        else:
            raise StopIteration


if __name__ == "__main__":
    fibonacci = FibonacciSequence(10)

    for num in fibonacci:
        print(num)
