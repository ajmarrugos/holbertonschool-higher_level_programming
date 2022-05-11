#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    r_dic = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    roman_num = 0
    for j in range(len(roman_string)):
        if j > 0 and r_dic[roman_string[j]] > r_dic[roman_string[j - 1]]:
            roman_num += r_dic[roman_string[j]] - 2 * \
                        r_dic[roman_string[j - 1]]
        else:
            roman_num += r_dic[roman_string[j]]
    return roman_num
