#!/usr/bin/python3

def is_prime (number: int) -> bool:
    prime_number_base: tuple[int, ...] = (2, 3, 5, 7)
    number_is_prime = True

    for prime_number in prime_number_base:
        if number % prime_number == 0:
            number_is_prime = False
            break

    return number_is_prime

def check_prime_numbers (num_numbers: int) -> tuple[int, ...]:
    prime_numbers: list[int] = []
    
    for i in range(num_numbers):
        if is_prime(i + 1):
            prime_numbers.append(i + 1)

    return tuple(prime_numbers)

if __name__ == "__main__":
    prime_numbers: tuple[int, ...] = check_prime_numbers(50)
    print(prime_numbers)
