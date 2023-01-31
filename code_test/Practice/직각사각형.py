"""
링크 - https://school.programmers.co.kr/learn/courses/30/lessons/86491
"""

def solution(sizes):
    answer = 0
    # 리스트에서 큰거는 가로쪽으로 작은거는 왼쪽으로 몰아준다.
    width_list = []
    height_list = []
    for i in sizes:
        # size list를 전체를 순회하면서, 가로에 큰것을 몰아주고, 세로엔 작은것을 몰아준다.
        # ex) [60, 50] 이 경우는 가로가 크기 때문에 가로 리스트에 60을 넣어주고, 세로에 50을 넣어준다.
        if i[0] >= i[1]:
            width_list.append(i[0])
            height_list.append(i[1])
        else:
            # ex) [30, 70] 이 경우는 가로가 세로보다 작기 때문에 세로를 가로로 넣어주고, 가로를 세로로 넣어준다.
            # 이렇게 되면, 가로 리스트엔 리스트 요소들 중 큰것들만 담기고 세로 리스트엔 리스트 요소중 작은것들만 모인다.
            width_list.append(i[1])
            height_list.append(i[0])
    return max(width_list) * max(height_list)

if __name__ == "__main__":
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))