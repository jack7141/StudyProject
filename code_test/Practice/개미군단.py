"""
개미 군단이 사냥을 나가려고 합니다.
개미군단은 사냥감의 체력에 딱 맞는 병력을 데리고 나가려고 합니다.
장군개미는 5의 공격력을, 병정개미는 3의 공격력을 일개미는 1의 공격력을 가지고 있습니다.
예를 들어 체력 23의 여치를 사냥하려고 할 때,
일개미 23마리를 데리고 가도 되지만,
장군개미 네 마리와 병정개미 한 마리를 데리고 간다면 더 적은 병력으로 사냥할 수 있습니다.
사냥감의 체력 hp가 매개변수로 주어질 때,
사냥감의 체력에 딱 맞게 최소한의 병력을 구성하려면 몇 마리의 개미가 필요한지를
return하도록 solution 함수를 완성해주세요.

링크 - https://school.programmers.co.kr/learn/courses/30/lessons/120837
"""

# Sol 1)
def solution(hp):
    king = hp // 5
    mid = (hp-(king*5)) // 3
    normal = (hp-(king*5)-(mid*3)) // 1
    return king+mid+normal

# Sol 2)
def solution(hp):
    answer = 0
    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant) # num1을 num2로 나눈 몫과 나머지를 출력하는 함수
        answer += d # hp를 각 수로 나눈 몫을 누적
    return answer


if __name__ == "__main__":
    print(solution(23))