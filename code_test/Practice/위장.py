"""
링크 - https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""
from collections import defaultdict
from itertools import permutations
from operator import itemgetter



def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(list)
    for i in clothes:
        clothes_dict[i[1]] += [i[0]]
    # dict_items([('headgear', ['yellow_hat', 'green_turban']), ('eyewear', ['blue_sunglasses'])])
    # clothes_dict

    clothes_count_list = []
    for i in clothes_dict.keys():
        answer = answer * (len(clothes_dict[i]) + 1)
    return answer - 1


if __name__ == "__main__":
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
    print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
