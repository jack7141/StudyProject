"""
반복을 위해 정의한 로직을 사용해 자체 이터러블을 만들어본다.
1. 이터러블 -> __iter__ 매직 메서드를 구현한 객체
2. 이터레이터 -> __next__ 매직 메서드를 사용한 객체
"""
# 이터러블 객체 만들기
from datetime import timedelta, date


class DateRangeContainerIterable:
    """자체 이터레이터 메서드를 가지고 있는 이터러블"""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        """첫번째 예제에서는 __iter__가 self를 반환하여 객체를 한번만 사용할 수 있었지만,
        __iter__에서 yield를 사용하여 제너레이터를 발생시켜 매번 새로운 이터레이터를 생성하여 활용할 수 있다.
        """
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)


if __name__ == '__main__':
    r1 = DateRangeContainerIterable(date(2019, 1, 30), date(2019, 2, 5))
    print(", ".join(map(str, r1)))
    print(max(r1))

    for day in DateRangeContainerIterable(date(2019, 1, 30), date(2019, 2, 5)):
        print(day)
