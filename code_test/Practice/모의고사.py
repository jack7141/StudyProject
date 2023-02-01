"""
링크 - https://school.programmers.co.kr/learn/courses/30/lessons/42840
"""

# def solution(answers):
#     answer = []
#     temp = []
#     num1 = [1, 2, 3, 4, 5]
#     num1_count = 0
#     num2 = [2, 1, 2, 3, 2, 4, 2, 5]
#     num2_count = 0
#     num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#     num3_count = 0
#     for i in range(len(answers)):
#         # 횟수를 문제의 횟수만큼 돌리기 위하여 아래와 같이 처리
#         num1_sol = i % 5
#         num2_sol = i % 8
#         num3_sol = i % 10
#
#         if num1[num1_sol] == answers[i]:
#             num1_count += 1
#         if num2[num2_sol] == answers[i]:
#             num2_count += 1
#         if num3[num3_sol] == answers[i]:
#             num3_count += 1
#
#     temp += [num1_count, num2_count, num3_count]
#
#     max_sol = max(temp)
#
#     if max_sol == temp[0]:
#         answer.append(1)
#     if max_sol == temp[1]:
#         answer.append(2)
#     if max_sol == temp[2]:
#         answer.append(3)
#     return answer


# SOL 2)
def solution(answers):
    result = []
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for idx, num in enumerate(answers):
        if num == num1[idx % len(num1)]:
            score[0] += 1
        if num == num2[idx % len(num2)]:
            score[1] += 1
        if num == num3[idx % len(num3)]:
            score[2] += 1
    for idx, i in enumerate(score):
        if i == max(score):
            result.append(idx + 1)
    return result

if __name__ == "__main__":
    print(solution([1,2,3,4,5,1,2,3,4]))