#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        while count < x:
            print(my_list[count], end="")
            count += 1
        print()
    except IndexError:
        print()
    finally:
        return count
