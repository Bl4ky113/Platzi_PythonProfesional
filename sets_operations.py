#!/usr/bin/python3

if __name__ == "__main__":
    set_1 = {1, 2, 3, 4, 5}
    set_2 = {5, 6, 7, 8, 9}

    print(set_1 | set_2)
    print(set_1 & set_2)
    print(set_1 - set_2)
    print(set_2 - set_1)
    print(set_1 ^ set_2)

    for i in range(20):
        print(i, set_1, set_2)
