"""
* Unpacking은 주로 반복되는 요소를 처리할 때 사용하는것이 가장 파이토닉한 방법
"""

USER = [(i, f"first_name:{i}", f"last_name:{i}")for i in range(1_000)]


class User:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        """
        __repr__이 있어야 아래와 같이 우리가 읽을 수 있는 형식으로 반환됨
        >>> [User(0, 'first_name:0', 'last_name:0'), User(1, 'first_name:1', 'last_name:1'),...]
        없으면? 아래와 같이 반환됨... __str__과 차이가 좀 있음
        >>> [<__main__.User object at 0x0000021344691F48>, <__main__.User object at 0x0000021344691F88>, ...]
        """
        return f"{self.__class__.__name__}({self.user_id!r}, {self.first_name!r}, {self.last_name!r})"


def bad_users_from_rows(dbrows) -> list:
    """A bad case (non-pythonic) of creating ``User``s from DB rows."""
    return [User(row[0], row[1], row[2]) for row in dbrows]


def users_from_rows(dbrows) -> list:
    """Create ``User``s from DB rows."""
    return [
        User(user_id, first_name, last_name)
        for (user_id, first_name, last_name) in dbrows
    ]

if __name__ == "__main__":
    print(USER)
    test_ = users_from_rows(USER)
    print(test_)