"""
링크 - https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""
from collections import defaultdict
from itertools import permutations
from operator import itemgetter

import functools

def solution(genres, plays):
    answer = []
    genre_play_dict = defaultdict(int)
    genres_play_tuple = []
    for index, data in enumerate(zip(genres, plays)):
        genre_play_dict[data[0]] += data[1]
        genres_play_tuple += [(index, data)]

    # dict에 담겨진 값을 가지고, 각 장르별로 우선순위가 높은 키를 찾는다.
    sorted_genres_play_list = sorted(genres_play_tuple, key=lambda x: (x[1][0], -x[1][1]))
    genre_rank = [genre for genre, play in sorted(genre_play_dict.items(), key=lambda x: x[1], reverse=True)]

    for music_rank in genre_rank:
        count = 0
        for i in sorted_genres_play_list:
            if i[1][0] == music_rank and count < 2:
                answer.append(i[0])
                count += 1
            else:
                continue

    return answer

# def solution(genres, plays):
#     genre_play_dict = defaultdict(lambda: 0)
#     for genre, play in zip(genres, plays):
#         genre_play_dict[genre] += play
#     genre_rank = [genre for genre, play in sorted(genre_play_dict.items(), key=itemgetter(1), reverse=True)]
#     final_dict = defaultdict(lambda: [])
#     for i, genre_play_tuple in enumerate(zip(genres, plays)):
#         final_dict[genre_play_tuple[0]].append((genre_play_tuple[1], i))
#     answer = []
#     for genre in genre_rank:
#         one_genre_list = sorted(final_dict[genre], key=itemgetter(0), reverse=True)
#         if len(one_genre_list) > 1:
#             answer.append(one_genre_list[0][1])
#             answer.append(one_genre_list[1][1])
#         else:
#             answer.append(one_genre_list[0][1])
#     return answer

if __name__ == "__main__":
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
