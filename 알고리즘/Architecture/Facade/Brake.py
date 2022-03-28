class Brake(object):
    """
    * 자동차 브레이크 클래스를 정의한다.
    """
    def __init__(self, number, type='disc') -> None:
        self.type = type
        self.number = number
    
    def engage(self):
        """
        * 브레이크 작동!
        """
        print(f'{self.__class__.__name__}, {self.number} engaged')

    def release(self):
        """
        * 브레이크 풀기 
        """
        print(f'{self.__class__.__name__}, {self.number} release')

