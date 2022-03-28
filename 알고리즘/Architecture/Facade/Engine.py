class Engine(object):
    """
    * 자동차 엔진 클래스를 정의한다.
    """
    def __init__(self, name, bhp, rpm, volume, cylinders=4, type='petrol') -> None:
        self.name = name
        self.bhp = bhp
        self.rpm = rpm
        self.volume = volume
        self.cylinders = cylinders
        self.type = type

    def start(self):
        """
        * 엔진 스타트!
        """
        print('Engine Start')

    def stop(self):
        """
        * 엔진 멈춤
        """
        print('Engine Stop')