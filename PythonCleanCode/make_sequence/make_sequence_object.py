"""
객체에 __iter__() 메서드를 정의하지 않았지만 반복을 원하는 경우도 있다.
iter() 함수는 객체 __iter__가 정의되어 있지 않으면 __getitem__을 찾고 없으면 TypeError를 발생시킨다.

이번 예제에서는 __len__과 __getitem__을 구현하고 첫 번째 인덱스 0부터 시작하여 포함된 요소를 한 번에
하나씩 차례로 가져올 수 있어야 한다. 즉, __getitem__을 올바르게 구현하여 이러한 인덱싱이 가능하도록 주의를 기울여야 한다.
"""
from datetime import timedelta, date


class DateRangeSequence:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        days = []
        current_day = self.start_date
        while current_day < self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days

    def __getitem__(self, item):
        return self._range[item]

    def __len__(self):
        return len(self._range)

if __name__ == '__main__':
    s1 = DateRangeSequence(date(2019, 1, 30), date(2019, 2, 6))
    for day in s1:
        print(day)

    print(s1[-1])
    print(s1[3])
    print(s1[1])
    print(s1[0])