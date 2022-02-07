clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]


from itertools import combinations
import math

# {'yellow_hat': [], 'blue_sunglasses': [], 'green_turban': []}
clothes_dict = {id[1]:[] for id in clothes}
result = 1
for i in clothes:
    # {'headgear': ['yellow_hat', 'green_turban'], 'eyewear': ['blue_sunglasses']}
    clothes_dict[i[1]].append(i[0])

for key in clothes_dict.keys():
    result = result * (len(clothes_dict[key]) + 1)
print(result - 1)