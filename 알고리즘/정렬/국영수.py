N = int(input())

score = []

for _ in range(N):
    [name, kor, eng, math] = map(str, input().split())
    
    score.append([name, int(kor), int(eng), int(math)])
    
sorted_score = sorted(score, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in sorted_score:
    print(i[0])