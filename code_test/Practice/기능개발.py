"""
https://www.acmicpc.net/problem/1303

bfs에서 인자를 바꾸는 이유
https://good-potato.tistory.com/84
https://printscanf.tistory.com/entry/DFS-DFS%EC%97%90%EC%84%9C-xy-%EC%A2%8C%ED%91%9C%EB%A5%BC-%EB%92%A4%EC%A7%91%EB%8A%94%EB%B0%94%EA%BE%B8%EB%8A%94-%EC%9D%B4%EC%9C%A0
"""
import sys
from collections import deque
def solution(n, m, x_axis, y_axis):
    x_big = 0
    if len(x_axis) == 1:
        x_big = x_axis[0]
        x_big = x_big if n - x_axis[0] <= x_big else n - x_axis[0]
    elif len(x_axis) == 0:
        x_big = n
    else:
        for index_x in range(len(x_axis)):
            if index_x == 0:
                x_big = x_axis[index_x]
            elif index_x == len(x_axis) - 1:
                if x_axis[index_x] - x_axis[index_x - 1] <= x_big:
                    x_big = x_big
                else:
                    x_big = x_axis[index_x] - x_axis[index_x - 1]
                if n - x_axis[index_x] <= x_big:
                    x_big = x_big
                else:
                    x_big = n - x_axis[index_x]
            else:
                if x_axis[index_x] - x_axis[index_x - 1] <= x_big:
                    x_big = x_big
                else:
                    x_big = x_axis[index_x] - x_axis[index_x - 1]
    y_big = 0
    if len(y_axis) == 1:
        y_big = y_axis[0]
        y_big = y_big if m - y_axis[0] <= y_big else m - y_axis[0]
    elif len(y_axis) == 0:
        y_big = m
    else:
        for index_y in range(len(y_axis)):

            if index_y == 0:
                y_big = y_axis[index_y]
            elif index_y == len(y_axis) - 1:
                y_big = y_big if y_axis[index_y] - y_axis[index_y - 1] <= y_big else y_axis[index_y] - y_axis[
                    index_y - 1]
                y_big = y_big if m - y_axis[index_y] <= y_big else m - y_axis[index_y]
            else:
                y_big = y_big if y_axis[index_y] - y_axis[index_y - 1] <= y_big else y_axis[index_y] - y_axis[index_y - 1]
    answer = x_big * y_big
    return answer



def solution(M, load):
    answer = 0
    loads_temp = []
    sorted_load = sorted(load)
    queue = deque(sorted_load)
    while queue:
        # 가장 큰 수와 가장 작은 수를 더해서 비교
        for i in range(len(queue)):
            if queue[0] + queue[i] == M:
                queue.popleft()
                queue.pop(i)
                loads_temp.append(0)
                loads_temp.append(0)
                answer += 1
        # if queue[0] + queue[-1] == M:




        if sum(loads_temp) + queue[0] <= M:
            l = queue.popleft()
            loads_temp.append(l)
            if sum(queue) == 0 and sum(loads_temp) <= M:
                answer += 1
                break
        else:
            answer += 1
            loads_temp = []
            l = queue.popleft()
            loads_temp.append(l)
            queue.append(0)
    return answer
#
#
#
def solution(M, load):
    len_load = len(load)
    load = sorted(load, reverse=True)
    move_load = [0] * len_load
    answer = 0
    ok = True
    for weight in load:
        if weight > M:
            ok = False
            break
    if ok:
        for index in range(len_load):
            sum_load = load[index]
            move_load[index] = 1
            for index_end in range(len(load) - 1, -1, -1):
                if move_load[index_end]:
                    continue
                else:
                    if sum_load + load[index_end] <= M:
                        sum_load += load[index_end]
                        move_load[index_end] = 1
                    else:
                        break
            answer += 1
            if sum(move_load) == len_load:
                break
    else:
        answer = -1
    return answer


if __name__ == "__main__":
    # print(solution(10, [2, 3, 7, 8]))
    # print(solution(5, [2, 2, 2, 2, 2]))
    # print(solution(20, [16, 15, 9, 17, 1, 3]))
    print(solution(40, [20, 10, 30, 40, 32, 35, 15])) #5



