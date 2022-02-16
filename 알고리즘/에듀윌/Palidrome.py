'''
문제 설명
팰린드롬이란 뒤에서부터 읽어도 원래와 똑같은 문자열을 의미합니다.

예를 들어, abab는 팰린드롬 문자열이 아닙니다. 하지만 뒤에 a를 추가한다면 ababa가 되어 앞에서부터 읽을 때와 뒤에서부터 읽을 때가 똑같은 팰린드롬 문자열이 되고, 이때 문자열의 길이는 5가 됩니다. 이처럼 문자열이 주어질 때, 문자열의 뒤에 적절히 문자를 추가한다면 팰린드롬인 문자열로 만들 수 있습니다.

문자열이 주어질 때, 문자열의 뒤에 최소한의 문자를 추가해 팰린드롬 문자열로 만든 후, 만들어진 팰린드롬 문자열의 전체 길이를 return 하도록 solution 함수를 완성해주세요.

제한사항
문자열의 길이는 1,000 이하의 자연수입니다.
문자열은 모두 소문자로만 이루어져 있습니다.
입출력 예
plain	result
abab	5
abcde	9
입출력 예 설명
입출력 예 #1
'abab'의 뒤에 'a'를 추가하면 'ababa'가 되어 팰린드롬인 문자열이 되고 길이는 5 입니다.

입출력 예 #2
'abcde'의 뒤에 'dcba'를 추가하면 'abcdedcba'가 되어 팰린드롬인 문자열이 되고 길이는 9 입니다.
'''
def isPalidrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

def makePalidrome(plain):
    result = ''
    _plain = plain[:-1]
    for i in reversed(_plain):
        result = plain+i
        if isPalidrome(result):
            return result
        else:
            plain += i

def solution(plain):
    return len(makePalidrome(plain))



# 해당문제 답 왜 이게 답인지 모르겠음;;
# https://haerang94.tistory.com/166
def solution(plain):
    for i in range(len(plain)):
        if plain[i:]==plain[i:][::-1]:
            return len(plain)+i