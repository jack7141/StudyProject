'''
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 "#####두 개씩 모아#####" 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
'''

# 각 장르별 총 횟수를 더해서 순위를 결정함
#  각 장르별에서 나온 순위를 기반으로 앨범을 구성함


# 
from functools import reduce
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

genres_dict = {id:[] for id in genres}
zip_lists = list(zip(genres, plays))
genres_dict_list = {}
ranking_list = []
answer = []

for i in zip_lists:
    # {'classic': [500, 150, 800], 'pop': [600, 2500]}
    genres_dict[i[0]].append(i[1])

for key, value in genres_dict.items():
    genres_dict_list[key] = reduce(lambda x, y: x + y, genres_dict[key])

# 장르별 합계 순위로 가장 많은 순서 ["pop", "classic"]	
ranklist = sorted(genres_dict_list,  key=lambda x: x[1], reverse=True)

print(genres_dict)
print(ranklist)
for key in ranklist:
    if len(genres_dict[key]) > 1:
        ranking_list.append(sorted(genres_dict[key], reverse=True)[:2])
    else:
        ranking_list.append(sorted(genres_dict[key]))
print(ranking_list)

for rank in ranking_list:
    for v in rank:
        answer.append(plays.index(v))

print(answer)