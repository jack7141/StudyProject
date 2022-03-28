

class Wheel(object):
    """
    * 자동차 휠 클래스를 정의한다.
    """
    def __init__(self, material, diameter, pitch) -> None:
        self.material = material
        self.diameter = diameter
        self.pitch = pitch