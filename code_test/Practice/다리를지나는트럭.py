"""
https://www.acmicpc.net/problem/1303

bfs에서 인자를 바꾸는 이유
https://good-potato.tistory.com/84
https://printscanf.tistory.com/entry/DFS-DFS%EC%97%90%EC%84%9C-xy-%EC%A2%8C%ED%91%9C%EB%A5%BC-%EB%92%A4%EC%A7%91%EB%8A%94%EB%B0%94%EA%BE%B8%EB%8A%94-%EC%9D%B4%EC%9C%A0
"""
import sys
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 다리에 올라갈 수 있는 트럭의 갯수
    bridge = deque([0] * bridge_length)
    # 다리 위의 트럭 무게의 합
    bridge_weight = 0
    while truck_weights:
        answer += 1
        # 다리를 지난 트럭 무게들
        bridge_weight -= bridge.popleft()
        #
        if bridge_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            # 다리를 지나갈 수 있으니까 bridge에 담는다.
            bridge.append(truck)
            # 다리 무게에 트럭의 무게를 담는다.
            bridge_weight += truck
        else:
            bridge.append(0)

    # 왜지?
    while bridge_weight > 0:
        answer += 1
        bridge_weight -= bridge.popleft()

    return answer


if __name__ == "__main__":
    print(solution(2, 10, [7,4,5,6]))



