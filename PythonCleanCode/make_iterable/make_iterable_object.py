"""
반복을 위해 정의한 로직을 사용해 자체 이터러블을 만들어본다.
1. 이터러블 -> __iter__ 매직 메서드를 구현한 객체
2. 이터레이터 -> __next__ 매직 메서드를 사용한 객체
"""
# 이터러블 객체 만들기
from datetime import timedelta, date


class DateRangeIterable:
    """자체 이터레이터 메서드를 가지고 있는 이터러블"""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        """for문을 통해 iter() 함수를 호출하고, 함수는 __iter__로 위임한다.
        이 함수는 self를 반환하므로 객체 자신을 뜻하고, 자신이 이러러블임을 나타낸다.
        따라서 각 루프 단계마다 next() 함수를 호출하고 이는 __next__ 매직 메서드에게 위임한다.
        """
        return self

    def __next__(self):
        """더 이상 생성할 것이 없으면 rasise StopIteration를 발생시켜서 중지시켜준다.
        for 루프가 작동하는 원리는 StopIteration 예외가 발생할 때까지 next()를 호출하는 것과 같다.
        """
        if self._present_day >= self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


if __name__ == '__main__':
    # for 루프는 앞서 만든 객체를 사용해 새로운 반복을 시작한다.
    # 파이썬은 iter() 함수를 호출한다.
    # 이 클래스에서 문제는 for문을 통해서는 오류가 없지만, next를 활용하여 제너레이트를 시키면
    # 더이상 돌게 없어서 오류가 발생한다.
    for day in DateRangeIterable(date(2019, 1, 30), date(2019, 2, 5)):
        print(day)

    r1 = DateRangeIterable(date(2019, 1, 30), date(2019, 2, 5))
    print(", ".join(map(str, r1)))

    """
    에러 케이스
    r1 = DateRangeIterable(date(2019, 1, 30), date(2019, 2, 2))
    next(r1)
    next(r1)
    next(r1)
    next(r1)
    next(r1)
    next(r1)
    next(r1)
    """

    """하위 케이스는 2번 연달아서 제너레이터 시키지 못하기때문에
    ValueError: max() arg is an empty sequence와 같은 에러 발생 
    """
    print(max(r1))
