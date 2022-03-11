import functools
 
def comparator(a,b):
    t1, t2 = a+b, b+a
    print(f"comparator: {a},{b} -> {t1},{t2} -> {(int(t1) > int(t2)) - (int(t1) < int(t2))}")
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
 
def solution(numbers):
    n = list(map(str, numbers))
    print(f'input -> {n}')
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    print(f'n -> {n}')
    answer = str(int(''.join(n)))
    return answer
 
if __name__ == "__main__":
    print('-' * 40)
    numbers = [[6, 10, 2], [3, 30, 34, 5, 9], [0,0,0,0,0,0]]
    correct_answer = ["6210", "9534330", "0"]
 
    for t in range(len(numbers)):
        answer = solution(numbers[t])
        print('answer :' + answer, '/ correct_answer :' + correct_answer[t])
        if correct_answer[t] == answer:
            print(f'테스트 {t}를 통과하였습니다.')
        else:
            print(f'테스트 {t}를 통과하지 못했습니다.')
        print('-'* 40)