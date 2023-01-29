from itertools import permutations, combinations

"""
리스트에서 각각의 점수를 통해서 등수를 구하는 방법
"""


from collections import Counter
import re


def solution(my_string):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string


if __name__ == "__main__":
    print(solution("nice to meet you"))

