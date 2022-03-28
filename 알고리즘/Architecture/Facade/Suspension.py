

class Suspension(object):
    """
    * 자동차 서스펜션 클래스를 정의한다.
    """
    def __init__(self, load, type='mcpherson') -> None:
        self.type = type
        self.load = load
