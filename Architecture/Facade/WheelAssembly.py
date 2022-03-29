from .Wheel import Wheel


class WheelAssembly(object):
    """
    * 자동차 휠 어셈블리 클래스를 정의한다.
    """
    def __init__(self, brake, suspension) -> None:
        self.brake = brake
        self.suspension = suspension
        self.wheels = Wheel(material='합금', diameter='M12', pitch=1.25)

    def apply_brakes(self):
        """
        * 브래이크 적용
        """
        print('Applying brakes')
        self.brake.engage
