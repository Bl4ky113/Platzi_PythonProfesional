#!/usr/bin/python3

from random import randint

def output_to_upper (function):
    def wrapper (*arg: any) -> str:
        return function(*arg).upper()
    
    return wrapper

@output_to_upper
def check_new_emails (email: str) -> str:
    return f"{email}, has {randint(1, 10)} new Emails"

if __name__ == "__main__":
    print(check_new_emails("bl4ky"))
