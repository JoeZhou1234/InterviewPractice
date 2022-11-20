"""
Given a string s containing a set of words, transform it such that the words appear in the reverse order.
One or more spaces separate words in s.
"""

s = "this is a string containing a set of words"


def reverse_string(s: str)->str:
    word_list = s.split(" ")
    s_reversed = ""
    for word in word_list:
        s_reversed = word + " " + s_reversed
    return s_reversed


print(reverse_string(s))

# The suggested answer was to reverse the whole string, then reverse each individual word


"""
Given an unsorted set of numbers from 1 to N with exactly two missing numbers, find those two missing numbers
"""

int_set = {10,3,5,6,1,4,8,11,2}


def find_missing_numbers(int_set: set)->set:
    total = 0
    N = 2
    for number in int_set:
        total = total - number
        N = N + 1

    total += N*(N + 1)//2  # total is the sum of the 2 missing numbers
    average = total//2  # average is the average of the 2 missing numbers
    smaller_number = average*(average + 1)//2

    for number in int_set:
        if number <= average:
            smaller_number -= number

    return {smaller_number, total - smaller_number}


print(find_missing_numbers(int_set))

# this answer is the revised answer according to the solution idea (to go from O(N^2) complexity to O(N) complexity)
