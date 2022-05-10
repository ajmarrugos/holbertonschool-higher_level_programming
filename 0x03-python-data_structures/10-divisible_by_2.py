#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_lst = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_lst.append(True)
        else:
            new_lst.append(False)
    return new_lst
