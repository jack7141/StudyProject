from itertools import permutations

"""
* 문자열 슬라이싱 기초 
순차적으로 숫자를 증가시키면서 문자열을 잘라낸다.
"""

def solution(s):
    answer = []
    word_dict = {}
    for index, word in enumerate(list(s)):
        if word not in word_dict:
            answer.append(-1)
            word_dict[word] = index
        else:
            answer.append(index - word_dict[word])
            word_dict[word] = index
    return answer

s = "banana"

if __name__ == "__main__":
    solution(s)