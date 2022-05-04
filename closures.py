#!/usr/bin/python3

def make_word_repeater (word: str):
    assert type(word) == str, "string only"
    def word_repeater (num_reps: int):
        final_word: str = word * num_reps

        return final_word

    return word_repeater

if __name__ == "__main__":
    joe_hawley_attacks = make_word_repeater("Joe Hawley ")
    print(joe_hawley_attacks(64))

