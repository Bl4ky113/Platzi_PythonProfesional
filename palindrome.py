#!/usr/bin/python3

""" 
"""

def is_palindrome (text: str) -> bool:
    text = text.replace(" ", "").lower()
    reverse_text = text[::-1]

    return text == reverse_text
     

if __name__ == "__main__":
    print(is_palindrome("Ana"))
    print(is_palindrome("perro"))
    print(is_palindrome("hello"))
