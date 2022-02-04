'''
문제 설명
신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.

각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.
다음은 전체 유저 목록이 ["muzi", "frodo", "apeach", "neo"]이고, k = 2(즉, 2번 이상 신고당하면 이용 정지)인 경우의 예시입니다.

유저 ID	유저가 신고한 ID	설명
"muzi"	"frodo"	"muzi"가 "frodo"를 신고했습니다.
"apeach"	"frodo"	"apeach"가 "frodo"를 신고했습니다.
"frodo"	"neo"	"frodo"가 "neo"를 신고했습니다.
"muzi"	"neo"	"muzi"가 "neo"를 신고했습니다.
"apeach"	"muzi"	"apeach"가 "muzi"를 신고했습니다.
각 유저별로 신고당한 횟수는 다음과 같습니다.

유저 ID	신고당한 횟수
"muzi"	1
"frodo"	2
"apeach"	0
"neo"	2
위 예시에서는 2번 이상 신고당한 "frodo"와 "neo"의 게시판 이용이 정지됩니다. 이때, 각 유저별로 신고한 아이디와 정지된 아이디를 정리하면 다음과 같습니다.

유저 ID	 유저가 신고한 ID	    정지된 ID
"muzi"	  ["frodo", "neo"]	 ["frodo", "neo"]
"frodo"	  ["neo"]	          ["neo"]
"apeach"  ["muzi", "frodo"]	 ["frodo"]
"neo"	   없음	               없음
따라서 "muzi"는 처리 결과 메일을 2회, "frodo"와 "apeach"는 각각 처리 결과 메일을 1회 받게 됩니다.

이용자의 ID가 담긴 문자열 배열 id_list, 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report, 정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때, 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.

id_list	report	k	result
["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2	[2,1,1,0]
["con", "ryan"]	["ryan con", "ryan con", "ryan con", "ryan con"]	3	[0,0]
'''
from optparse import Values
from typing import Counter


id_list = ["muzi", "frodo", "apeach", "neo"]
reports = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

# 유저가 신고한 ID를 조합하고, 그중에서 정지된 ID의 갯수를 리턴한다.
#  각 유저가 신고한 ID를 key value로 묶기
# 목표
# 신고한 아이디 리스트값
# {'muzi': ['frodo', 'neo'], 'frodo': ['neo'], 'apeach': ['frodo', 'muzi'], 'neo': []}
# 신고 당한 아이디 명수
# {'frodo': 2, 'neo': 2, 'muzi': 1}
# 결과
# [2,1,1,0]

answer = [0]*len(id_list)
id_dict = {i:[] for i in id_list}
penalty = []
# for i, data in set(enumerate(reports)):
for i in set(reports):
    name = i.split(" ")[0]
    report_name = i.split(" ")[1]
    # penalty.append(report_name)

    # {'muzi': ['frodo', 'neo'], 'frodo': ['neo'], 'apeach': ['frodo', 'muzi'], 'neo': []}
    # {'muzi': ['apeach'], 'frodo': ['muzi', 'apeach'], 'apeach': [], 'neo': ['frodo', 'muzi']}
    # {신고당한놈: [신고한놈들]}
    id_dict[report_name].append(name)

# k만큼 신고당한 인원만
# {'frodo', 'neo'}
# print(id_dict)
# penalty = set([i for i in penalty if penalty.count(i) >= k])

for key, value in id_dict.items():
    # print(value)
    if len(value) >= k:
        for v in value:
            answer[id_list.index(v)] += 1
# print(answer)


def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    # 신고당한놈을 기준으로 dict에 값추가
    for r in set(report):
        reports[r.split()[1]] += 1
    
    for r in set(report):
        # 신고당한놈이 K값 보다 크면
        if reports[r.split()[1]] >= k:
            # idList에서 신고한놈 위치에 +1
            answer[id_list.index(r.split()[0])] += 1

    return answer
solution(id_list, reports, k)
'''
for key, value in id_dict.items():
    id_dict[key] = list(set(id_dict[key]))


report_dict = dict(Counter(report_name_list))
print(report_dict)

report_dict = {key: value for key, value in report_dict.items() if value >= k}


test_dict = {i:0 for i in id_list}
for i in report_dict:
    for key, value in id_dict.items():
        if i in value:
            test_dict[key] += 1

print(test_dict)
'''













