'''
문제 설명
0부터 9까지의 정수를 영어로 읽으면 “zero, one, two, three, four, five, six, seven, eight, nine”이 됩니다. 이 단어들만 사용하여 숫자의 각 자릿수를 읽으려고 합니다. 예를 들어 147의 각 자릿수를 순서대로 읽으면 one, four, seven이 되며 붙여서 “onefourseven”이 됩니다. 읽으려고 하는 숫자 num이 매개변수로 주어질 때, 이 숫자의 각 자릿수를 위의 단어들만 사용하여 읽은 결과를 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

제한사항
숫자 num의 범위 : 0 ≤ num ≤ 100,000,000, num은 정수
return 하는 문자열은 전부 소문자이어야 합니다.
입출력 예
num	result
147	"onefourseven"
5	"five"
1112	"oneoneonetwo"
입출력 예 설명
입출력 예 #1
147은 one, four, seven으로 읽으며, 붙여서 "onefourseven"이 됩니다.

입출력 예 #2
5는 five로 읽으며 붙여서 "five"가 됩니다.

입출력 예 #3
1112는 one, one, one, two로 읽으며 붙여서 "oneoneonetwo"가 됩니다.
'''
def solution(num):
    number = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 0:'zero'}
    answer = ""
    for i in str(num):
        answer += number[int(i)]
    return answer