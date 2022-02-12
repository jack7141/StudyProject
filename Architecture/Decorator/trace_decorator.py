def trace(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper       

def trace_decorator1(func):
    def wrapper():
        print('decorator1 기능')
        func()
    return wrapper
 
def trace_decorator2(func):
    def wrapper():
        print('decorator2 기능')
        func()
    return wrapper